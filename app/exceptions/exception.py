"""
Custom Exceptions.
"""

from http import HTTPStatus

from core.exceptions import BaseException


class BadRequestException(BaseException):
    error_code = HTTPStatus.BAD_REQUEST
    status_code = HTTPStatus.BAD_REQUEST
    message = HTTPStatus.BAD_REQUEST.description


class NotFoundException(BaseException):
    error_code = HTTPStatus.NOT_FOUND
    status_code = HTTPStatus.NOT_FOUND
    message = HTTPStatus.NOT_FOUND.description


class ServerErrorException(BaseException):
    error_code = HTTPStatus.INTERNAL_SERVER_ERROR
    status_code = HTTPStatus.INTERNAL_SERVER_ERROR
    message = HTTPStatus.INTERNAL_SERVER_ERROR.description


class UnprocessableEntityException(BaseException):
    error_code = HTTPStatus.UNPROCESSABLE_ENTITY
    status_code = HTTPStatus.UNPROCESSABLE_ENTITY
    message = HTTPStatus.UNPROCESSABLE_ENTITY.description


class UnauthorizedException(BaseException):
    error_code = HTTPStatus.UNAUTHORIZED
    status_code = HTTPStatus.UNAUTHORIZED
    message = HTTPStatus.UNAUTHORIZED.description
    headers={"WWW-Authenticate": "Bearer"}
