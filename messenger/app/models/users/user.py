"""
User SQLAlchemy ORM model.
"""

from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from messenger.core.authentication import pwd_context
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
    hashed_password: Mapped[str] = mapped_column(
        String,
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

    @property
    def password(self) -> str:
        """
        Returns hashed password
        """
        return self.hashed_password

    @password.setter
    def password(self, password: str) -> str:
        """
        Sets and returns hashed password
        """
        self.hashed_password = pwd_context.hash(password)
        return self.hashed_password
    

    def password_verify(self, password: str) -> bool:
        """
        Verify password.
        """
        return pwd_context.verify(password, self.hashed_password)
