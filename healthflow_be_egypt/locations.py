from __future__ import annotations

import json
from dataclasses import dataclass
from importlib.resources import files


@dataclass(frozen=True)
class Governorate:
    code: str
    name_en: str
    name_ar: str


def egypt_governorates() -> tuple[Governorate, ...]:
    data_file = files("healthflow_be_egypt").joinpath("data/egypt_governorates.json")
    raw = json.loads(data_file.read_text(encoding="utf-8"))
    return tuple(Governorate(**record) for record in raw)


def governorate_by_code(code: str) -> Governorate:
    for governorate in egypt_governorates():
        if governorate.code == code:
            return governorate
    raise KeyError(f"Unknown Egyptian governorate code: {code}")
