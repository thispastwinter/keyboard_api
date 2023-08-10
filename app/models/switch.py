from typing_extensions import Literal, TypedDict
from app.models.switch_type import SwitchType


class Switch(TypedDict):
    id: str
    name: str
    brand_name: str
    total_travel: str
    pre_travel: str
    num_of_pins: Literal[3, 5]
    type: SwitchType
    price: float | None
    price_per_unit: float | None
    unit_count: int | None
