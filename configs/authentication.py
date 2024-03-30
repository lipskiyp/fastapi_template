"""
Base configuration settings for authentication.
"""

from os import environ
from pydantic_settings import BaseSettings


class AuthenticationConfig(BaseSettings):
    """
    Authentication configuration settings. 
    """

    AUTH_KEY: str = environ.get("AUTH_KEY")  # openssl rand -hex 32
    AUTH_ALGORITHM: str = environ.get("AUTH_ALGORITHM")
    AUTH_TOKEN_PATH: str = environ.get("AUTH_TOKEN_PATH")
    AUTH_EXPIRE: int = int(environ.get("AUTH_EXPIRE")) 


authentication_config = AuthenticationConfig()
