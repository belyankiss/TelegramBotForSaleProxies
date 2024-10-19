from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from proxy_bot.configs.settings import settings

async_engine = create_async_engine(
    url=settings.DATABASE_URL_aiosqlite,
    echo=False,

)

async_session = async_sessionmaker(async_engine)