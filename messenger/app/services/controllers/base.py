"""
Base database controller service for cross-controller logic.
"""

from abc import ABC
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from messenger.app.dependencies.database import db_session
from messenger.app.factories.controllers import ControllerFactory
import messenger.app.controllers as controllers


class BaseControllerService(ABC):
    """
    Base database controller service.
    """

    def __init__(
        self, session: AsyncSession = Depends(db_session)
    ) -> None:
        self.session = session
        self.controller_factory = ControllerFactory()
        self._init_controller()


    def _init_controller(self) -> None:
        """
        Initialise database controllers.
        """
        self._user_controller = None
        self._thread_controller = None
        self._message_controller = None


    @property
    def user_controller(self) -> controllers.UserController:
        """
        Returns or initializes User controller instance. 
        """
        if not self._user_controller: 
            self._user_controller = self.controller_factory.get_user_controller(
                session=self.session
            )
        return self._user_controller
    

    @property
    def thread_controller(self) -> controllers.ThreadController:
        """
        Returns or initializes Thread controller instance. 
        """
        if not self._thread_controller: 
            self._thread_controller = self.controller_factory.get_thread_controller(
                session=self.session
            )
        return self._thread_controller
    

    @property
    def message_controller(self) -> controllers.MessageController:
        """
        Returns or initializes Message controller instance. 
        """
        if not self._message_controller: 
            self._message_controller = self.controller_factory.get_message_controller(
                session=self.session
            )
        return self._message_controller
        