from typing import List

from app.services.build_data import BuildData
from app.models.switch import Switch


switches: List[Switch] = [
    {
        "id": "1",
        "name": "Blue Switch",
        "brand_name": "ABC Switches",
        "total_travel": "4.0mm",
        "pre_travel": "2.0mm",
        "num_of_pins": 3,
        "type": "clicky",
    },
    {
        "id": "2",
        "name": "Brown Switch",
        "brand_name": "DEF Switches",
        "total_travel": "3.5mm",
        "pre_travel": "2.0mm",
        "num_of_pins": 5,
        "type": "tactile",
    },
    {
        "id": "3",
        "name": "Red Switch",
        "brand_name": "XYZ Switches",
        "total_travel": "3.0mm",
        "pre_travel": "2.0mm",
        "num_of_pins": 3,
        "type": "linear",
    },
]


class SwitchService(BuildData[Switch]):
    @classmethod
    def get_all(cls) -> List[Switch]:
        return switches

    @classmethod
    def get_one(cls, id: str) -> Switch:
        return Switch(
            id=id,
            name="Red Switch",
            brand_name="XYZ Switches",
            total_travel="3.0mm",
            pre_travel="2.0mm",
            num_of_pins=3,
            type="linear",
        )
