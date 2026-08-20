from django.core.management.base import BaseCommand

from healthflow_be_egypt.location_seed import seed_egypt_governorates


class Command(BaseCommand):
    help = "Seed or update Egyptian governorates as openIMIS region locations."

    def add_arguments(self, parser):
        parser.add_argument(
            "--audit-user-id",
            type=int,
            default=0,
            help="Audit user identifier recorded for created or updated locations.",
        )

    def handle(self, *args, **options):
        result = seed_egypt_governorates(audit_user_id=options["audit_user_id"])
        self.stdout.write(
            self.style.SUCCESS(
                "Egypt governorates seeded: "
                f"created={result.created}, updated={result.updated}, "
                f"unchanged={result.unchanged}"
            )
        )
