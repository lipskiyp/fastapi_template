"""
Base SQLAlchemy database repository.
"""

from fastapi_filter.contrib.sqlalchemy import Filter
from sqlalchemy import Select, ScalarResult, Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import select
from typing import Any, Generic, List, Optional, Type

from messenger.core.models import ModelType


class BaseRepository(Generic[ModelType]):
    """
    Base SQLAlchemy database repository. 
    """
    def __init__(
        self, model: Type[ModelType], session: AsyncSession,
    ) -> None:
        self.model = model
        self.session = session


    async def get_by(
        self, get_by: dict[str, Any]
    ) -> ModelType:
        """
        Get a model object by field(s).
        """
        query = self._query(get_by=get_by)
        res = await self._scalars(query)
        return res.one_or_none()
    

    async def list_by(
        self, get_by: dict[str, str] = {}, order_by: dict[str, Any] = {}, limit: Optional[int] = None
    ) -> List[ModelType]:
        """
        Get ordered list of model objects by field(s).
        """
        query = self._query(get_by=get_by, order_by=order_by)
        if limit: query = query.limit(limit)
        res = await self._scalars(query)
        return res.all()
    

    async def list_filter(
        self, filters: Filter
    ) -> List[ModelType]:
        """
        Get filtered list of model objects using FastAPI Filter.
        """
        query = self._query()
        query = filters.filter(query)
        res = await self._scalars(query)
        return res.all()
    

    async def create(
        self, model_obj: ModelType
    ) -> ModelType:
        """
        Creates and returns new model object.
        """
        self.session.add(model_obj)
        await self.session.flush()
        return model_obj
    

    async def delete(
        self, model_obj: ModelType
    ) -> None:
        """
        Deletes model object.
        """
        await self.session.delete(model_obj)
        await self.session.flush()


    def _query(
        self, get_by: dict[str, Any] = {}, order_by: dict[str, Any] = {}
    ) -> Select:
        """
        Returns a base query with optional order by filter and join.
        """
        query = select(self.model)
        query = self._filter_by(query, get_by)
        query = self._order_by(query, order_by)
        return query


    def _filter_by(
        self, query: Select, filter_by: dict[str, Any] = {}
    ) -> Select:
        """
        Returns a filtered query.
        """
        return query.filter_by(**filter_by)


    def _order_by(
        self, query: Select, order_by: dict[str, Any] = {}
    ) -> Select:
        """
        Returns an ordered query.
        """
        for field, order in order_by.items():
            if order == "asc":
                query = query.order_by(
                    getattr(self.model, field).asc()
                 )
            elif order == "desc":
                query = query.order_by(
                    getattr(self.model, field).desc()
                 )
            else:
                query = query.order_by(
                    getattr(self.model, field)
                )       
        return query
    

    async def execute_all(
        self, query: Select
    ) -> List[ModelType]:
        """
        Executes query and returns .all() database object.
        """
        res = await self._execute(query)
        return res.all() 
    

    async def execute_scalars(
        self, query: Select
    ) -> List[ScalarResult]:
        """
        Executes query and returns .scalars() database object.
        """
        res = await self._execute(query)
        return res.scalars() 
    

    async def _execute(
        self, query: Select
    ) -> Result:
        """
        Executes query.
        """
        return await self.session.execute(query)


    async def _scalars(
        self, query: Select
    ) -> ScalarResult:
        """
        Executes and returns query.
        """
        return await self.session.scalars(query)
