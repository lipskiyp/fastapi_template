"""
Messages FastAPI router.
"""

from fastapi import APIRouter, Depends, status
from uuid import UUID 

from messenger.app.controllers import MessageController
from messenger.app.dependencies.authentication import get_current_active_user
from messenger.app.exceptions import UnauthorizedException
from messenger.app.factories.controllers import ControllerFactory
from messenger.app.models import User
from messenger.app.schemas import (
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
    controller: MessageController = Depends(ControllerFactory.get_message_controller)
) -> MessageResponseSchema:
    """
    Send a message.
    """
    return await controller.create(
        **request.model_dump(), user_id = current_user.id
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
    message = await controller.get_by({"id": id})
    if message.user_id != current_user.id:
        raise UnauthorizedException
    return await controller.update_by(
        update_by={"id": message.id}, request=request.model_dump()
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
    message = await controller.get_by({"id": id})
    if message.user_id != current_user.id:
        raise UnauthorizedException
    return await controller.soft_delete_by(
        update_by={"id": message.id}
    )
