from typing import List

from app.services.build_data import BuildData
from app.models.keycap import KeyCap

keycaps: List[KeyCap] = [
    {
        "id": "1",
        "name": "Classic Black",
        "brand_name": "XYZ Keyboards",
        "material": "ABS plastic",
    },
    {
        "id": "2",
        "name": "Retro Beige",
        "brand_name": "ABC Keyboards",
        "material": "PBT plastic",
    },
    {
        "id": "3",
        "name": "Colorful Rainbow",
        "brand_name": "DEF Keyboards",
        "material": "Double-shot PBT plastic",
    },
]


class KeyCapService(BuildData[KeyCap]):
    @classmethod
    def get_all(cls) -> List[KeyCap]:
        return keycaps

    @classmethod
    def get_one(cls, id: str) -> KeyCap:
        return KeyCap(
            id=id,
            name="Classic Black",
            brand_name="XYZ Keyboards",
            material="ABS plastic",
        )
