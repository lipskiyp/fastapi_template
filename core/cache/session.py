"""
Redis cache session.
"""

from redis.asyncio import Redis

from .connection_pool import connection_pool


def cache_session() -> Redis:
    """
    Returns Redis instance.
    """
    return Redis(connection_pool=connection_pool)
