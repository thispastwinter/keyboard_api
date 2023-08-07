from typing_extensions import Literal, TypedDict


class Switch(TypedDict):
    id: str
    name: str
    brand_name: str
    total_travel: str
    pre_travel: str
    num_of_pins: Literal[3, 5]
    type: Literal["clicky", "tactile", "linear"]
