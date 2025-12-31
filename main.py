import asyncio
from bot import create_bot
import logging_config

async def main():
    logging_config.setup_logging()
    bot, dp = create_bot()
    import handlers
    handlers.register_handlers(dp)
    print("Бот AI IMAGE HD жёсткий от ANONYMOUS запущен!")
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())
