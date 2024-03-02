"""
Database FastAPI dependency injections.
"""

from sqlalchemy.ext.asyncio import AsyncSession

from messenger.core.database import session_maker


async def db_session() -> AsyncSession:
    async with session_maker() as session:
        try:
            yield session
            await session.commit()
        except Exception as e:
            await session.rollback()
            raise e
        finally:
            await session.close()
