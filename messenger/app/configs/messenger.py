"""
Base configuration settings for messenger.
"""

from os import environ
from pydantic_settings import BaseSettings


class MessengerConfig(BaseSettings):
    """
    Messenger configuration settings. 
    """
    APP_HOST: str = environ.get("APP_HOST")
    APP_PORT: int = int(environ.get("APP_PORT"))


messenger_config = MessengerConfig()
