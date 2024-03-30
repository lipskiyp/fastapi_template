"""
Base model type.
"""

from typing import TypeVar

from .base import Base


ModelType = TypeVar("ModelType", bound=Base)
