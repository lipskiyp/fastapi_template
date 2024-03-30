"""
Threads SQLAlchemy ORM model.
"""

from sqlalchemy import Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import CommonBase
from ..association_tables import users_and_threads


class Thread(CommonBase):
    """
    Threads ORM model.
    """
    __tablename__ = "threads"

    active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True
    )

    users = relationship(
        "User",
        secondary=users_and_threads,
        back_populates="threads",
        passive_deletes=True,
    )

    __mapper_args__ = {
        'eager_defaults': True,
    }
    