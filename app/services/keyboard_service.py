from app.services.build_data import BuildData
from app.models.keyboard import KeyboardFull, KeyboardPartial
from app.services.database_service import RelatedField, DatabaseService


class KeyboardService(BuildData):
    @classmethod
    async def get_all(cls):
        keyboards_data = await DatabaseService[KeyboardPartial].get_all("keyboards")

        return keyboards_data

    @classmethod
    async def get_one(cls, id: str):
        keyboard_data = await DatabaseService[KeyboardFull].get_one(
            "keyboards",
            id=id,
            fields=[
                "id",
                "name",
                "brand_name",
                "color_way",
                "led",
                "hot_swap",
                "price",
                "num_of_pins",
                "led_direction",
            ],
            related_fields=[
                RelatedField(name="layout_id", alias="layout"),
                RelatedField(
                    name="switch_id",
                    alias="switch",
                    related_fields=[RelatedField(alias="type", name="type")],
                ),
                RelatedField(name="keycap_id", alias="keycap"),
            ],
        )
        print(keyboard_data)

        return keyboard_data
