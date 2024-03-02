"""
Base configuration settings for database.
"""

from os import environ
from pydantic_settings import BaseSettings


class DatabaseConfig(BaseSettings):
    """
    Database configuration settings. 
    """
    POSTGRESQL_DB: str = environ.get("POSTGRESQL_DB")
    POSTGRESQL_HOST: str = environ.get("POSTGRESQL_HOST")
    POSTGRESQL_PORT: int = int(environ.get("POSTGRESQL_PORT"))
    POSTGRESQL_USER: str = environ.get("POSTGRESQL_USER")
    POSTGRESQL_PASSWORD: str = environ.get("POSTGRESQL_PASSWORD")

    @property
    def database_url(self) -> str:
        """
        Database connection url.
        """
        return f"postgresql+asyncpg://{self.POSTGRESQL_USER}:{self.POSTGRESQL_PASSWORD}@{self.POSTGRESQL_HOST}:{self.POSTGRESQL_PORT}/{self.POSTGRESQL_DB}"


database_config = DatabaseConfig()
