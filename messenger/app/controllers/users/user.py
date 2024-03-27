"""
User database controller.
"""

from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any

from messenger.app.authentication import create_token
from messenger.app.configs import authentication_config
from messenger.app.exceptions import UnauthorizedException
from messenger.app.models import User
from messenger.app.repositories import UserRepository
from messenger.app.schemas import TokenCreateSchema
from messenger.core.controllers import BaseController


class UserController(BaseController):
    """
    User database controller.
    """

    def __init__(
        self, repository: UserRepository
    ) -> None:
        super().__init__(model=User, repository=repository)


    async def create_user(
        self, request: dict[str, Any]
    ) -> User:
        """
        Creates and returns new User.
        """
        password, password_confirm = request.pop("password"), request.pop("password_confirm")
        if password != password_confirm:
            raise UnauthorizedException(custom_message="Invalid password.")
        
        model_obj = self.model(**request, hashed_password="")
        model_obj.password = password

        return await self.repository.create(model_obj=model_obj)
    

    async def authenticate_user(
        self, request: OAuth2PasswordRequestForm
    ) -> TokenCreateSchema:
        """
        Authenticates user and returns Token.
        """
        user = await self.get_by({"username": request.username})
        if user.password_verify(password=request.password):
            return await self.get_access_token(user=user)
        raise UnauthorizedException(custom_message="Incorrect username or password.")
    

    async def get_access_token(
        self, user: User
    ) -> TokenCreateSchema:
        """
        Creates and returns Token.
        """
        token = create_token(
            data={
                "sub": user.username,
                "scopes": user.scopes
            },
            expires_delta=timedelta(
                minutes=authentication_config.AUTH_EXPIRE
            )
        )
        return TokenCreateSchema(**{"access_token": token, "token_type": "bearer"})
    