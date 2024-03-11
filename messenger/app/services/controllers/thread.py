"""
Thread database controller service for cross-controller logic.
"""

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from uuid import UUID 

from messenger.app.dependencies.database import db_session
from messenger.app.exceptions import NotFoundException
from messenger.app.models import User
from .base import BaseControllerService


class ThreadControllerService(BaseControllerService):
    """
    Thread database controller service.
    """
    
    def __inti__(
        self, session: AsyncSession = Depends(db_session)
    ) -> None:
        super().__init__(session=session)


    async def add_or_remove_users_from_thread(
        self, thread_id: UUID, users_add: List[UUID], users_remove: List[UUID]
    ) -> List[User]:
        """
        Adds or removes users from a tread.
        """
        thread = await self.thread_controller.get_by({"id": thread_id})

        await thread.awaitable_attrs.users

        for user_id in users_add:  # for every user to be added
            try:
                user = await self.user_controller.get_by({"id": user_id})  
                if user not in thread.users: thread.users.append(user)  # add user to thread if not already in the thread
            except NotFoundException:
                pass

        for user_id in users_remove:  # for every user to be removed
            try:
                user = await self.user_controller.get_by({"id": user_id})  
                if user in thread.users: thread.users.remove(user)  # remove user from the tread only if already in the thread
            except NotFoundException:
                pass

        await self.session.commit()

        return thread.users
    