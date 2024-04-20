"""
Users FastAPI router.
"""

from fastapi import APIRouter, Depends, status, Security
from fastapi_filter import FilterDepends
from fastapi_filter.contrib.sqlalchemy import Filter
from fastapi.security import OAuth2PasswordRequestForm
from typing import List
from uuid import UUID 

from app.controllers import UserController
from app.dependencies.authentication import get_current_active_user
from app.exceptions import UnauthorizedException
from app.factories.controllers import ControllerFactory
from app.filters import UserFilter
from app.services.controllers import UserControllerService
from app.models import User
from app.schemas import (
    UserCreateSchema, UserResponseSchema, UserUpdateSchema, 
    TokenCreateSchema, ThreadResponseSchema, UserAddRemoveThreadsSchema
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
    return await controller.create_user(
        request.model_dump()
    )


@router.post(
    "/token/",
    summary="Authenticate user.",
    tags=["users"]
)
async def authenticate_user(
    request: OAuth2PasswordRequestForm = Depends(),
    controller: UserController = Depends(
        ControllerFactory.get_user_controller
    )  
) -> TokenCreateSchema:
    """
    Authenticates user and returns token.
    """
    return await controller.authenticate_user(
        request=request
    )


@router.get(
    "/me/",
    summary="Get current authenticated user.",
    tags=["users"] 
)
async def get_authenticated_user(
    current_user: User = Depends(get_current_active_user)
) -> UserResponseSchema:
    """
    Returns current authenticated user.
    """
    return current_user


@router.get(
    "/",
    summary="List users.",
    tags=["users"],
    #dependencies=[
    #    # requires authenticated user with users:admins scopes
    #    Security(get_current_active_user, scopes=["users:admin"])   
    #]   
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
    return await controller.list_users_filter(filters, a=1)


@router.get(
    "/{id}",
    summary="Returns a user by id.",
    tags=["users"],
    dependencies=[
        # requires authenticated user with users:admins scopes
        Security(get_current_active_user, scopes=["users:admin"])   
    ]   
)
async def get_user_by_id(
    id: UUID,
    controller: UserController = Depends(
        ControllerFactory.get_user_controller
    )
) -> UserResponseSchema:
    """
    Returns user by id.
    """
    return await controller.get_by({"id": id})


@router.patch(
    "/me/",
    summary="Updates current authenticated user.",
    tags=["users"] 
)
async def update_authenticated_user(
    request: UserUpdateSchema, 
    current_user: User = Depends(get_current_active_user),
    controller: UserController = Depends(
        ControllerFactory.get_user_controller
    )
) -> UserResponseSchema:
    """
    Updates and returns current authenticated user.
    """
    return await controller.update_by(
        update_by={"id": current_user.id}, request=request.model_dump()
    )


@router.patch(
    "/{id}",
    summary="Updates a user by id.",
    tags=["users"],
    dependencies=[
        # requires authenticated user with users:admins scopes
        Security(get_current_active_user, scopes=["users:admin"])   
    ]   
)
async def update_user_by_id(
    id: UUID,
    request: UserUpdateSchema, 
    controller: UserController = Depends(
        ControllerFactory.get_user_controller
    )
) -> UserResponseSchema:
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
    tags=["users"],
    dependencies=[
        # requires authenticated user with users:admins scopes
        Security(get_current_active_user, scopes=["users:admin"]) 
    ]   
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
    return await controller.soft_delete_by({"id": id})


@router.get(
    "/me/threads/",
    summary="Get all user's threads.",
    tags=["users"],
)
async def get_users_in_thread(
    current_user: User = Depends(get_current_active_user),
    controller: UserController = Depends(
        ControllerFactory.get_user_controller
    )
) -> List[ThreadResponseSchema]:
    """
    Returns all user's threads.
    """
    user = await controller.get_by({"id": current_user.id})
    return await user.awaitable_attrs.threads


@router.patch(
    "/me/threads/",
    summary="Add or remove threads to/from a user.",
    tags=["users"],
)
async def add_or_remove_threads_from_user(
    request: UserAddRemoveThreadsSchema,
    current_user: User = Depends(get_current_active_user),
    controller_service: UserControllerService = Depends(UserControllerService)
) -> List[ThreadResponseSchema]:
    """
    Adds or removes threads to/from a user.
    """
    return await controller_service.add_or_remove_threads_from_user(
        user_id=current_user.id, threads_add=request.add, threads_remove=request.remove
    )
