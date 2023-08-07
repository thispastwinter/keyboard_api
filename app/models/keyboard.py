from typing_extensions import Literal, TypedDict
from typing import List
from app.models.switch import Switch
from app.models.keycap import KeyCap

KeyboardLayout = Literal[
    "TKL",
    "75%",
    "60%",
    "40%",
    "Split",
    "Ortholinear",
    "ErgoDox",
    "HHKB",
    "Chiclet",
]


class Keyboard(TypedDict):
    id: str
    name: str
    brand_name: str
    layout: KeyboardLayout
    color_way: List[str]
    led: bool
    hot_swap: bool
    price: float
    num_of_pins: Literal[3, 5]
    led_direction: Literal["north", "south"] | None
    switch: Switch | None
    keycap: KeyCap | None
