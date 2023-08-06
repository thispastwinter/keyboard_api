from pydantic.generics import GenericModel
from pydantic import BaseModel
from typing import Generic, TypeVar
from datetime import datetime

ISO_8601 = "YYYY-MM-DDTHH:MM:SS.mmmmmm"

T = TypeVar("T")


class Meta(BaseModel):
    date: str
    status_code: int
    message: str | None


class APIResponse(GenericModel, Generic[T]):
    data: T
    meta: Meta

    @classmethod
    def create(
        cls,
        data: T,
        status_code: str | None = None,
        date: str | None = None,
        message: str | None = None,
    ):
        meta_status_code = None
        meta_date = None

        if status_code is not None:
            meta_status_code = status_code
        else:
            meta_status_code = 200

        if date is not None:
            meta_date = date
        else:
            meta_date = datetime.now().strftime(ISO_8601)

        return cls(
            data=data,
            status_code=meta_status_code,
            date=meta_date,
            message=message,
        )
