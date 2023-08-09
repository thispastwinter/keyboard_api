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
async def get_keyboards():
    try:
        data = await KeyboardService.get_all()

        return APIResponse.create(data=data)

    except Exception as e:
        print(e, flush=True)
        raise HTTPException(status_code=500, detail=str(e))


@keyboards_router.get("/{keyboard_id}", response_model=APIResponse[KeyboardFull])
async def get_keyboard(
    keyboard_id: str = Path(
        title="Keyboard ID", description="The ID of the keyboard to get data for"
    )
):
    try:
        data = await KeyboardService.get_one(id=keyboard_id)

        return APIResponse.create(data=data)

    except Exception as e:
        print(e, flush=True)
        raise HTTPException(status_code=500, detail=str(e))
