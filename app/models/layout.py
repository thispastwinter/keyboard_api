from typing_extensions import TypedDict, Literal

KeyboardLayoutName = Literal[
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


class Layout(TypedDict):
    id: str
    name: KeyboardLayoutName
