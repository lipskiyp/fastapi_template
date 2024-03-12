"""
Message Pydantic validation schemas. 
"""
from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from uuid import UUID 


class MessageSendSchema(BaseModel):
    """
    Pydantic schema to send a message.
    """
    thread_id: UUID  
    message: str


class MessageResponseSchema(BaseModel):
    """
    Pydantic schema to receive a message.
    """
    thread_id: UUID 
    user_id: UUID 
    message: str
    created_at: datetime
    updated_at: datetime


class MessageUpdateSchema(BaseModel):
    """
    Pydantic schema to update a message.
    """
    message: Optional[str] = None
