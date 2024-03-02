"""
Threads SQLAlchemy ORM model.
"""

from sqlalchemy.orm import relationship

from messenger.core.models import CommonBase
from ..association_tables import users_and_threads


class Thread(CommonBase):
    """
    Threads ORM model.
    """
    __tablename__ = "threads"

    users = relationship(
        "User",
        secondary=users_and_threads,
        back_populates="threads",
        passive_deletes=True,
    )

    __mapper_args__ = {
        'eager_defaults': True,
    }