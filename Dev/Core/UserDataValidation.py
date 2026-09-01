from kivy.app import App
from kivy.uix.textinput import TextInput


class UserDataValidation:

    # Validate plan Length
    @staticmethod
    def validate_plan_length(plan_length):

        data = App.get_running_app().data
        race = data["race"]

        # No input
        if not plan_length:
            return False, "Please Input your plan length."

        # Input is not a number
        if not plan_length.isdigit():
            return False, "You must input a number"

        # Plan must be higher then 3
        if int(plan_length) < 3:
            return False, "The plan must be at least 3 weeks."

        # Plan must be lower than 15
        if int(plan_length) > 14:
            return False, "The plan length must be less than 14 weeks."

        if race == "marathon":
            if int(plan_length) < 8:
                return False, "The plan length must be at least 8 weeks for a Marathon."

        if race == "half":
            if int(plan_length) < 6:
                return False, "The plan length must be at least 6 weeks for a Half-Marathon."

        if race == "10k":
            if int(plan_length) < 4:
                return False, "The plan length must be at least 4 weeks for a 10K."

        return True, ""

    # Validate Activity days
    @staticmethod
    def validate_activity_days(days):

        # No input
        if not days:
            return False, "Please select your days."

        # Activity days should be higher then 1
        if len(days) < 2:
            return False, "Please run at least 2 days."

        return True, ""

    # Validate Long Activity
    @staticmethod
    def validate_long_activity_day(day):

        # No input
        if day == "Select Day" or not day:
            return False, "Please input your long activity day."

        return True, ""

    # Validate Distances
    @staticmethod
    def validate_distances(longest_distance, weekly_distance):

        # Longest run should not be higher than weekly distance
        if weekly_distance < longest_distance:
            return False, "Weekly distance cannot be lower than your longest run."

        # Longest run should be higher than 5
        if longest_distance < 5:
            return False, "Longest distance cannot be lower then 5K."

        return True, ""

    # Validate Level
    @staticmethod
    def validate_level(level):

        # No input
        if not level:
            return False, "You must select what level runner you are."

        return True, ""

    # Convert pb into seconds
    @staticmethod
    def convert_time_to_seconds(text):
        try:
            # Split into hours minutes and seconds
            parts = text.strip().split(":")

            if len(parts) != 3:
                return None

            hours = int(parts[0])
            minutes = int(parts[1])
            seconds = int(parts[2])

            if minutes >= 60 or seconds >= 60:
                return None

            # Calculate in seconds
            return (
                    hours * 3600
                    + minutes * 60
                    + seconds
            )

        except ValueError:
            return None

    # Validate pbs
    @staticmethod
    def validate_pbs(pbs):

        # Dictionary for pbs
        pb_times = {}

        # Extract the distance and the pb from pbs
        for dist, pb_input in pbs.items():

            # for app validation
            if TextInput:
                text = pb_input.text.strip()

            # for unit tests
            elif str:
                text = pb_input.strip()

            # No input
            if not text:
                return False, f"Please enter a {dist.upper()} time.\n" "Please use HH:MM:SS."

            # Convert to seconds.
            total_seconds = UserDataValidation.convert_time_to_seconds(text)

            # No input
            if total_seconds is None:
                return False, f"Invalid {dist.upper()} time.\n" "Please use HH:MM:SS."

            # Add to pb times
            pb_times[dist] = total_seconds

        # If 5k is longer then 10k time return false
        if "5k" in pb_times and "10k" in pb_times:
            if pb_times["10k"] <= pb_times["5k"]:
                return False, "Your 10K PB must be longer than your 5K PB."

        # If 10k is longer then half-marathon time return false
        if "10k" in pb_times and "half" in pb_times:
            if pb_times["half"] <= pb_times["10k"]:
                return False, "Your Half Marathon PB must be longer than your 10K PB."

        # If half-marathon is longer then marathon time return false
        if "half" in pb_times and "marathon" in pb_times:
            if pb_times["marathon"] <= pb_times["half"]:
                return False, "Your marathon must be longer than your half PB."

        return True, ""
