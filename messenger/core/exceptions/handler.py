"""
Base Exception handler.
"""
from starlette.responses import JSONResponse

from .exception import BaseException


class ExceptionHandler:
    @staticmethod
    def handle(
        request, exc: BaseException
    ) -> JSONResponse:
        """
        Handle Exception.
        """
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "error": {
                    "code": exc.error_code,
                    "message": exc.message
                }
            }
        )
    