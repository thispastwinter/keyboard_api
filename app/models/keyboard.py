from typing_extensions import Literal, TypedDict, get_args
from typing import List
from app.models.switch import Switch
from app.models.keycap import KeyCap
from app.models.layout import Layout

class KeyboardBase(TypedDict):
    id: str
    name: str
    brand_name: str
    color_way: List[str]
    led: bool
    hot_swap: bool
    price: float
    num_of_pins: Literal[3, 5]
    led_direction: Literal["north", "south"] | None


class KeyboardPartial(KeyboardBase):
    switch_id: str | None
    keycap_id: str | None
    layout_id: str


class KeyboardFull(KeyboardBase):
    switch: Switch | None
    keycap: KeyCap | None
    layout: Layout
