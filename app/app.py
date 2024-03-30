"""
Messenger FastAPI app.
"""

from fastapi import FastAPI

import app.exceptions as exceptions
from core.exceptions import ExceptionHandler
from routers.api import api_router
from routers.metadata import metadata


class App:
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
    

app = App().app

"""
from core.models import Base
from core.database import engine

async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@messenger.on_event("startup")
async def on_startup():
    await init_models()
"""
