"""
Messages FastAPI router.
"""

from fastapi import APIRouter, Depends, status
from uuid import UUID 

from app.controllers import MessageController
from app.dependencies.authentication import get_current_active_user
from app.exceptions import UnauthorizedException
from app.factories.controllers import ControllerFactory
from app.services.controllers import MessageControllerService
from app.models import User
from app.schemas import (
    MessageSendSchema, MessageResponseSchema, MessageUpdateSchema
)


router = APIRouter()


@router.post(
    "/send",
    status_code=status.HTTP_201_CREATED,
    summary="Send a message.",
    tags=["messages"]
)
async def send_message(
    request: MessageSendSchema,
    current_user: User = Depends(get_current_active_user),
    controller_service: MessageControllerService = Depends(MessageControllerService),
) -> MessageResponseSchema:
    """
    Send a message.
    """
    return await controller_service.send_message(
        user=current_user, request=request.model_dump()
    )


@router.post(
    "/{id}",
    summary="Update a message.",
    tags=["messages"],

)
async def update_message(
    id: UUID, 
    request: MessageUpdateSchema,
    current_user: User = Depends(get_current_active_user),
    controller: MessageController = Depends(ControllerFactory.get_message_controller)
) -> MessageResponseSchema:
    """
    Updates and returns a message.
    """
    return await controller.update_message(
        id=id, user=current_user, request=request.model_dump()
    )


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a message.",
    tags=["messages"],

)
async def delete_message(
    id: UUID, 
    current_user: User = Depends(get_current_active_user),
    controller: MessageController = Depends(ControllerFactory.get_message_controller)
):
    """
    Deletes a message.
    """
    return await controller.delete_message(
        id=id, user=current_user
    )
