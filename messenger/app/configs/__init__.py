from dotenv import load_dotenv

# Load .env variables
load_dotenv(".envs/.production/.messenger")

from .database import database_config
from .messenger import messenger_config


__all__ = [
    "database_config",
    "messenger_config",
]

