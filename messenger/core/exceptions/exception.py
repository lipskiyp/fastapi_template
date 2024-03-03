"""
Base Exception.
"""

from typing import Optional


class BaseException(Exception):
    def __init__(self, message: Optional[str] = None):
        if message: self.message = message
