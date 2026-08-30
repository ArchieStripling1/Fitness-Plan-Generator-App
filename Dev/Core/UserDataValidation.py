

class UserDataValidation:

    @staticmethod
    def validate_plan_length(plan_length):

        if not plan_length:
            return False, "Please Input your plan length."

        if not plan_length.isdigit():
            return False, "You must input a number"

        if int(plan_length) < 3:
            return False, "The plan must be at least 3 weeks."

        if int(plan_length) > 14:
            return False, "The plan length must be less than 14 weeks."

        return True, ""

    @staticmethod
    def validate_activity_days(days):

        if not days:
            return False, "Please select your days."

        if len(days) < 2:
            return False, "Please run at least 2 days."

        return True, ""

    @staticmethod
    def validate_long_activity_day(day):

        if day == "Select Day":
            return False, "Please input your long activity day."

        return True, ""

    @staticmethod
    def validate_distances(longest_distance, weekly_distance):
        if weekly_distance < longest_distance:
            return False, "Weekly distance cannot be lower than your longest run."

        if longest_distance < 5:
            return False, "Longest distance cannot be lower then 5K."

        return True, ""

    @staticmethod
    def validate_level(level):
        if not level:
            return False, "You must select what level runner you are."

        return True, ""

    @staticmethod
    def convert_time_to_seconds(text):
        try:
            parts = text.strip().split(":")

            if len(parts) != 3:
                return None

            hours = int(parts[0])
            minutes = int(parts[1])
            seconds = int(parts[2])

            if minutes >= 60 or seconds >= 60:
                return None

            return (
                    hours * 3600
                    + minutes * 60
                    + seconds
            )

        except ValueError:
            return None

    @staticmethod
    def validate_pbs(pbs):
        for dist, pb_input in pbs.items():
            pb_times = {}
            text = pb_input.text.strip()

            if not text:
                return False, f"Please enter a {dist.upper()} time.\n" "Please use HH:MM:SS."

            total_seconds = UserDataValidation.convert_time_to_seconds(text)

            if total_seconds is None:
                return False, f"Invalid {dist.upper()} time.\n" "Please use HH:MM:SS."

            pb_times[dist] = total_seconds

            # DOESN'T WORK YET

            # if "5k" in pb_times and "10k" in pb_times:
            #     if pb_times["10k"] <= pb_times["5k"]:
            #         return False, "Your 10K PB must be longer than your 5K PB."
            #
            # if "10k" in pb_times and "half" in pb_times:
            #     if pb_times["half"] <= pb_times["10k"]:
            #         return False, "Your Half Marathon PB must be longer than your 10K PB."
            #
            # if "half" in pb_times and "marathon" in pb_times:
            #     if pb_times["marathon"] <= pb_times["half"]:
            #         return False, "Your marathon must be longer than your half PB."

        return True, ""
