"""
Redis cache client.
"""

from redis.asyncio import Redis
from redis.exceptions import ConnectionError
from typing import Any

from app.exceptions import ServerErrorException
from core.cache import cache_session
from configs import cache_config


REDIS_CONNECTION_ERROR = ServerErrorException(
    message="Could not connect to redis server"
)


class RedisClient:
    """
    Redis cache client.
    """

    @property
    def session(self) -> Redis:
        """
        Returns Redis session.
        """
        return cache_session()


    async def set(
        self, key: str, value: dict[str, Any], expiration: int = cache_config.REDIS_EXPIRATION
    ):
        """
        Write to Redis.
        """
        try:
            return await self.session.set(key, value, ex=expiration)
        
        except ConnectionError:
            raise REDIS_CONNECTION_ERROR


    async def exists(
        self, key: str
    ) -> bool:
        """
        Check if in Redis.
        """
        try:
            return await self.session.exists(key)
        
        except ConnectionError:
            raise REDIS_CONNECTION_ERROR


    async def get(
        self, key: str
    ):
        """
        Read from Redis.
        """
        try:
            return await self.session.get(key)
        
        except ConnectionError:
            raise REDIS_CONNECTION_ERROR


    async def delete(
        self, key: str
    ):
        """
        Delete from Redis.
        """
        try:
            return await self.session.delete(key)
        
        except ConnectionError:
            raise REDIS_CONNECTION_ERROR
        


    async def list_keys(self):
        """
        List all Redis cache keys.
        """
        try:
            return await self.session.keys(pattern="*")
        
        except ConnectionError:
            raise REDIS_CONNECTION_ERROR
        

    async def flush(self):
        """
        Clear Redis database.
        """
        try:
            return await self.session.flushdb()
        
        except ConnectionError:
            raise REDIS_CONNECTION_ERROR
        