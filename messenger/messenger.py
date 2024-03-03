"""
Messenger FastAPI app.
"""

from fastapi import FastAPI

import messenger.app.exceptions as exceptions
from messenger.core.exceptions import ExceptionHandler
from messenger.routers.api import api_router
from messenger.routers.metadata import metadata


class Messenger:
    """
    Messenger FastAPI app.
    """
    
    def __init__(self) -> None:
        self._app = FastAPI(
            openapi_tags=metadata,
        )
        self.init_routers()
        self.init_exception_handlers()


    def init_routers(self):
        self._app.include_router(api_router, prefix="/api")


    def init_exception_handlers(self):
        self.app.add_exception_handler(
            exceptions.BadRequestException, ExceptionHandler.handle
        )
        self.app.add_exception_handler(
            exceptions.NotFoundException, ExceptionHandler.handle
        )
        self.app.add_exception_handler(
            exceptions.ServerErrorException, ExceptionHandler.handle
        )
        self.app.add_exception_handler(
            exceptions.UnprocessableEntityException, ExceptionHandler.handle
        )
        self.app.add_exception_handler(
            exceptions.UnauthorizedException, ExceptionHandler.handle
        )


    @property
    def app(self) -> FastAPI:
        return self._app
    

messenger = Messenger().app


from messenger.core.models import Base
from messenger.core.database import engine

async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@messenger.on_event("startup")
async def on_startup():
    await init_models()
