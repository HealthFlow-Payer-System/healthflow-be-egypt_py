from __future__ import annotations

from dataclasses import dataclass
from datetime import date
import re


EGYPT_GOVERNORATE_CODES = frozenset(
    {
        "01", "02", "03", "04", "11", "12", "13", "14", "15", "16", "17", "18", "19",
        "21", "22", "23", "24", "25", "26", "27", "28", "29", "31", "32", "33", "34", "35",
    }
)

_EGYPTIAN_NATIONAL_ID = re.compile(r"^[23]\d{13}$")
_EGYPTIAN_MOBILE = re.compile(r"^\+20(10|11|12|15)\d{8}$")


@dataclass(frozen=True)
class EgyptianNationalId:
    value: str
    birth_date: date
    governorate_code: str
    sequence: int
    gender: str


def _luhn_checksum(value: str) -> bool:
    digits = [int(digit) for digit in value]
    checksum = 0
    parity = len(digits) % 2
    for index, digit in enumerate(digits):
        if index % 2 == parity:
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit
    return checksum % 10 == 0


def parse_egyptian_national_id(value: str) -> EgyptianNationalId:
    """Validate and parse an Egyptian 14-digit National ID.

    The first digit identifies the century, the next six digits encode the
    Gregorian birth date, digits 8–9 identify the governorate, digits 10–13
    are the sequence/gender block, and the final digit is checked with Luhn.
    """
    if not isinstance(value, str) or not _EGYPTIAN_NATIONAL_ID.fullmatch(value):
        raise ValueError("Egyptian National ID must contain exactly 14 digits and start with 2 or 3")

    century = 1900 if value[0] == "2" else 2000
    try:
        birth_date = date(
            century + int(value[1:3]),
            int(value[3:5]),
            int(value[5:7]),
        )
    except ValueError as exc:
        raise ValueError("Egyptian National ID contains an invalid birth date") from exc

    governorate_code = value[7:9]
    if governorate_code not in EGYPT_GOVERNORATE_CODES:
        raise ValueError("Egyptian National ID contains an unknown governorate code")

    if not _luhn_checksum(value):
        raise ValueError("Egyptian National ID checksum is invalid")

    sequence = int(value[9:13])
    gender = "female" if sequence % 2 == 0 else "male"
    return EgyptianNationalId(value, birth_date, governorate_code, sequence, gender)


def validate_egyptian_phone(value: str) -> bool:
    """Return whether value is an Egyptian mobile number in E.164 form."""
    return isinstance(value, str) and bool(_EGYPTIAN_MOBILE.fullmatch(value))


def validate_egyptian_insuree_number(value: str) -> list[dict]:
    """Adapt National ID validation to openIMIS ``insuree_number_validator``."""
    try:
        parse_egyptian_national_id(value)
    except ValueError as exc:
        return [{"errorCode": 5, "message": str(exc)}]
    return []
