import unittest
from contextlib import nullcontext
from types import SimpleNamespace

from healthflow_be_egypt.location_seed import seed_egypt_governorates


class FakeManager:
    def __init__(self):
        self.records = {}

    def get_or_create(self, *, code, type, defaults):
        key = (code, type)
        if key in self.records:
            return self.records[key], False
        record = SimpleNamespace(code=code, type=type, **defaults)
        record.save = lambda update_fields: None
        self.records[key] = record
        return record, True


class FakeLocation:
    objects = FakeManager()


class GovernorateSeedTests(unittest.TestCase):
    def setUp(self):
        FakeLocation.objects = FakeManager()

    def test_first_run_creates_all_governorates_as_regions(self):
        result = seed_egypt_governorates(FakeLocation, transaction_context=nullcontext)
        self.assertEqual(result.created, 27)
        self.assertEqual(result.updated, 0)
        self.assertEqual(result.unchanged, 0)
        self.assertEqual({record.type for record in FakeLocation.objects.records.values()}, {"R"})

    def test_second_run_is_idempotent(self):
        seed_egypt_governorates(FakeLocation, transaction_context=nullcontext)
        result = seed_egypt_governorates(FakeLocation, transaction_context=nullcontext)
        self.assertEqual(result.created, 0)
        self.assertEqual(result.updated, 0)
        self.assertEqual(result.unchanged, 27)

    def test_existing_name_is_corrected(self):
        seed_egypt_governorates(FakeLocation, transaction_context=nullcontext)
        cairo = FakeLocation.objects.records[("01", "R")]
        cairo.name = "Old Cairo Label"
        result = seed_egypt_governorates(FakeLocation, transaction_context=nullcontext)
        self.assertEqual(result.updated, 1)
        self.assertEqual(cairo.name, "Cairo")


if __name__ == "__main__":
    unittest.main()
