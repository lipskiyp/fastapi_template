"""
Thread database controller.
"""

from messenger.app.models import Thread
from messenger.app.repositories import ThreadRepository
from messenger.core.controllers import BaseController


class ThreadController(BaseController):
    """
    Thread database controller.
    """

    def __init__(
        self, repository: ThreadRepository
    ) -> None:
        super().__init__(model=Thread, repository=repository)
        