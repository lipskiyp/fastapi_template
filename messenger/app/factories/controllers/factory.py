"""
Database controller factory.
"""

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from messenger.app.dependencies import db_session
import messenger.app.controllers as controllers
import messenger.app.repositories as repositories


class ControllerFactory:
    """
    Database controller factory.
    """

    @staticmethod
    def get_message_controller(
        session: AsyncSession = Depends(db_session)
    ) -> controllers.MessageController:
        """
        Returns Message database controller.
        """
        return controllers.MessageController(
            repository=repositories.MessageRepository(
                session=session
            )
        )

    
    @staticmethod
    def get_thread_controller(
        session: AsyncSession = Depends(db_session)
    ) -> controllers.ThreadController:
        """
        Returns Thread database controller.
        """
        return controllers.ThreadController(
            repository=repositories.ThreadRepository(
                session=session
            )
        )
    

    @staticmethod
    def get_user_controller(
        session: AsyncSession = Depends(db_session)
    ) -> controllers.UserController:
        """
        Returns User database controller.
        """
        return controllers.UserController(
            repository=repositories.UserRepository(
                session=session
            )
        )