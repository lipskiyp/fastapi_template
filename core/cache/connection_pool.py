"""
Redis cache connection pool.
"""

from redis.asyncio import ConnectionPool

from configs import cache_config


connection_pool = ConnectionPool.from_url(
    cache_config.cache_url
)
