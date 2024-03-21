"""
Access Token.
"""

from datetime import datetime, timedelta
from jose import jwt
from typing import Any

from messenger.app.configs import authentication_config


def create_token(
    data: dict[str, Any],
    expires_delta: timedelta
) -> str:
    """
    Returns new access Token.
    """
    _data = data.copy()

    _data.update(
        {"exp": datetime.utcnow() + expires_delta}
    )

    return jwt.encode(
        _data, authentication_config.AUTH_KEY, algorithm=authentication_config.AUTH_ALGORITHM
    )
