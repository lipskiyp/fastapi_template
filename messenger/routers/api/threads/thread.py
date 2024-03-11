"""
Threads FastAPI router.
"""

from fastapi import APIRouter, Depends, status
from typing import List
from uuid import UUID 

from messenger.app.controllers import ThreadController
from messenger.app.factories.controllers import ControllerFactory
from messenger.app.services.controllers import ThreadControllerService
from messenger.app.schemas import (
    ThreadResponseSchema, ThreadAddRemoveUsersSchema, UserResponseSchema
)


router = APIRouter()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    summary="Create a new thread.",
    tags=["threads"]   
)
async def create_thread(
    controller: ThreadController = Depends(
        ControllerFactory.get_thread_controller
    )
) -> ThreadResponseSchema:
    """
    Creates and returns a new Thread.
    """
    return await controller.create()


@router.get(
    "/",
    summary="List threads.",
    tags=["threads"]   
)
async def list_threads(
    controller: ThreadController = Depends(
        ControllerFactory.get_thread_controller
    )
) -> List[ThreadResponseSchema]:
    """
    Creates and returns a new Thread.
    """
    return await controller.list_by()


@router.get(
    "/{id}",
    summary="Get a thread by id.",
    tags=["threads"]   
)
async def get_thread_by_id(
    id: UUID,
    controller: ThreadController = Depends(
        ControllerFactory.get_thread_controller
    )
) -> ThreadResponseSchema:
    """
    Returns a Thread by id.
    """
    return await controller.get_by({"id": id})


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Deletes a thread by id.",
    tags=["threads"]
)
async def delete_thread_by_id(
    id: UUID,
    controller: ThreadController = Depends(
        ControllerFactory.get_thread_controller
    )
) -> None:
    """
    Deletes thread by id.
    """
    return await controller.delete_by({"id": id})


@router.get(
    "/{id}/users/",
    summary="Get all users in a thread.",
    tags=["threads"]
)
async def get_users_in_thread(
    id: UUID,
    controller: ThreadController = Depends(
        ControllerFactory.get_thread_controller
    )
) -> List[UserResponseSchema]:
    """
    Returns all users in a thread.
    """
    thread = await controller.get_by({"id": id})
    return await thread.awaitable_attrs.users


@router.patch(
    "/{id}/users/",
    summary="Add or remove users to/from a thread.",
    tags=["threads"]
)
async def add_or_remove_users_from_thread(
    id: UUID,
    request: ThreadAddRemoveUsersSchema,
    controller_service: ThreadControllerService = Depends(ThreadControllerService)
) -> List[UserResponseSchema]:
    """
    Adds or removes users to/from a tread.
    """
    return await controller_service.add_or_remove_users_from_thread(
        thread_id=id, users_add=request.add, users_remove=request.remove
    )