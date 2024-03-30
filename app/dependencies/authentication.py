"""
User authentication FastAPI dependency injections.
"""

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from jose import JWTError, jwt

from configs import authentication_config
from app.controllers import UserController
from app.exceptions import UnauthorizedException
from app.factories.controllers import ControllerFactory
from app.models import User
from app.schemas import TokenData


INVALID_CREDENTIALS = UnauthorizedException(message="Invalid credentials")


USER_SCOPES = {
    "users:regular": "Regular user scopes.",
    "users:admin": "Admin user scopes.",
    "users:super": "Super user scopes.",
}


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=authentication_config.AUTH_TOKEN_PATH,
    scopes=USER_SCOPES
)


def check_user_scopes(
    scopes, user_scopes
) -> None:
    """
    Check if user has all of the required scopes.
    """
    # Full access to superuser
    if "users:super" in user_scopes:
        return 
    
    for scope in scopes:
        if scope not in user_scopes:
            raise INVALID_CREDENTIALS


def validate_token(
    security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)
) -> TokenData:
    """
    Validates token, checks user scopes (if any security_scopes.scopes provided) and returns username if successful.
    """
    try:
        payload = jwt.decode(
            token, authentication_config.AUTH_KEY, algorithms=[authentication_config.AUTH_ALGORITHM]
        )

        if username := payload.get("sub"):
            token_data = TokenData.model_validate({
                "username": username,
                "scopes": payload.get("scopes", [])
            })

            # Check user scopes against provided scopes
            check_user_scopes(
                scopes=security_scopes.scopes, user_scopes=token_data.scopes
            )
                
            return token_data

        raise INVALID_CREDENTIALS

    except JWTError:
        raise INVALID_CREDENTIALS
    

async def get_current_user(
    token_data: TokenData = Depends(validate_token),
    controller: UserController = Depends(ControllerFactory().get_user_controller),
) -> User:
    """
    Validates token and returns current User.
    """
    if user := await controller.get_by({"username": token_data.username}):
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
