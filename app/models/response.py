from pydantic import BaseModel
from typing import Generic
from typing_extensions import TypeVar, Self
from datetime import datetime

T = TypeVar("T")


class Meta(BaseModel):
    date: str
    status_code: int
    message: str | None


class APIResponse(BaseModel, Generic[T]):
    data: T
    meta: Meta

    @classmethod
    def create(
        cls,
        data: T,
        status_code: int | None = None,
        date: str | None = None,
        message: str | None = None,
    ) -> Self:
        meta_status_code = None
        meta_date = None

        if status_code is not None:
            meta_status_code = status_code
        else:
            meta_status_code = 200

        if date is not None:
            meta_date = date
        else:
            meta_date = datetime.now().isoformat()

        return cls(
            data=data,
            meta=Meta(
                status_code=meta_status_code,
                date=meta_date,
                message=message,
            ),
        )
