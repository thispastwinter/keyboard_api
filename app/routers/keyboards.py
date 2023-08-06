from fastapi import APIRouter, Path

keyboards_router = APIRouter(
    tags=["Keyboards"],
    prefix="/keyboards",
)


@keyboards_router.get("")
async def keyboards():
    return {"keyboards": []}


@keyboards_router.get("/{keyboard_id}")
async def keyboard(
    keyboard_id: str = Path(
        title="Keyboard ID", description="The ID of the keyboard to get data for"
    )
):
    return {"keyboard": keyboard_id}
