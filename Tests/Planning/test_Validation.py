import unittest
from Dev.Core.UserDataValidation import UserDataValidation


class ValidationTests(unittest.TestCase):

    def test_plan_length_is_3_valid(self):
        valid, error = UserDataValidation.validate_plan_length("3")
        self.assertTrue(valid)

    def test_plan_length_is_14_valid(self):
        valid, error = UserDataValidation.validate_plan_length("14")
        self.assertTrue(valid)

    def test_plan_length_is_1_invalid(self):
        valid, error = UserDataValidation.validate_plan_length("1")
        self.assertFalse(valid)

    def test_plan_length_is_20_invalid(self):
        valid, error = UserDataValidation.validate_plan_length("20")
        self.assertFalse(valid)

    def test_plan_length_is_a_invalid(self):
        valid, error = UserDataValidation.validate_plan_length("a")
        self.assertFalse(valid)

    def test_null_plan_length_invalid(self):
        valid, error = UserDataValidation.validate_plan_length("")
        self.assertFalse(valid)

    def test_activity_days_valid(self):
        valid, error = UserDataValidation.validate_activity_days(["Monday", "Wednesday", "Friday"])
        self.assertTrue(valid)

    def test_activity_days_lower_invalid(self):
        valid, error = UserDataValidation.validate_activity_days(["Monday"])
        self.assertFalse(valid)

    def test_null_activity_days_invalid(self):
        valid, error = UserDataValidation.validate_plan_length("")
        self.assertFalse(valid)

    def test_long_activity_day_valid(self):
        valid, error = UserDataValidation.validate_long_activity_day("Saturday")
        self.assertTrue(valid)

    def test_null_long_activity_day_invalid(self):
        valid, error = UserDataValidation.validate_long_activity_day("")
        self.assertFalse(valid)

    def test_distances_valid(self):
        valid, error = UserDataValidation.validate_distances(22, 42)
        self.assertTrue(valid)

    def test_distances_longest_lower_invalid(self):
        valid, error = UserDataValidation.validate_distances(4, 42)
        self.assertFalse(valid)

    def test_distances_weekly_lower_invalid(self):
        valid, error = UserDataValidation.validate_distances(20, 15)
        self.assertFalse(valid)

    def test_validate_level_valid(self):
        valid, error = UserDataValidation.validate_level("Advanced")
        self.assertTrue(valid)

    def test_validate_null_level_invalid(self):
        valid, error = UserDataValidation.validate_plan_length("")
        self.assertFalse(valid)

    def test_validate_pbs_valid(self):
        valid, error = UserDataValidation.validate_pbs({
            "5k": "00:20:00",
            "10k": "00:44:00",
        })
        self.assertTrue(valid)

    def test_validate_full_pbs_valid(self):
        valid, error = UserDataValidation.validate_pbs({
            "5k": "00:20:00",
            "10k": "00:44:00",
            "half": "01:40:00",
            "marathon": "04:00:00",
        })
        self.assertTrue(valid)

    def test_null_pbs_invalid(self):
        valid, error = UserDataValidation.validate_pbs({
            "5k": "",
            "10k": ""
        })
        self.assertFalse(valid)

    def test_validate_5k_10k_invalid(self):
        valid, error = UserDataValidation.validate_pbs({
            "5k": "00:40:00",
            "10k": "00:30:00",
        })
        self.assertFalse(valid)

    def test_validate_10k_half_invalid(self):
        valid, error = UserDataValidation.validate_pbs({
            "5k": "00:30:00",
            "10k": "01:00:00",
            "half": "00:50:00",
        })
        self.assertFalse(valid)

    def test_validate_half_marathon_invalid(self):
        valid, error = UserDataValidation.validate_pbs({
            "5k": "00:50:00",
            "10k": "01:00:00",
            "half": "02:30:00",
            "marathon": "02:00:00",
        })
        self.assertFalse(valid)
