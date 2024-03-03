"""
Threads Pydantic validation schemas. 
"""
from datetime import datetime
from pydantic import BaseModel
from uuid import UUID 


class ThreadResponseSchema(BaseModel):
    """
    Pydantic schema to return a threads.
    """
    id: UUID
    active: bool
    created_at: datetime
    updated_at: datetime
