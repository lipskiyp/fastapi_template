"""
User authentication FastAPI dependency injections.
"""

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from messenger.app.configs import authentication_config
from messenger.app.controllers import UserController
from messenger.app.exceptions import UnauthorizedException
from messenger.app.factories.controllers import ControllerFactory
from messenger.app.models import User


oauth2_scheme = OAuth2PasswordBearer(tokenUrl=authentication_config.AUTH_TOKEN_PATH)


INVALID_CREDENTIALS = UnauthorizedException(message="Invalid credentials")


def validate_token(
    token: str = Depends(oauth2_scheme)
) -> str:
    """
    Validates token and returns username if successful.
    """
    try:
        payload = jwt.decode(
            token, authentication_config.AUTH_KEY, algorithms=[authentication_config.AUTH_ALGORITHM]
        )
        username: str = payload.get("sub")
        if username:
            return username
        raise INVALID_CREDENTIALS

    except JWTError:
        raise INVALID_CREDENTIALS
    

async def get_current_user(
    username: str = Depends(validate_token),
    controller: UserController = Depends(ControllerFactory().get_user_controller),
) -> User:
    """
    Validates token and returns current User.
    """
    if user := await controller.get_by({"username": username}):
        return user
    raise INVALID_CREDENTIALS


async def get_current_active_user(
    current_user: User = Depends(get_current_user)
) -> User:
    """
    Validates token and returns current User if active.
    """
    if current_user.active:
        return current_user
    raise UnauthorizedException(message="User is not active.")
