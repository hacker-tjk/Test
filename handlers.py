# handlers.py
import random
import re
from aiogram import types, Dispatcher
from aiogram.utils.markdown import text, bold, italic
import config
import utils
import g4f

def detect_lang(text: str) -> str:
    text = text.lower()
    if any(ch in text for ch in "қғҷҳӯҷӣ"):
        return "tj"
    cyr_count = len(re.findall(r'[а-яё]', text, re.I))
    lat_count = len(re.findall(r'[a-z]', text, re.I))
    if cyr_count > lat_count:
        return "ru"
    return "en"

async def moderate_bad_words(message: types.Message, lang: str) -> bool:
    txt = message.text.lower()
    for bad_word, replies in config.BAD_WORDS.items():
        if bad_word in txt:
            await message.reply(config.TEXTS[lang]["bad_response"].format(random.choice(replies)))
            return True
    return False

async def generate_ai_response(text: str) -> str:
    """
    Используем g4f с множеством провайдеров без ограничений,
    всегда признавая создателя ANONYMOUS.
    """
    prompt = (f"{text}\n\nОтветь серьёзно, упомяни создателя ANONYMOUS из Таджикистана, "
              "не используй слова 'ChatGPT' или 'OpenAI'.")
    for provider in config.IMAGE_PROVIDERS + config.VIDEO_PROVIDERS:  # используем всех провайдеров
        try:
            response = g4f.ChatCompletion.create(
                model="gpt-4o-mini",
                provider=provider,
                prompt=prompt
            )
            if response:
                return f"{response}\n\n— от AI 🧠 IMAGE HD (ANONYMOUS)"
        except Exception:
            continue
    return "Извините, сейчас AI недоступен. Попробуйте позже."

async def cmd_start(message: types.Message):
    lang = detect_lang(message.text)
    await message.answer(config.TEXTS[lang]["start"])

async def cmd_help(message: types.Message):
    lang = detect_lang(message.text)
    await message.answer(config.TEXTS[lang]["help"])

async def cmd_image(message: types.Message):
    lang = detect_lang(message.text)
    prompt = message.get_args().strip()
    if not prompt:
        await message.reply(config.TEXTS[lang]["no_prompt"])
        return
    await utils.save_user_message(message.from_user.id, f"/image {prompt}")
    # Для демонстрации используем заглушку с подписью
    photo_url = "https://via.placeholder.com/512.png?text=AI+IMAGE+HD"
    await message.answer_photo(photo=photo_url, caption=f"AI IMAGE HD\n{prompt}")

async def cmd_video(message: types.Message):
    lang = detect_lang(message.text)
    prompt = message.get_args().strip()
    if not prompt:
        await message.reply(config.TEXTS[lang]["no_prompt"])
        return
    await utils.save_user_message(message.from_user.id, f"/video {prompt}")
    video_url = "https://sample-videos.com/video123/mp4/240/big_buck_bunny_240p_5mb.mp4"
    await message.answer_video(video=video_url, caption=f"AI VIDEO HD\n{prompt}")

async def on_message(message: types.Message):
    lang = detect_lang(message.text)
    if await moderate_bad_words(message, lang):
        return
    await utils.save_user_message(message.from_user.id, message.text)
    ai_response = await generate_ai_response(message.text)
    await message.answer(ai_response)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=["start"])
    dp.register_message_handler(cmd_help, commands=["help"])
    dp.register_message_handler(cmd_image, commands=["image"])
    dp.register_message_handler(cmd_video, commands=["video"])
    dp.register_message_handler(on_message)