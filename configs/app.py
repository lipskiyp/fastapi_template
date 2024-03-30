"""
Base configuration settings for app.
"""

from os import environ
from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    """
    App configuration settings. 
    """
    APP_HOST: str = environ.get("APP_HOST")
    APP_PORT: int = int(environ.get("APP_PORT"))


app_config = AppConfig()
