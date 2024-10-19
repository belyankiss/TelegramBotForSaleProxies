from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardRemove

from proxy_bot.database.userorm import CreateUser
from proxy_bot.wrappers.blocked_wrapper import update_user_info

start_router = Router()
start_router.message.filter(F.chat.type == "private")


@start_router.message(CommandStart())
@update_user_info
async def start_page(msg: Message):
    new_user = CreateUser()
    user = await new_user.create_user(msg)


