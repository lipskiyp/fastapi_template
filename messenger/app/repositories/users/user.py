"""
User SQLAlchemy database repository.
"""

from sqlalchemy.ext.asyncio import AsyncSession

from messenger.app.models import User
from messenger.core.repositories import BaseRepository


class UserRepository(BaseRepository):
    """
    User SQLAlchemy database repository.
    """
    
    def __init__(
        self, session: AsyncSession
    ) -> None:
        super().__init__(model=User, session=session)
