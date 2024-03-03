"""
Messages FastAPI router.
"""

from fastapi import APIRouter, Depends, status
from fastapi_filter import FilterDepends
from fastapi_filter.contrib.sqlalchemy import Filter
from typing import List, Optional
from uuid import UUID 

from messenger.app.controllers import UserController
from messenger.app.factories.controllers import ControllerFactory
from messenger.app.filters import UserFilter
from messenger.app.schemas import (
    UserCreateSchema, UserResponseSchema, UserUpdateSchema
)


router = APIRouter()