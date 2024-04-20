"""
Cache client.
"""

import json
from functools import wraps
from pydantic import TypeAdapter
from typing import Callable, Optional
import inspect

from configs import cache_config
from .redis import RedisClient


class CacheClient:
    """
    Cache client.
    """

    def __init__(self) -> None:
        """
        Initialise cache client.
        """
        self.client = RedisClient()


    def cached(
        self, expiration: int = cache_config.REDIS_EXPIRATION, adapter: Optional[TypeAdapter] = None
    ):
        """
        Retrieve cache or set new cache. 
        """
        def decorator(func: Callable):
            @wraps(func)
            async def wrapper(*args, **kwargs):
                # Generate cache key
                # await self.client.clear()
                key = self._key(func, *args, **kwargs)

                # Return cache if exists already 
                if await self.client.exists(key):
                    if cache := await self.client.get(key) and adapter:
                        print(cache)
                        return adapter.validate_json(cache)
                    
                    elif cache:
                        return cache
                
                # Call function
                res = await func(*args, **kwargs)

                # Apply Pydantic adapter 
                value = adapter.dump_json(res).decode("utf-8") if adapter else res

                # Set new cache
                await self.client.set(
                    key, value, expiration=expiration
                )

                return res
            return wrapper
        return decorator
    

    def _key(
        self, func: Callable, *args, **kwargs
    ) -> str:
        """
        Generate standardized cache key.
        """
        key = f"{inspect.getmodule(func).__name__}.{func.__name__}"

        for key, value in kwargs.items():
            key += f"{key}:{value}"

        return key
    

Cache = CacheClient()
    