from typing import Literal, List
from pydantic import BaseModel
from app.models.switch import Switch

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


class Keyboard(BaseModel):
    id: str
    layout: KeyboardLayout
    color_way: List[str]
    led: bool
    hot_swap: bool
    price: float
    num_of_pins: Literal[3, 5]
    switch: Switch
