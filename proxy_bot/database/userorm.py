from datetime import datetime

from aiogram.types import Message, CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from proxy_bot.database.models import User
from proxy_bot.database.session import async_session


class UserORM:
    def __init__(self):
        self.a_session = async_session


class CreateUser(UserORM):
    async def get_user_by_user_id(self, user_id: int, session: AsyncSession = None):
        if session is None:
            async with self.a_session() as session:
                return await session.get(User, user_id)
        return await session.get(User, user_id)

    @staticmethod
    async def _update_date_username_active(session: AsyncSession, user: User, username: str | None) -> User:
        user.username = username
        user.date_active = datetime.now()
        await session.commit()
        await session.refresh(user)
        return user

    @staticmethod
    async def _add_user(session: AsyncSession,
                        user_id: int,
                        username: str | None,
                        referral_id: int | None = None) -> User:
        date = datetime.now()
        user = User(user_id=user_id,
                    username=username,
                    date_registration=date,
                    referral_id=referral_id,
                    date_active=date)
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user

    async def create_user(self, event: Message | CallbackQuery) -> User:
        user_id = event.from_user.id
        username = event.from_user.username
        try:
            referral_id = int(event.text.split()[1])
        except IndexError:
            referral_id = None
        async with self.a_session() as session:
            user: User | None = await self.get_user_by_user_id(user_id, session)
            if user is not None:
                user = await self._update_date_username_active(session, user, username)
            else:
                if referral_id == user_id:
                    referral_id = None
                user = await self._add_user(session, user_id, username, referral_id)
            return user

class UpdateActionUser(CreateUser):
    async def update_action(self, user_id: int) -> "User.blocked":
        async with self.a_session() as session:
            user = await self.get_user_by_user_id(user_id, session)
            user.date_active = datetime.now()
            await session.commit()
            await session.refresh(user)
            return user.blocked