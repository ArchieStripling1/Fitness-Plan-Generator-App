import unittest

from RunningPlanGenerator import RunningPlanGenerator

class TestRunningPlan(unittest.TestCase):

    def marathon_test_data(self):

        return {
            "race": "marathon",
            "Longest_Run": 25,
            "Weekly_Distance": 55,
            "5k_pb": 20 * 60,
            "10k_pb": 44 * 60,
            "half_pb": 1 * 3600 + 40 * 60,
            "marathon_pb": 2.0,
            "Level": "Intermediate",
            "CurrentPlanLength": 10,
            "ActivityDays": [
                "Tuesday",
                "Thursday",
                "Sunday"
            ],
            "LongActivityDay": "Sunday"
        }
    def half_marathon_test_data(self):

        return {
            "race": "half",
            "Longest_Run": 16,
            "Weekly_Distance": 40,
            "5k_pb": 20 * 60,
            "10k_pb": 44 * 60,
            "half_pb": 2.0,
            "marathon_pb": 2.0,
            "Level": "Intermediate",
            "CurrentPlanLength": 10,
            "ActivityDays": [
                "Tuesday",
                "Thursday",
                "Sunday"
            ],
            "LongActivityDay": "Sunday"
        }

    def k10_test_data(self):

        return {
            "race": "10k",
            "Longest_Run": 7,
            "Weekly_Distance": 25,
            "5k_pb": 20 * 60,
            "10k_pb": 2.0,
            "half_pb": 2.0,
            "marathon_pb": 2.0,
            "Level": "Beginner",
            "CurrentPlanLength": 6,
            "ActivityDays": [
                "Tuesday",
                "Thursday",
                "Sunday"
            ],
            "LongActivityDay": "Sunday"
        }


    def test_marathon_data(self):

        data = self.marathon_test_data()

        self.assertEqual(data["race"], "marathon")
        self.assertEqual(data["Longest_Run"], 25)
        self.assertEqual(data["Weekly_Distance"], 55)
        self.assertEqual(data["Level"], "Intermediate")
        self.assertEqual(data["CurrentPlanLength"], 10)

    def test_half_data(self):

        data = self.half_marathon_test_data()

        self.assertEqual(data["race"], "half")
        self.assertEqual(data["Longest_Run"], 16)
        self.assertEqual(data["Weekly_Distance"], 40)
        self.assertEqual(data["Level"], "Intermediate")
        self.assertEqual(data["CurrentPlanLength"], 10)

    def test_10k_data(self):

        data = self.k10_test_data()

        self.assertEqual(data["race"], "10k")
        self.assertEqual(data["Longest_Run"], 7)
        self.assertEqual(data["Weekly_Distance"], 25)
        self.assertEqual(data["Level"], "Beginner")
        self.assertEqual(data["CurrentPlanLength"], 6)



if __name__ == '__main__':
    unittest.main()