"""
User database controller.
"""

from messenger.app.models import User
from messenger.app.repositories import UserRepository
from messenger.core.controllers import BaseController


class UserController(BaseController):
    """
    User database controller.
    """

    def __init__(
        self, repository: UserRepository
    ) -> None:
        super().__init__(model=User, repository=repository)
        