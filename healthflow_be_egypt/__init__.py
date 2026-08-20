"""Egypt-specific validation and localization helpers for HealthFlow Payer."""

from .config import DEFAULT_EGYPT_CONFIG, get_default_config
from .location_seed import SeedResult, seed_egypt_governorates
from .locations import Governorate, egypt_governorates, governorate_by_code
from .validators import EgyptianNationalId, parse_egyptian_national_id, validate_egyptian_phone

__all__ = [
    "DEFAULT_EGYPT_CONFIG",
    "EgyptianNationalId",
    "Governorate",
    "SeedResult",
    "egypt_governorates",
    "get_default_config",
    "governorate_by_code",
    "parse_egyptian_national_id",
    "seed_egypt_governorates",
    "validate_egyptian_phone",
]
