"""
Redis cache configuration settings.
"""

from os import environ
from pydantic_settings import BaseSettings


class CacheConfig(BaseSettings):
    """
    Redis cache configuration settings.
    """

    REDIS_HOST: str = environ.get("REDIS_HOST")
    REDIS_PORT: int = int(environ.get("REDIS_PORT"))
    REDIS_EXPIRATION: int = int(environ.get("REDIS_EXPIRATION"))  # seconds

    @property
    def cache_url(self) -> str:
        """
        Redis cache connection url.
        """
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}"


cache_config = CacheConfig()
