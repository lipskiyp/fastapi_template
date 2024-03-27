"""
User database controller service for cross-controller logic.
"""

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from uuid import UUID 

from messenger.app.dependencies.database import db_session
from messenger.app.exceptions import NotFoundException
from messenger.app.models import User
from .base import BaseControllerService


class UserControllerService(BaseControllerService):
    """
    User database controller service.
    """
    
    def __inti__(
        self, session: AsyncSession = Depends(db_session)
    ) -> None:
        super().__init__(session=session)


    async def add_or_remove_threads_from_user(
        self, user_id: UUID, threads_add: List[UUID], threads_remove: List[UUID]
    ) -> List[User]:
        """
        Adds or removes threads from a user.
        """
        user = await self.user_controller.get_by({"id": user_id})

        await user.awaitable_attrs.threads

        for thread_id in threads_add:  # for every user to be added
            try:
                thread = await self.thread_controller.get_by({"id": thread_id})  
                if thread not in user.threads: user.threads.append(thread)  # add thread to the user if not already in the user
            except NotFoundException:
                print("hey")
                pass

        for thread_id in threads_remove:  # for every user to be removed
            try:
                thread = await self.thread_controller.get_by({"id": thread_id})  
                if thread not in user.threads: user.threads.remove(thread)  # remove thread from the user only if already in the user
            except NotFoundException:
                pass

        await self.session.commit()

        return user.threads
    