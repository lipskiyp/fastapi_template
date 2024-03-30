"""
Message SQLAlchemy database repository.
"""

from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Message
from core.repositories import BaseRepository


class MessageRepository(BaseRepository):
    """
    Message SQLAlchemy database repository.
    """
    
    def __init__(
        self, session: AsyncSession
    ) -> None:
        super().__init__(model=Message, session=session)
