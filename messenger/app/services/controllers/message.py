"""
Message database controller service for cross-controller logic.
"""

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any

from messenger.app.dependencies.database import db_session
from messenger.app.exceptions import UnauthorizedException
from messenger.app.models import User, Message
from .base import BaseControllerService


class MessageControllerService(BaseControllerService):
    """
    Message database controller service.
    """
    
    def __inti__(
        self, session: AsyncSession = Depends(db_session)
    ) -> None:
        super().__init__(session=session)


    async def send_message(
        self, user: User, request: dict[str, Any]
    ) -> Message:
        """
        Send a message.
        """
        thread = await self.thread_controller.get_by({"id": request["thread_id"]})
        if user in await thread.awaitable_attrs.users:
            return await self.message_controller.create(
                **request, user_id = user.id
            )
        
        raise UnauthorizedException
    