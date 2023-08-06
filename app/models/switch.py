from pydantic import BaseModel
from typing import Literal


class Switch(BaseModel):
    id: str
    bottom_force: str
    total_travel: str
    pre_travel: str
    initial_force: str
    num_of_pins: Literal[3, 5]
    led_direction: Literal["north", "south"]
    type: Literal["clicky", "tactile", "linear"]
