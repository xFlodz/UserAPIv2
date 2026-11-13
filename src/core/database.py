from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from src.core.config import DatabaseVariables as DBV


DATABASE_URL = f'postgresql+asyncpg://{DBV.USER}:{DBV.PASSWORD}@{DBV.HOST}:{DBV.PORT}/{DBV.DATABASE}'


engine = create_async_engine(DATABASE_URL, echo=True)
Base = declarative_base()

async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session


async def create_tables():
    from src.models import user

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)