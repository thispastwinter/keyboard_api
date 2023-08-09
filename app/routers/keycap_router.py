from fastapi import APIRouter, Path, HTTPException
from typing import List

from app.models.response import APIResponse
from app.models.keycap import KeyCap
from app.services.keycap_service import KeyCapService


keycaps_router = APIRouter(
    tags=["Keycaps"],
    prefix="/keycaps",
)


@keycaps_router.get("", response_model=APIResponse[List[KeyCap]])
async def get_keycaps():
    try:
        data = await KeyCapService.get_all()

        return APIResponse.create(data=data)

    except Exception as e:
        print(e, flush=True)
        raise HTTPException(status_code=500, detail=str(e))


@keycaps_router.get("/{keycap_id}", response_model=APIResponse[KeyCap])
async def get_keycap(
    keycap_id: str = Path(
        title="KeyCap ID", description="The ID of the KeyCap to get data for"
    )
):
    try:
        data = await KeyCapService.get_one(id=keycap_id)

        return APIResponse.create(data=data)

    except Exception as e:
        print(e, flush=True)
        raise HTTPException(status_code=500, detail=str(e))
