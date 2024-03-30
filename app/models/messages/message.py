"""
Messages SQLAlchemy ORM model.
"""

from sqlalchemy import Boolean, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import UUID as uuid

from core.models import CommonBase


class Message(CommonBase):
    """
    Messages ORM model.
    """
    __tablename__ = "messages"

    message: Mapped[str] = mapped_column(
        String(254),
        nullable=False
    )
    user_id: Mapped[uuid] = mapped_column(
        UUID,
        ForeignKey("users.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    thread_id: Mapped[uuid] = mapped_column(
        UUID,
        ForeignKey("threads.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )

    sender: Mapped["User"] = relationship(
        backref="messages",
        foreign_keys=[user_id],
        init=False,
    )
    thread: Mapped["Thread"] = relationship(
        backref="messages",
        foreign_keys=[thread_id],
        init=False,
    )

    __mapper_args__ = {
        'eager_defaults': True,
    }