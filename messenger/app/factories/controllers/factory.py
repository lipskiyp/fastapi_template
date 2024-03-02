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
    