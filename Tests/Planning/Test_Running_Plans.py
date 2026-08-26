import unittest

from Dev.RunningPlanGenerator import *

class TestRunningPlan(unittest.TestCase):

    # Generate Plan so no reuse of code
    def generate_plan(self, data):
        generator = RunningPlanGenerator(data)
        return generator.generate_running_plan()

    # Create Marathon Test Data
    def marathon_test_data(self):
        return {
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

    # Test Plan Length of Marathon plan
    def test_marathon_plan_length(self):
        plan = self.generate_plan(self.marathon_test_data())

        print(plan)
        self.assertEqual(len(plan), 10)

    # Test Race day of Marathon plan
    def test_marathon_race_day(self):
        plan = self.generate_plan(self.marathon_test_data())

        race_day = plan["Week 10"]["workouts"]["Sunday"]

        self.assertEqual(race_day["type"], "Race Day!")
        self.assertEqual(race_day["distance"], "Marathon")

    # Test Long run of Marathon plan
    def test_marathon_race_long_run(self):
        plan = self.generate_plan(self.marathon_test_data())

        for week, week_data in plan.items():
            if week != "Week 10":
                sunday = week_data["workouts"]["Sunday"]

                self.assertEqual(sunday["type"], "Long Run")

    # Test Rest day of Marathon Plan
    def test_marathon_race_rest_day(self):
        plan = self.generate_plan(self.marathon_test_data())

        for week, week_data in plan.items():
            if week != "Week 10":
                workouts = week_data["workouts"]

                self.assertEqual(workouts["Monday"]["type"], "Rest")
                self.assertEqual(workouts["Wednesday"]["type"], "Rest")
                self.assertEqual(workouts["Friday"]["type"], "Rest")
                self.assertEqual(workouts["Saturday"]["type"], "Rest")

    # Create Half-Marathon Test data
    def half_marathon_test_data(self):

        return {
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
                "Monday",
                "Thursday",
                "Saturday"
            ],
            "LongActivityDay": "Saturday"
        }

    # Test Plan length of Half-Marathon plan
    def test_half_marathon_race_plan_length(self):
        plan = self.generate_plan(self.half_marathon_test_data())

        self.assertEqual(len(plan), 10)

    # Test Race day of Half-Marathon plan
    def test_half_marathon_race_day(self):
        plan = self.generate_plan(self.half_marathon_test_data())

        race_day = plan["Week 10"]["workouts"]["Sunday"]

        self.assertEqual(race_day["type"], "Race Day!")
        self.assertEqual(race_day["distance"], "Half")

    # Test Long run of Half-Marathon plan
    def test_half_marathon_race_long_run(self):
        plan = self.generate_plan(self.half_marathon_test_data())

        for week, week_data in plan.items():
            if week != "Week 10":
                saturday = week_data["workouts"]["Saturday"]

                self.assertEqual(saturday["type"], "Long Run")

    # Test Race day of Half-Marathon plan
    def test_half_marathon_race_rest_day(self):
        plan = self.generate_plan(self.half_marathon_test_data())

        for week, week_data in plan.items():
            if week != "Week 10":
                workouts = week_data["workouts"]

                self.assertEqual(workouts["Tuesday"]["type"], "Rest")
                self.assertEqual(workouts["Wednesday"]["type"], "Rest")
                self.assertEqual(workouts["Friday"]["type"], "Rest")
                self.assertEqual(workouts["Sunday"]["type"], "Rest")

    # Create 10k Test Data
    def test_10k_data(self):
        return {
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

    # Test Plan length of 10k plan
    def test_10k_race_plan_length(self):
        plan = self.generate_plan(self.test_10k_data())

        self.assertEqual(len(plan), 6)

    # Test Race day of 10k plan
    def test_10k_race_day(self):
        plan = self.generate_plan(self.test_10k_data())

        race_day = plan["Week 6"]["workouts"]["Sunday"]

        self.assertEqual(race_day["type"], "Race Day!")
        self.assertEqual(race_day["distance"], "10k")

    # Test Long Run of 10k plan
    def test_10k_race_long_run(self):
        plan = self.generate_plan(self.test_10k_data())

        for week, week_data in plan.items():
            if week != "Week 6":
                sunday = week_data["workouts"]["Sunday"]

                self.assertEqual(sunday["type"], "Long Run")

    # Test Rest day of 10k plan
    def test_10k_race_rest_day(self):
        plan = self.generate_plan(self.test_10k_data())

        for week, week_data in plan.items():
            if week != "Week 6":
                workouts = week_data["workouts"]

                self.assertEqual(workouts["Monday"]["type"], "Rest")
                self.assertEqual(workouts["Wednesday"]["type"], "Rest")
                self.assertEqual(workouts["Friday"]["type"], "Rest")
                self.assertEqual(workouts["Saturday"]["type"], "Rest")

if __name__ == '__main__':
    unittest.main()