import unittest

from Dev.RunningPlanGenerator import *

class TestRunningPlan(unittest.TestCase):

    def test_marathon_test_data(self):

        data = {
            "race": "marathon",
            "Longest_Run": 25,
            "Weekly_Distance": 55,
            "5k_pb": 20 * 60,
            "10k_pb": 44 * 60,
            "half_pb": 1 * 3600 + 40 * 60,
            "marathon_pb": 2.0,
            "level": "Intermediate",
            "CurrentPlanLength": 10,
            "ActivityDays": [
                "Tuesday",
                "Thursday",
                "Sunday"
            ],
            "LongActivityDay": "Sunday"
        }
        generator = RunningPlanGenerator(data)
        plan = generator.generate_running_plan()

        self.assertEqual(len(plan), 10)
    def test_half_marathon_test_data(self):

        data = {
            "race": "half",
            "Longest_Run": 16,
            "Weekly_Distance": 40,
            "5k_pb": 20 * 60,
            "10k_pb": 44 * 60,
            "half_pb": 2.0,
            "marathon_pb": 2.0,
            "level": "Intermediate",
            "CurrentPlanLength": 10,
            "ActivityDays": [
                "Tuesday",
                "Thursday",
                "Sunday"
            ],
            "LongActivityDay": "Sunday"
        }
        generator = RunningPlanGenerator(data)
        plan = generator.generate_running_plan()

        self.assertEqual(len(plan), 10)


    def test_10k_test_data(self):

        data = {
            "race": "10k",
            "Longest_Run": 7,
            "Weekly_Distance": 25,
            "5k_pb": 20 * 60,
            "10k_pb": 2.0,
            "half_pb": 2.0,
            "marathon_pb": 2.0,
            "level": "Beginner",
            "CurrentPlanLength": 6,
            "ActivityDays": [
                "Tuesday",
                "Thursday",
                "Sunday"
            ],
            "LongActivityDay": "Sunday"
        }
        generator = RunningPlanGenerator(data)
        plan = generator.generate_running_plan()

        self.assertEqual(len(plan), 6)

if __name__ == '__main__':
    unittest.main()