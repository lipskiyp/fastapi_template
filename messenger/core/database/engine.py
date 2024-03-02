"""
Database engine.
"""

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine

from messenger.app.configs import database_config


meta = MetaData()


engine = create_async_engine(database_config.database_url)  
