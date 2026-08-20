from __future__ import annotations

from copy import deepcopy


DEFAULT_EGYPT_CONFIG = {
    "countryCode": "EG",
    "defaultLocale": "ar-EG",
    "supportedLocales": ["ar-EG", "en-GB"],
    "direction": "rtl",
    "currency": {
        "code": "EGP",
        "symbol": "ج.م",
        "fractionDigits": 2,
    },
    "nationalId": {
        "requiredLength": 14,
        "validateChecksum": True,
        "governorateCodes": "egypt_governorates",
    },
    "phone": {
        "countryCallingCode": "+20",
        "format": "E.164",
    },
}


def get_default_config() -> dict:
    """Return a mutable copy of the safe Egypt defaults."""
    return deepcopy(DEFAULT_EGYPT_CONFIG)
