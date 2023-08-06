from typing_extensions import Literal, TypedDict
from typing import List
from app.models.switch import Switch
from app.models.keycap import KeyCap

KeyboardLayout = Literal[
    "ANSI",
    "ISO",
    "TKL",
    "75%",
    "60%",
    "40%",
    "Split",
    "Ortholinear",
    "ErgoDox",
    "HHKB",
    "60% ISO",
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
    switch: Switch | None
    keycap: KeyCap | None
