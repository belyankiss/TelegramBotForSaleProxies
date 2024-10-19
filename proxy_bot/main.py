import asyncio
import logging
import sys

from proxy_bot.handlers.start_handler import start_router
from proxy_bot.program_imports import bot, dp


async def main() -> None:
    dp.include_routers(start_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Bot stopped")

