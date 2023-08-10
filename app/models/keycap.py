from typing_extensions import TypedDict


class KeyCap(TypedDict):
    id: str
    name: str
    brand_name: str
    material: str
    price: float | None
    price_per_unit: float | None
    unit_count: int | None
