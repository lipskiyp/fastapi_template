"""
Threads FastAPI router.
"""

from fastapi import APIRouter, Depends, status
from typing import List, Optional
from uuid import UUID 

from messenger.app.controllers import ThreadController
from messenger.app.factories.controllers import ControllerFactory
from messenger.app.schemas import ThreadResponseSchema


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
) -> Optional[ThreadResponseSchema]:
    """
    Returns a Thread by id.
    """
    return await controller.get_by({"id": id})


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Deletes a thread by id.",
    tags=["users"]
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
