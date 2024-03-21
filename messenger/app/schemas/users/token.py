"""
Token Pydantic validation schemas. 
"""

from pydantic import BaseModel
from typing import List


class TokenCreateSchema(BaseModel):
    """
    Pydantic schema to create a new token.
    """
    access_token: str
    token_type: str


class TokenData(BaseModel):
    """
    Pydantic schema with Token data.
    """
    username: str
    scopes: List[str]
    