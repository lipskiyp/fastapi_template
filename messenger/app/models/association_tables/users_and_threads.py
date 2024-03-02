"""
Users and Threads association table.
"""

from sqlalchemy import Table, Column, ForeignKey, PrimaryKeyConstraint

from messenger.core.models import Base

users_and_threads = Table(
    "users_and_threads",
    Base.metadata,
    Column("user_id", ForeignKey("users.id", ondelete="CASCADE"), primary_key=True),
    Column("thread_id", ForeignKey("threads.id", ondelete="CASCADE"), primary_key=True),
    PrimaryKeyConstraint('user_id', 'thread_id')  
)
