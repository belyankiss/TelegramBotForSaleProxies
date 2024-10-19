import functools

from aiogram.types import Message, ReplyKeyboardRemove

from proxy_bot.database.userorm import UpdateActionUser


def update_user_info(function):
    @functools.wraps(function)
    async def wrapper(msg: Message, *args, **kwargs):
        user = UpdateActionUser()
        if not await user.update_action(msg.from_user.id):
            return await function(msg, *args, **kwargs)
        else:
            await msg.answer(text="You are blocked", reply_markup=ReplyKeyboardRemove(remove_keyboard=True))

    return wrapper