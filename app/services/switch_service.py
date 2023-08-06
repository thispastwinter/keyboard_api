from typing import List

from app.services.build_data import BuildData
from app.models.switch import Switch


switches: List[Switch] = [
    {
        "id": "1",
        "name": "Blue Switch",
        "brand_name": "ABC Switches",
        "bottom_force": "50g",
        "total_travel": "4.0mm",
        "pre_travel": "2.0mm",
        "initial_force": "60g",
        "num_of_pins": 3,
        "led_direction": "north",
        "type": "clicky",
    },
    {
        "id": "2",
        "name": "Brown Switch",
        "brand_name": "DEF Switches",
        "bottom_force": "45g",
        "total_travel": "3.5mm",
        "pre_travel": "2.0mm",
        "initial_force": "55g",
        "num_of_pins": 5,
        "led_direction": "south",
        "type": "tactile",
    },
    {
        "id": "3",
        "name": "Red Switch",
        "brand_name": "XYZ Switches",
        "bottom_force": "40g",
        "total_travel": "3.0mm",
        "pre_travel": "2.0mm",
        "initial_force": "50g",
        "num_of_pins": 3,
        "led_direction": "north",
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
            bottom_force="40g",
            total_travel="3.0mm",
            pre_travel="2.0mm",
            initial_force="50g",
            num_of_pins=3,
            led_direction="north",
            type="linear",
        )
