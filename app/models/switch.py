from typing_extensions import Literal, TypedDict


class Switch(TypedDict):
    id: str
    name: str
    brand_name: str
    bottom_force: str
    total_travel: str
    pre_travel: str
    initial_force: str
    num_of_pins: Literal[3, 5]
    led_direction: Literal["north", "south"]
    type: Literal["clicky", "tactile", "linear"]
