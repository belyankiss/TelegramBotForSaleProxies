from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from proxy_bot.configs.settings import settings

bot = Bot(settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
dp = Dispatcher()