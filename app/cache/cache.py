"""
Redis cache client.
"""

from functools import wraps
from redis.exceptions import ConnectionError
from typing import Any

from core.cache import cache_session
from configs import cache_config


def handle_connection_error():
    """
    Decorator to handle Redis ConnectionError.
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except ConnectionError:
                return None
        return wrapper
    return decorator


class Cache:
    """
    Redis cache client.
    """

    def __init__(self) -> None:
        """
        Initialise Redis cache client.
        """
        self.session = cache_session()
    

    @handle_connection_error
    async def write(
        self, key: str, value: dict[str, Any], expiration: int = cache_config.REDIS_EXPIRATION
    ):
        """
        Write to Redis.
        """
        return await self.session.set(key, value, ex=expiration)


    @handle_connection_error
    async def exists(
        self, key: str
    ) -> bool:
        """
        Check if in Redis.
        """
        return await self.session.exists(key)


    @handle_connection_error
    async def read(
        self, key: str
    ):
        """
        Read from Redis.
        """
        return await self.session.get(key)


    @handle_connection_error
    async def delete(
        self, key: str
    ):
        """
        Delete from Redis.
        """
        return await self.session.delete(key)
    