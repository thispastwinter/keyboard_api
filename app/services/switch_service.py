from app.services.build_data import BuildData
from app.models.switch import Switch
from app.services.database_service import RelatedField, DatabaseService


class SwitchService(BuildData):
    @classmethod
    async def get_all(cls):
        switches_data = await DatabaseService[Switch].get_all(
            "switches", related_fields=[RelatedField(alias="type", name="type")]
        )

        return switches_data

    @classmethod
    async def get_one(cls, id: str):
        switch_data = await DatabaseService[Switch].get_one(
            "switches", id=id, related_fields=[RelatedField(alias="type", name="type")]
        )

        return switch_data
