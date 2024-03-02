"""
User FastAPI filters.
"""

from typing import Optional
from fastapi_filter.contrib.sqlalchemy import Filter

from messenger.app.models import User


class UserFilter(Filter):
    """
    User FastAPI filters.
    """
    active: Optional[bool] = None
    order_by: Optional[list[str]] = ["username"]

    class Constants(Filter.Constants):
        model = User
