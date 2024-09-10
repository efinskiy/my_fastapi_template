from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import sessionmaker
from app.core.config import settings


engine = create_async_engine(url=settings.SQLALCHEMY_DATABASE_URI)
session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_session() -> AsyncSession:
    async with session_maker() as session:
        yield session