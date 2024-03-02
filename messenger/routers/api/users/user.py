"""
User FastAPI router.
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


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    summary="Create a new user.",
    tags=["users"]
)
async def create_user(
    request: UserCreateSchema, 
    controller: UserController = Depends(
        ControllerFactory.get_user_controller
    )  
) -> UserResponseSchema:
    """
    Creates and returns new users.
    """
    return await controller.create(
        **request.model_dump()
    )


@router.get(
    "/",
    summary="Lists users.",
    tags=["users"]
)
async def list_users(
    filters: Filter = FilterDepends(UserFilter), 
    controller: UserController = Depends(
        ControllerFactory.get_user_controller
    )
) -> List[UserResponseSchema]:
    """
    Returns a list of users.
    """
    return await controller.list_filter(filters=filters)


@router.get(
    "/{id}",
    summary="Returns a user by id.",
    tags=["users"]
)
async def get_user_by_id(
    id: UUID,
    controller: UserController = Depends(
        ControllerFactory.get_user_controller
    )
) -> Optional[UserResponseSchema]:
    """
    Returns user by id.
    """
    return await controller.get_by({"id": id})


@router.patch(
    "/{id}",
    summary="Updates a user by id.",
    tags=["users"]
)
async def update_user_by_id(
    id: UUID,
    request: UserUpdateSchema, 
    controller: UserController = Depends(
        ControllerFactory.get_user_controller
    )
) -> Optional[UserResponseSchema]:
    """
    Updates and returns user by id.
    """
    return await controller.update_by(
        update_by={"id": id}, request=request.model_dump()
    )


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Deletes a user by id.",
    tags=["users"]
)
async def delete_user_by_id(
    id: UUID,
    controller: UserController = Depends(
        ControllerFactory.get_user_controller
    )
) -> None:
    """
    Deletes user by id.
    """
    return await controller.delete_by({"id": id})
