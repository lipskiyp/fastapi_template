from fastapi import APIRouter

from .messages import router as message_router
from .threads import router as thread_router
from .users import router as user_router


api_router = APIRouter()
api_router.include_router(message_router, prefix="/messages")
api_router.include_router(thread_router, prefix="/threads")
api_router.include_router(user_router, prefix="/users")


__all__ = [
    "api_router"
]
