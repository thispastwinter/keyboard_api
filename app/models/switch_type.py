from typing_extensions import TypedDict, Literal


class SwitchType(TypedDict):
    id: str
    name: Literal["clicky", "tactile", "linear"]
