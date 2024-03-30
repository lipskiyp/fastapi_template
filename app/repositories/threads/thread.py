"""
Thread SQLAlchemy database repository.
"""

from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Thread
from core.repositories import BaseRepository


class ThreadRepository(BaseRepository):
    """
    Thread SQLAlchemy database repository.
    """
    
    def __init__(
        self, session: AsyncSession
    ) -> None:
        super().__init__(model=Thread, session=session)
