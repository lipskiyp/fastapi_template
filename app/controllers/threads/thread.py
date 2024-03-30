"""
Thread database controller.
"""

from app.models import Thread
from app.repositories import ThreadRepository
from core.controllers import BaseController


class ThreadController(BaseController):
    """
    Thread database controller.
    """

    def __init__(
        self, repository: ThreadRepository
    ) -> None:
        super().__init__(model=Thread, repository=repository)
        