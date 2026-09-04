import random
from Dev.Data.SpeedWorkoutData import SpeedWorkoutData
from Dev.Data.RaceSettingsData import RaceSettingsData


class RunningPlanGenerator:

    def __init__(self, data):
        self.data = data

    def generate_running_plan(self):

        data = self.data
        print(data)

        race = data.get("race")
        plan_length = int(data.get("CurrentPlanLength", 0))
        PB = float(data.get(f"{race}_pb", 2))
        longest_run = int(data.get("Longest_Run"))
        weekly_miles = int(data.get("Weekly_Distance"))
        activity_days = data.get("ActivityDays")
        long_run_day = data.get("LongActivityDay")
        level = data.get("level")
        weekly_hard_run = 0

        # Days in the week
        days = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]

        runlst = ["5k", "10k", "half", "marathon"]

        if race not in runlst:
            return

        # Make sure the activity days exist
        if not activity_days:
            return

        self.createPredictedTimes()
        if race in runlst:

            # Variable settings that change for each race.

            if race == "5k":
                # raceDistance = 5

                # Work out what their race pace based off their last PB
                predictedPace = PB - plan_length * 10
                race_pace = predictedPace / 5

                # Create different paces for different runs.
                easy_pace = self.formatRunPace(race_pace + 120)

            elif race == "10k":
                # if user has not run that far it will
                # get the PB that they have,
                # not run a half-marathon yet
                # so they will use their 10k PB for reference.
                # raceDistance = 10

                if PB == 2.0:
                    PB = float(data.get("10k_pb", 2))
                    race_pace = self.formatRunPace(PB / 10)
                    # Create different paces for different runs.
                    easy_pace = self.formatRunPace(PB / 10 + 120)

                else:
                    race_pace = self.formatRunPace(PB / 10)

                    # Create different paces for different runs.
                    easy_pace = self.formatRunPace(PB / 10 + 105)

            elif race == "half":
                print(PB)
                # raceDistance = 21.1
                if PB == 2.0:
                    PB = float(data.get("half_pb", 2))
                    race_pace = self.formatRunPace(PB / 21.1)

                    # Create different paces for different runs.
                    easy_pace = self.formatRunPace(PB / 21.1 + 105)
                else:
                    # Work out what their race pace based off their last PB
                    race_pace = self.formatRunPace(PB / 21.1)

                    # Create different paces for different runs.
                    easy_pace = self.formatRunPace(PB / 21.1 + 90)

            elif race == "marathon":
                # raceDistance = 42.2
                if PB == 2.0:
                    PB = float(data.get("marathon_pb", 2))
                    race_pace = self.formatRunPace(PB / 42.2)

                    # Create different paces for different runs.
                    easy_pace = self.formatRunPace(PB / 42.2 + 90)

                else:
                    # Work out what their race pace based off their last PB
                    race_pace = self.formatRunPace(PB / 42.2)

                    # Create different paces for different runs.
                    easy_pace = self.formatRunPace(PB / 42.2 + 75)

            print(PB)

            # Change max distances based of
            # their longest run and race distance.
            if RaceSettingsData.distance_greater[race]["distance"] > longest_run:
                race_settings = RaceSettingsData.distance_smaller
            else:
                race_settings = RaceSettingsData.distance_greater
            print(PB)

            # Interval/Tempo types for Beginner
            # runners which have a 5k or 10k race
            if level == "Beginner" and race in ["5k", "10k"]:

                interval_types = (SpeedWorkoutData.
                                  Beginner_Short_Interval_Types)
                tempo_types = (SpeedWorkoutData.
                               Beginner_Short_Tempo_Types)

            # Interval/Tempo types for Beginner runners
            # which have a Half-Marathon or Marathon race
            elif level == "Beginner" and race in ["half", "marathon"]:

                interval_types = (SpeedWorkoutData.
                                  Beginner_Long_Interval_Types)
                tempo_types = (SpeedWorkoutData.
                               Beginner_Long_Tempo_Types)

            # Interval/Tempo types for Novice
            # runners which have a 5k or 10k race
            elif level == "Novice" and race in ["5k", "10k"]:

                interval_types = (SpeedWorkoutData.
                                  Novice_Short_Interval_Types)
                tempo_types = (SpeedWorkoutData.
                               Novice_Short_Tempo_Types)

            # Interval/Tempo types for Novice runners
            # which have a Half-Marathon or Marathon race
            elif level == "Novice" and race in ["half", "marathon"]:

                interval_types = (SpeedWorkoutData.
                                  Novice_Long_Interval_Types)
                tempo_types = (SpeedWorkoutData.
                               Novice_Long_Tempo_Types)

            # Interval/Tempo types for Intermediate
            # runners which have a 5k or 10k race
            elif level == "Intermediate" and race in ["5k", "10k"]:

                interval_types = (SpeedWorkoutData.
                                  Intermediate_Short_Interval_Types)
                tempo_types = (SpeedWorkoutData.
                               Intermediate_Short_Tempo_Types)

            # Interval/Tempo types for Intermediate
            # runners which have a Half-Marathon or Marathon race
            elif level == "Intermediate" and race in ["half", "marathon"]:

                interval_types = (SpeedWorkoutData.
                                  Intermediate_Long_Interval_Types)
                tempo_types = (SpeedWorkoutData.
                               Intermediate_Long_Tempo_Types)

            # Interval/Tempo types for Advanced
            # runners which have a 5k or 10k race
            elif level == "Advanced" and race in ["5k", "10k"]:

                interval_types = (SpeedWorkoutData.
                                  Advanced_Short_Interval_Types)
                tempo_types = (SpeedWorkoutData.
                               Advanced_Short_Tempo_Types)

            # Interval/Tempo types for Advanced runners
            # which have a Half-Marathon or Marathon race
            elif level == "Advanced" and race in ["half", "marathon"]:

                interval_types = (SpeedWorkoutData.
                                  Advanced_Long_Interval_Types)
                tempo_types = (SpeedWorkoutData.
                               Advanced_Long_Tempo_Types)

            # Dictionary for the plan.
            plan = {}
            current_weekly_distance = 0

            # For week in range 1 to the length of the current plan
            for week in range(1, plan_length + 1):
                week_name = f"Week {week}"
                self.createPredictedTimes()

                plan[week_name] = {
                    "workouts": {},
                    "distance": 0
                }

                # Created a recovery week every 4
                # weeks which decrease the load
                recovery_week = False

                if week % 4 == 0:
                    recovery_week = True

                for day in days:
                    # Default
                    workout = {
                        "type": "Rest"
                    }
                    plan[week_name]["workouts"][day] = workout

                    # Long run
                    if day == long_run_day:

                        base_phase = []
                        build_phase = []
                        peak_phase = []
                        taper_phase = []
                        raceWeek = []

                        for i in range(1, plan_length+1):
                            position = i / plan_length

                            if position < 0.25:
                                base_phase.append(i)
                            elif position < 0.5:
                                build_phase.append(i)
                            elif position < 0.75:
                                peak_phase.append(i)
                            elif position == 1:
                                raceWeek.append(i)
                            else:
                                taper_phase.append(i)
                        print(base_phase, build_phase, peak_phase, taper_phase, raceWeek)

                        # Create a Starting Distance Memory
                        starting_distance = longest_run
                        long_run_distance = starting_distance

                        # Longest run of training
                        peak_long_run = race_settings[race]["max_long_run"]
                        peak_week = peak_phase[-1]

                        if longest_run < peak_long_run:
                            # Calculate Up step to peak weak
                            up_step = (
                                round((peak_long_run - starting_distance) / peak_week, 1)
                            )

                            # Calculate down step for taper phase
                            down_step = 1 - (0.2 * (week - peak_week))

                            # Calculate weekly long run progression
                            long_run_progress = (
                                    week * up_step
                            )

                            # Calculate weekly long run decrease for taper
                            long_run_decrease = (
                                    race_settings[race]["max_long_run"] * down_step
                            )

                            # Starting week == longest run
                            if week == base_phase[0]:
                                long_run_distance = starting_distance

                            # Peak week == max long run
                            elif week == peak_week:
                                long_run_distance = race_settings[race]["max_long_run"]

                            # Weekly progression
                            elif (week in base_phase) or (week in build_phase) or (week in peak_phase):
                                long_run_distance = (
                                        starting_distance + long_run_progress
                                )

                            # Taper fade
                            elif week in taper_phase:
                                long_run_distance = (
                                    round(long_run_decrease)
                                )

                        elif longest_run > peak_long_run:

                            up_step = (
                                round((peak_long_run - race_settings[race]["min_long_run"]) / peak_week, 1)
                            )

                            # Calculate down step for taper phase
                            down_step = 1 - (0.2 * (week - peak_week))

                            # Calculate weekly long run progression
                            long_run_progress = (
                                    week * up_step
                            )

                            # Calculate weekly long run decrease for taper
                            long_run_decrease = (
                                    race_settings[race]["max_long_run"] * down_step
                            )

                            # Starting week == longest run
                            if week == base_phase[0]:
                                long_run_distance = race_settings[race]["min_long_run"]

                            # Peak week == max long run
                            elif week == peak_week:
                                long_run_distance = race_settings[race]["max_long_run"]

                            # Weekly progression
                            elif week in base_phase:
                                long_run_distance = (
                                    race_settings[race]["min_long_run"] + long_run_progress
                                )
                            elif week in build_phase:
                                long_run_distance = (
                                        race_settings[race]["min_long_run"] + long_run_progress
                                )
                            elif week in peak_phase:
                                long_run_distance = (
                                    race_settings[race]["min_long_run"] + long_run_progress
                                )

                            # Taper fade
                            elif week in taper_phase:
                                long_run_distance = (
                                    round(long_run_decrease)
                                )

                        # Prevent going over max
                        if (long_run_distance >
                                race_settings[race]["max_long_run"]):
                            long_run_distance = \
                                race_settings[race]["max_long_run"]

                        if recovery_week:
                            long_run_distance *= 0.95

                        workout = {
                            "type": "Long Run",
                            "distance": int(long_run_distance),
                            "pace": "Conversational Pace"
                        }
                        plan[week_name]["workouts"][day] = workout

                        # Keep track of how far they have run this week.
                        current_weekly_distance += long_run_distance

                    # Other running days
                    elif day in activity_days:

                        # First activity day = hard session
                        if weekly_hard_run == 0:

                            # Select actual session
                            if week % 2 == 0:
                                # Session type is Tempo Run.
                                hard_type = "Tempo Run"

                                # Get Session name and session
                                # info from tempo types.
                                session, session_info = random.choice(
                                    list(tempo_types.items()))

                                # Get Pace from Session info.
                                pace = session_info["Pace"]

                                # If there is a PaceOffset then
                                # get that from session info.
                                if "PaceOffset" in session_info:
                                    paceoffset = session_info["PaceOffset"]

                                    # If the pace is in list of races
                                    if pace in ["5k", "10k", "half",
                                                "marathon"]:

                                        # Get that race PB
                                        P = float(data.get(f"{pace}_pb", 2))

                                        # RacePace = Race PB + or - paceoffset
                                        racePace = P + paceoffset

                                        # If race is a 5k divide it by 5
                                        # and formatRunPace for
                                        # the interval pace
                                        if pace == "5k":
                                            new_race_pace = racePace / 5
                                            interval_pace = (self.
                                                             formatRunPace(new_race_pace))
                                            workout_pace = interval_pace

                                        # If race is a 10k divide it by 10
                                        # and formatRunPace for the interval pace
                                        elif pace == "10k":
                                            new_race_pace = racePace / 10
                                            interval_pace = (self.
                                                             formatRunPace(new_race_pace))
                                            workout_pace = interval_pace

                                        # If race is a Half-Marathon divide it
                                        # by 21 and formatRunPace for the interval pace
                                        elif pace == "half":
                                            new_race_pace = racePace / 21
                                            interval_pace = (self.
                                                             formatRunPace(new_race_pace))
                                            workout_pace = interval_pace

                                        # If race is a Marathon divide it by 42
                                        # and formatRunPace for the interval pace
                                        elif pace == "marathon":
                                            new_race_pace = racePace / 42
                                            interval_pace = (self.
                                                             formatRunPace(new_race_pace))
                                            workout_pace = interval_pace

                                    else:

                                        workout_pace = pace
                                else:
                                    workout_pace = pace

                                # Get all variables of session info.
                                warmup = session_info["Warm-Up"]
                                cooldown = session_info["Cooldown"]
                                recovery = session_info["Recovery"]
                                reps = session_info["Reps"]
                                interval = session_info["Interval"]

                                # Format them using function into Description.
                                description = self.formatRunDescription(
                                    warmup,
                                    reps,
                                    recovery,
                                    workout_pace,
                                    interval,
                                    cooldown)

                                print(description)

                            else:
                                # Session type is tempo run.
                                hard_type = "Interval Run"

                                # Get Session name and session
                                # info from tempo types.
                                session, session_info = random.choice(
                                    list(interval_types.items()))

                                pace = session_info["Pace"]

                                if "PaceOffset" in session_info:
                                    paceoffset = session_info["PaceOffset"]

                                    if pace in ["5k", "10k", "half", "marathon"]:
                                        P = float(data.get(f"{pace}_pb", 2))
                                        racePace = P + paceoffset

                                        if pace == "5k":
                                            new_race_pace = racePace / 5
                                            interval_pace = (self.
                                                             formatRunPace(new_race_pace))
                                            workout_pace = interval_pace
                                        elif pace == "10k":
                                            new_race_pace = racePace / 10
                                            interval_pace = (self.
                                                             formatRunPace(new_race_pace))
                                            workout_pace = interval_pace
                                        elif pace == "half":
                                            new_race_pace = racePace / 21
                                            interval_pace = (self.
                                                             formatRunPace(new_race_pace))
                                            workout_pace = interval_pace
                                        elif pace == "marathon":
                                            new_race_pace = racePace / 42
                                            interval_pace = (self.
                                                             formatRunPace(new_race_pace))
                                            workout_pace = interval_pace

                                    else:

                                        workout_pace = pace
                                else:
                                    workout_pace = pace

                                warmup = session_info["Warm-Up"]
                                cooldown = session_info["Cooldown"]
                                recovery = session_info["Recovery"]
                                reps = session_info["Reps"]
                                interval = session_info["Interval"]

                                description = self.formatRunDescription(
                                    warmup,
                                    reps,
                                    recovery,
                                    workout_pace,
                                    interval,
                                    cooldown)

                                print(description)

                            # Create nested dict to store
                            # everything for the run
                            workout = {
                                "type": hard_type,
                                "session": session,
                                "distance": session_info["Distance"],
                                "pace": workout_pace
                            }
                            plan[week_name]["workouts"][day] \
                                = workout

                            current_weekly_distance += \
                                session_info["Distance"]

                        # Remaining = easy runs
                        else:
                            easy_distance = (
                                (weekly_miles / len(activity_days))
                            )

                            # Prevent going over max
                            if (easy_distance >
                                    race_settings[race]["max_easy_run"]):
                                easy_distance = \
                                    race_settings[race]["max_easy_run"]

                            if recovery_week:
                                easy_distance *= 0.8

                            # Create nested dict to store
                            # everything for the run
                            workout = {
                                "type": "Easy Run",
                                "distance": int(easy_distance),
                                "pace": easy_pace
                            }
                            plan[week_name]["workouts"][day] \
                                = workout
                            current_weekly_distance \
                                += easy_distance

                        # No more than one hard
                        # run a week right now.
                        weekly_hard_run += 1

                    # Race Week Workout
                    if week == plan_length:
                        workout = {
                            "type": "Rest"
                        }
                        plan[week_name]["workouts"][day] = workout
                        if day == "Wednesday":
                            workout = {
                                "type": "Race Practice Session!",
                                "distance": "Race Pace Miles x 3",
                                "pace": race_pace
                            }
                            plan[week_name]["workouts"][day] \
                                = workout
                        if day == "Sunday":
                            workout = {
                                "type": "Race Day!",
                                "distance": race.capitalize(),
                                "pace": race_pace
                            }
                            plan[week_name]["workouts"][day] \
                                = workout

                # Reset for next week
                plan[week_name]["distance"] = round(
                    current_weekly_distance)
                weekly_hard_run = 0
                weekly_miles = current_weekly_distance
                current_weekly_distance = 0

            data["GeneratedPlan"] = plan

            return plan

    def createPredictedTimes(self):
        data = self.data
        pb_5k = float(data.get("5k_pb", 2))
        pb_10k = float(data.get("10k_pb", 2))
        pb_half = float(data.get("half_pb", 2))
        pb_marathon = float(data.get(
            "marathon_pb", 2))
        active_pbs = {}
        non_active_pbs = {}

        pbs = {
            "5k": pb_5k,
            "10k": pb_10k,
            "half": pb_half,
            "marathon": pb_marathon

        }

        for distance, pb in pbs.items():
            if pb == 2.0:
                non_active_pbs[distance] = pb
            else:
                active_pbs[distance] = pb

        if "10k" not in active_pbs:

            if "5k" in active_pbs:
                time_5k = active_pbs["5k"]

                predicted_10k = int(
                    time_5k * (10 / 5) * 1.08
                )

                active_pbs["10k"] = predicted_10k

            # 10K -> Half Marathon
        if "half" not in active_pbs:

            if "10k" in active_pbs:
                time_10k = active_pbs["10k"]

                predicted_half = int(
                    time_10k * (21.0975 / 10) * 1.08
                )

                active_pbs["half"] = predicted_half

            # Half Marathon -> Marathon
        if "marathon" not in active_pbs:

            if "half" in active_pbs:
                time_half = active_pbs["half"]

                predicted_marathon = int(
                    time_half * (42.195 /
                                 21.0975) * 1.05
                )

                active_pbs["marathon"] = predicted_marathon

        for distance, pb in active_pbs.items():
            active_pbs[distance] = (self.
                                    format_time(pb))
            data[f"{distance}_pb"] = pb
            data[f"prediction_{distance}"] = (
                self.format_time(pb))

        return print(active_pbs)

    def formatRunPace(self, PB):

        # Turn seconds into minutes and seconds
        # rounded to the nearest division of 5.
        minutes = int(PB // 60)
        seconds = 5 * int(round((PB % 60) / 5))
        if seconds == 60:
            minutes += 1
            seconds = 0

        # Return the formated string.
        return f"{minutes}:{seconds:02d}/km"

    def format_time(self, seconds):
        seconds = int(seconds)

        hours = seconds // 3600
        minutes = (seconds % 3600) // 60

        return f"{hours:02d}:{minutes:02d}:00"

        # Format the run Description.

    def formatRunDescription(self, warmup, reps,
                             recovery, pace, interval, cooldown):

        if interval is not list:
            return f"""\
                • Warm up with {warmup} at a conversational pace.

                • Run {interval} at {pace}.

                • {recovery} for recovery.

                • Repeat {reps} times.

                • Cool down with {cooldown} at a conversational pace.
                """
        else:
            return "-"
