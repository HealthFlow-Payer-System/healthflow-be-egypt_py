import unittest

from healthflow_be_egypt import egypt_governorates, governorate_by_code
from healthflow_be_egypt.validators import parse_egyptian_national_id, validate_egyptian_phone


class EgyptianValidatorTests(unittest.TestCase):
    def test_valid_national_id_is_parsed(self):
        # 29501023201951: 1995-01-02, governorate code 32, odd sequence => male.
        parsed = parse_egyptian_national_id("29501023201951")
        self.assertEqual(parsed.birth_date.isoformat(), "1995-01-02")
        self.assertEqual(parsed.governorate_code, "32")
        self.assertEqual(parsed.gender, "male")

    def test_invalid_date_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "invalid birth date"):
            parse_egyptian_national_id("29502323201952")

    def test_invalid_governorate_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "unknown governorate"):
            parse_egyptian_national_id("29501099001952")

    def test_invalid_checksum_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "checksum"):
            parse_egyptian_national_id("29501023201953")

    def test_phone_is_e164(self):
        self.assertTrue(validate_egyptian_phone("+201012345678"))
        self.assertFalse(validate_egyptian_phone("01012345678"))

    def test_governorate_seed_contains_27_bilingual_records(self):
        governorates = egypt_governorates()
        self.assertEqual(len(governorates), 27)
        self.assertEqual(governorate_by_code("01").name_ar, "القاهرة")
        self.assertEqual(governorate_by_code("35").name_en, "South Sinai")


if __name__ == "__main__":
    unittest.main()
