"""
User Pydantic validation schemas. 
"""
from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID 


class UserCreateSchema(BaseModel):
    """
    Pydantic schema to create a new user.
    """
    username: str 
    firstname: str
    secondname: str 
    password: str
    password_confirm: str


class UserAddRemoveThreadsSchema(BaseModel):
    """
    Pydantic schema to add/remove thread to/from a user.
    """
    add: Optional[List[UUID]] = []
    remove: Optional[List[UUID]] = []


class UserResponseSchema(BaseModel):
    """
    Pydantic schema to return a user.
    """
    id: UUID
    username: str 
    firstname: str
    secondname: str 
    active: bool
    scopes_str: str
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
