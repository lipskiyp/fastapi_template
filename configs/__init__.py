from dotenv import load_dotenv

# Load .env variables
load_dotenv(".envs/.app")

from .authentication import authentication_config
from .cache import cache_config
from .database import database_config
from .app import app_config


__all__ = [
    "authentication_config",
    "cache_config",
    "database_config",
    "app_config",
]

