from pydantic import BaseModel
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Callable

T = TypeVar("T")

class BuildData(BaseModel, Generic[T], ABC):
    @abstractmethod
    def get_all(cls) -> List[T]:
        pass

    @abstractmethod
    def get_one(cls, id: str) -> T:
        pass