"""
Token Pydantic validation schemas. 
"""

from pydantic import BaseModel


class TokenCreateSchema(BaseModel):
    """
    Pydantic schema to create a new token.
    """
    access_token: str
    token_type: str
    