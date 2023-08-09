from app.services.build_data import BuildData
from app.models.keycap import KeyCap
from app.services.database_service import DatabaseService


class KeyCapService(BuildData):
    @classmethod
    async def get_all(cls):
        keycaps_data = await DatabaseService[KeyCap].get_all("keycaps")

        return keycaps_data

    @classmethod
    async def get_one(cls, id: str):
        keycap_data = await DatabaseService[KeyCap].get_one("keycaps", id=id)

        return keycap_data
