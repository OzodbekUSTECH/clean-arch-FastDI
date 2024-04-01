from typing import AsyncIterable

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from fast_di import FastDIStub, DependencyCollector
from app.config import settings



db_collector = DependencyCollector()



@db_collector.singleton(AsyncEngine)
def provide_engine() -> AsyncEngine:
    return create_async_engine(settings.DATABASE_URL, echo=settings.ECHO)


@db_collector.singleton(async_sessionmaker[AsyncSession])
def provide_session_maker(
    engine: FastDIStub[AsyncEngine],
) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(bind=engine, expire_on_commit=False)


@db_collector.factory(AsyncSession)
async def provide_session(
    session_maker: FastDIStub[async_sessionmaker[AsyncSession]],
) -> AsyncIterable[AsyncSession]:
    async with session_maker() as session:
        yield session


