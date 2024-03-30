from fastapi import APIRouter

from .thread import router as thread_router 


router = APIRouter()
router.include_router(thread_router, prefix="")


__all__ = [
    "router"
]
