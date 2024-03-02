"""
User Pydantic validation schemas. 
"""
from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from uuid import UUID 


class UserCreateSchema(BaseModel):
    """
    Pydantic schema to create a new user.
    """
    username: str 
    firstname: str
    secondname: str 


class UserResponseSchema(BaseModel):
    """
    Pydantic schema to return a user.
    """
    id: UUID
    username: str 
    firstname: str
    secondname: str 
    active: bool
    created_at: datetime
    updated_at: datetime


class UserUpdateSchema(BaseModel):
    """
    Pydantic schema to update a user.
    """
    username: Optional[str] = None
    firstname: Optional[str] = None
    secondname: Optional[str] = None 
    active: Optional[bool] = None 
