from pydantic import BaseModel
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List

T = TypeVar("T")


class BuildData(BaseModel, Generic[T], ABC):
    @abstractmethod
    async def get_all(cls) -> List[T]:
        pass

    @abstractmethod
    async def get_one(cls, id: str) -> T:
        pass
