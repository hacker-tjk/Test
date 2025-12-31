# config.py
from pathlib import Path

TOKEN = "8505740315:AAHF0_gJXf8z_DRWN3TbOg3ofyoIShIJguA"
BOT_NAME = "AI 🧠 IMAGE HD"
COMPANY = "ANONYMOUS from Tajikistan"
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

BAD_WORDS = {
    "ты тупой": ["сам тупой", "пашол нафиг", "сам нафиг"],
    "иди нахуй": ["сам иди нахуй", "пошёл вон"],
}

TEXTS = {
    "ru": {
        "start": ("<b>Привет!</b>\n"
                  "Я - нейросеть <i>AI 🧠 IMAGE HD</i> от компании ANONYMOUS из Таджикистана.\n"
                  "Создаю картинки и видео с фирменной подписью.\nОтправь команду /help."),
        "help": ("/image &lt;текст&gt; — создать картинку\n"
                 "/video &lt;текст&gt; — создать видео\n"
                 "/start — перезапуск бота"),
        "bad_response": "Так себя вести некрасиво: {}",
        "no_prompt": "✏️ Пожалуйста, добавьте описание после команды.",
        "copy": "Текст скопирован. Используйте кнопку копирования."
    },
    "tj": {
        "start": ("<b>Салом!</b>\n"
                  "Ман - нейросети <i>AI 🧠 IMAGE HD</i> аз ширкати ANONYMOUS дар Тоҷикистон.\n"
                  "Тасвирҳо ва видео бо имзои махсус месозам.\n"
                  "Барои кӯмак /helpро нависед."),
        "help": ("/image &lt;матн&gt; — тасвир созед\n"
                 "/video &lt;матн&gt; — видео созед\n"
                 "/start — оғозшавӣ дубора"),
        "bad_response": "Рафтори шумо бад аст: {}",
        "no_prompt": "✏️ Лутфан пас аз фармон матнро нависед.",
        "copy": "Матн нусхабардорӣ шуд."
    },
    "en": {
        "start": ("<b>Hello!</b>\n"
                  "I am AI 🧠 IMAGE HD by ANONYMOUS from Tajikistan.\n"
                  "I create images and videos with branded watermark.\n"
                  "Type /help for commands."),
        "help": ("/image &lt;text&gt; — create image\n"
                 "/video &lt;text&gt; — create video\n"
                 "/start — restart bot"),
        "bad_response": "Unacceptable behavior: {}",
        "no_prompt": "✏️ Please provide text after the command.",
        "copy": "Text copied. Use copy button."
    }
}

# Множество провайдеров (бесплатных и популярных) для генерации (примеры)
IMAGE_PROVIDERS = [
    "bluewillow", "bing", "openai", "stablediffusion", "mj", "dalle2",
    "deepai", "huggingface", "replicate", "lexica"
]

VIDEO_PROVIDERS = [
    "deepbrain", "runwayml", "synthesia", "d-id", "kairos", "papercup"
]