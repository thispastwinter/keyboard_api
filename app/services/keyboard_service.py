from typing import List

from app.services.build_data import BuildData
from app.models.keyboard import Keyboard

keyboards: List[Keyboard] = [
    {
        "id": "kbd001",
        "name": "MechMaster Pro",
        "brand_name": "MechTech",
        "layout": "TKL",
        "color_way": ["Black", "Gunmetal Gray", "RGB"],
        "led": True,
        "hot_swap": False,
        "price": 129.99,
        "num_of_pins": 5,
        "switch": {
            "id": "sw001",
            "name": "Cherry MX Brown",
            "brand_name": "Cherry",
            "bottom_force": "55g",
            "total_travel": "4.0mm",
            "pre_travel": "2.0mm",
            "initial_force": "30g",
            "num_of_pins": 5,
            "led_direction": "north",
            "type": "tactile",
        },
        "keycap": {
            "id": "kc001",
            "name": "Classic DSA",
            "brand_name": "Signature Plastics",
            "material": "PBT",
        },
    },
]


class KeyboardService(BuildData[Keyboard]):
    @classmethod
    def get_all(cls) -> List[Keyboard]:
        return keyboards

    @classmethod
    def get_one(cls, id: str) -> Keyboard:
        return Keyboard(
            id=id,
            brand_name="A Keyboard Brand",
            color_way=["yello", "green"],
            hot_swap=True,
            keycap=None,
            switch=None,
            price=199.99,
            layout="75%",
            led=True,
            name="Awesome Keyboard",
            num_of_pins=5,
        )
