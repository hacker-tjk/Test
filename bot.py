from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import config

def create_bot():
    # [span_2](start_span)Используем токен, который вы указали в config.py[span_2](end_span)
    bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
    return bot, dp
