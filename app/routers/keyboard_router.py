from fastapi import APIRouter, Path, HTTPException
from typing import List

from app.models.response import APIResponse
from app.models.keyboard import KeyboardFull, KeyboardPartial
from app.services.keyboard_service import KeyboardService


keyboards_router = APIRouter(
    tags=["Keyboards"],
    prefix="/keyboards",
)


@keyboards_router.get("", response_model=APIResponse[List[KeyboardPartial]])
def get_keyboards() -> APIResponse[KeyboardPartial]:
    try:
        data = KeyboardService.get_all()
        print(data)

        return APIResponse.create(data=data)

    except Exception as e:
        print(e, flush=True)
        raise HTTPException(status_code=500, detail=str(e))


@keyboards_router.get("/{keyboard_id}", response_model=APIResponse[KeyboardFull])
def get_keyboard(
    keyboard_id: str = Path(
        title="Keyboard ID", description="The ID of the keyboard to get data for"
    )
) -> APIResponse[KeyboardFull]:
    try:
        data = KeyboardService.get_one(id=keyboard_id)

        return APIResponse.create(data=data)

    except Exception as e:
        print(e, flush=True)
        raise HTTPException(status_code=500, detail=str(e))
