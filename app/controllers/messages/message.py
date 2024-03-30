"""
Message database controller.
"""

from typing import Any
from uuid import UUID 

from app.exceptions import UnauthorizedException
from app.models import Message, User
from app.repositories import MessageRepository
from core.controllers import BaseController


class MessageController(BaseController):
    """
    Message database controller.
    """

    def __init__(
        self, repository: MessageRepository
    ) -> None:
        super().__init__(model=Message, repository=repository)


    async def update_message(
        self, id: UUID, user: User, request: dict[str, Any],
    ) -> Message:
        """
        Updates and returns a message.
        """
        message = await self.get_by({"id": id})
        if message.user_id != user.id:  # only sender can update message
            raise UnauthorizedException
        
        return await self.update_by(
            update_by={"id": message.id}, request=request
        )


    async def delete_message(
        self, id: UUID, user: User,
    ) -> None:
        """
        Deletes a message.
        """
        message = await self.get_by({"id": id})
        if message.user_id != user.id:  # only sender can delete message
            raise UnauthorizedException
        
        return await self.soft_delete_by(
            update_by={"id": message.id}
        )
        