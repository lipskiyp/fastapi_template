"""
Base database controller.
"""

from fastapi_filter.contrib.sqlalchemy import Filter
from typing import Any, Generic, List, Optional, Type

from messenger.core.models import ModelType
from messenger.core.repositories import BaseRepository


class BaseController(Generic[ModelType]):
    """
    Base SQLAlchemy database controller.
    """

    def __init__(
        self, model: Type[ModelType], repository: BaseRepository
    ) -> None:
        self.model = model
        self.repository = repository


    async def create(
        self, **kwargs
    ) -> ModelType:
        """
        Creates and returns new model object.
        """
        model_obj = self.model(**kwargs)
        return await self.repository.create(
            model_obj=model_obj
        )


    async def get_by(
        self, get_by: dict[str, Any]
    ) -> Optional[ModelType]:
        """
        Get a model object by field(s).
        """
        return await self.repository.get_by(
            get_by=get_by
        )
    

    async def list_by(
        self, get_by: dict[str, Any] = {}, order_by: dict[str, Any] = {}, limit: Optional[int] = None
    ) -> List[ModelType]:
        """
        Get ordered list of model objects by field(s).
        """
        return await self.repository.list_by(
            get_by=get_by, order_by=order_by, limit=limit
        )
    

    async def list_filter(
        self, filters: Filter
    ) -> List[ModelType]:
        """
        Get filtered list of model objects using FastAPI Filter.
        """
        return await self.repository.list_filter(
            filters=filters,
        )
    

    async def update_by(
        self, request: dict[str, Any], update_by: dict[str, Any]
    ) -> Optional[ModelType]:
        """
        Updates and returns model object.
        """
        if model_obj := await self.get_by(get_by=update_by):
            for key, value in request.items():
                if value is not None:
                    setattr(model_obj, key, value)
            return await self.repository.create(model_obj)
        return None
    

    async def delete_by(
        self, delete_by: dict[str, Any]
    ) -> None:
        """
        Deletes model object.
        """
        if model_obj := await self.get_by(get_by=delete_by):
            await self.repository.delete(model_obj)
    