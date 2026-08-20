from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .locations import egypt_governorates


@dataclass(frozen=True)
class SeedResult:
    created: int
    updated: int
    unchanged: int

    @property
    def total(self) -> int:
        return self.created + self.updated + self.unchanged


def seed_egypt_governorates(
    location_model: Any = None,
    *,
    audit_user_id: int = 0,
    transaction_context: Any = None,
) -> SeedResult:
    """Idempotently create or update Egypt governorates as openIMIS regions.

    The standard openIMIS ``Location`` model has one display-name column, so
    the English name is stored in ``name`` while the package catalog retains
    the Arabic name for locale-aware presentation and later location-label
    integration.
    """
    if location_model is None:
        from location.models import Location

        location_model = Location

    if transaction_context is None:
        from django.db import transaction

        transaction_context = transaction.atomic

    created = updated = unchanged = 0
    with transaction_context():
        for governorate in egypt_governorates():
            location, was_created = location_model.objects.get_or_create(
                code=governorate.code,
                type="R",
                defaults={
                    "name": governorate.name_en,
                    "parent_id": None,
                    "audit_user_id": audit_user_id,
                },
            )
            if was_created:
                created += 1
                continue
            if location.name != governorate.name_en:
                location.name = governorate.name_en
                location.audit_user_id = audit_user_id
                location.save(update_fields=["name", "audit_user_id"])
                updated += 1
            else:
                unchanged += 1

    return SeedResult(created=created, updated=updated, unchanged=unchanged)
