from fastapi import APIRouter, Path, HTTPException
from typing import List

from app.models.response import APIResponse
from app.models.switch import Switch
from app.services.switch_service import SwitchService


switches_router = APIRouter(
    tags=["Switches"],
    prefix="/switches",
)


@switches_router.get("", response_model=APIResponse[List[Switch]])
async def get_switches():
    try:
        data = SwitchService.get_all()

        return APIResponse.create(data=data)

    except Exception as e:
        print(e, flush=True)
        raise HTTPException(status_code=500, detail=str(e))


@switches_router.get("/{switch_id}", response_model=APIResponse[Switch])
async def get_switch(
    switch_id: str = Path(
        title="Switch ID", description="The ID of the Switch to get data for"
    )
) -> APIResponse[Switch]:
    try:
        data = SwitchService.get_one(id=switch_id)

        return APIResponse.create(data=data)

    except Exception as e:
        print(e, flush=True)
        raise HTTPException(status_code=500, detail=str(e))
