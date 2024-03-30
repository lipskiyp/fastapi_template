"""
Threads Pydantic validation schemas. 
"""
from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID 


class ThreadResponseSchema(BaseModel):
    """
    Pydantic schema to return a threads.
    """
    id: UUID
    active: bool
    created_at: datetime
    updated_at: datetime


class ThreadAddRemoveUsersSchema(BaseModel):
    """
    Pydantic schema to add/remove users to/from a thread.
    """
    add: Optional[List[UUID]] = []
    remove: Optional[List[UUID]] = []
    