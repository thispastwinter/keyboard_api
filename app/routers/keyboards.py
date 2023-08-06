from fastapi import APIRouter, Path, HTTPException
from typing import List

from app.models.response import APIResponse
from app.models.keyboard import Keyboard


keyboards_router = APIRouter(
    tags=["Keyboards"],
    prefix="/keyboards",
)


@keyboards_router.get("", response_model=APIResponse[List[Keyboard]])
async def keyboards():
    try:
        return APIResponse.create(data=[])
    
    except Exception as e:
        print(e, flush=True)
        raise HTTPException(status_code=500, detail=str(e))


@keyboards_router.get("/{keyboard_id}", response_model=APIResponse[Keyboard])
async def keyboard(
    keyboard_id: str = Path(
        title="Keyboard ID", description="The ID of the keyboard to get data for"
    )
):
    try:
        return APIResponse.create(data=keyboard_id)

    except Exception as e:
        print(e, flush=True)
        raise HTTPException(status_code=500, detail=str(e))
