"""
User SQLAlchemy ORM model.
"""

from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from messenger.core.models import CommonBase
from ..association_tables import users_and_threads


class User(CommonBase):
    """
    Users ORM model.
    """
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(
        String(64),
        unique=True,
        nullable=False,
        index=True
    )
    firstname: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
    )
    secondname: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
    )
    active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True
    )

    threads = relationship(
        "Thread",
        secondary=users_and_threads,
        back_populates="users",
        passive_deletes=True,
    )

    __mapper_args__ = {
        'eager_defaults': True,
    }
