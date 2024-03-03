"""
Message database controller.
"""

from messenger.app.models import Message
from messenger.app.repositories import MessageRepository
from messenger.core.controllers import BaseController


class MessageController(BaseController):
    """
    Message database controller.
    """

    def __init__(
        self, repository: MessageRepository
    ) -> None:
        super().__init__(model=Message, repository=repository)
        