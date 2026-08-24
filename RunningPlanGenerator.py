import random

from kivy.app import App

class RunningPlanGenerator:

    def __init__(self, data):
        self.data = data

    def generate_running_plan(self):

        data = self.data

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
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

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
                raceDistance = 5

                # Work out what their race pace based off their last PB
                predictedPace = PB - plan_length * 10
                race_pace = predictedPace / 5

                # Create different paces for different runs.
                easy_pace = self.formatRunPace(race_pace + 120)


            elif race == "10k":
                # if user has not run that far it will get the PB that they have,
                # not run a half-marathon yet so they will use their 10k PB for reference.
                raceDistance = 10

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
                raceDistance = 21.1
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
                raceDistance = 42.2
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

            # Change max distances based of their longest run and race distance.
            if raceDistance > longest_run:
                race_settings = {
                    "5k": {
                        "max_long_run": 5,
                        "max_easy_run": 3,
                        "speed": "fast"
                    },
                    "10k": {
                        "max_long_run": 10,
                        "max_easy_run": 6,
                        "speed": "semi-fast"

                    },
                    "half": {
                        "max_long_run": 20,
                        "max_easy_run": 8,
                        "speed": "medium"
                    },
                    "marathon": {
                        "max_long_run": 34,
                        "max_easy_run": 15,
                        "speed": "slow"
                    }
                }
            else:
                race_settings = {
                    "5k": {
                        "max_long_run": 12,
                        "max_easy_run": 6,
                        "speed": "fast"
                    },
                    "10k": {
                        "max_long_run": 16,
                        "max_easy_run": 8,
                        "speed": "semi-fast"

                    },
                    "half": {
                        "max_long_run": 26,
                        "max_easy_run": 13,
                        "speed": "medium"
                    },
                    "marathon": {
                        "max_long_run": 38,
                        "max_easy_run": 20,
                        "speed": "slow"
                    }
                }

            print(PB)

            # If Level beginner these are the interval and tempo types of runs.
            if level == "Beginner":
                interval_types = {
                    # Name of the Interval Type.
                    "6 x 200M": {
                        # How long the Warm-up is before the intervals start.
                        "Warm-Up": "1.5K",
                        # How many reps there is in the intervals.
                        "Reps": 6,
                        # What pace they will run the interval at.
                        "Pace": "5k",
                        # Whether there is any change to the pace.
                        "PaceOffset": 0,
                        # What the interval is.
                        "Interval": "200M",
                        # What the recovery is inbetween each interval.
                        "Recovery": "Walk 60/90 seconds",
                        # What the cooldown is after the intervals are complete.
                        "Cooldown": "1K",
                        # Probable distance of the run.
                        "Distance": 3.7
                    },
                    "8 x 1 Minute": {
                        "Warm-Up": "1.5K",
                        "Reps": 8,
                        "Pace": "Hard",
                        "PaceOffset": 0,
                        "Interval": "1 Minute",
                        "Recovery": "Walk for 90 seconds",
                        "Cooldown": "1K",
                        "Distance": 4
                    },
                    "5 x 400M": {
                        "Warm-Up": "1.5K",
                        "Reps": 5,
                        "Pace": "5k",
                        "PaceOffset": 0,
                        "Interval": "400M",
                        "Recovery": "Walk for 90 seconds",
                        "Cooldown": "1K",
                        "Distance": 4.5
                    }
                }

                # Name of the Tempo Type
                tempo_types = {
                    "20 Minute Tempo": {
                        "Warm-Up": "10 Minutes",
                        "Reps": 1,
                        "Pace": "Run 20 minutes at 'comfortably hard'",
                        "PaceOffset": 0,
                        "Interval": "20 Minutes",
                        "Recovery": "Walk for 2 minutes",
                        "Cooldown": "10 Minutes",
                        "Distance": 6
                    },
                    "3 x 8 Minutes Tempo": {
                        "Warm-Up": "10 Minutes",
                        "Reps": 3,
                        "Pace": "Run 8 minutes at 'comfortably hard'",
                        "PaceOffset": 0,
                        "Interval": "8 Minutes",
                        "Recovery": "Walk for 2 minutes",
                        "Cooldown": "10 Minute Easy jog",
                        "Distance": 6.5
                    }

                }

            # Interval/Tempo types for Intermediate runners which have a 5k or 10k race
            elif level == "Intermediate" and race in ["5k", "10k"]:
                interval_types = {
                    "1K-2K-1K Pyramid": {
                        "Warm-Up": "2km",
                        "Reps": 1,
                        "Pace": "5k",
                        "PaceOffset": 0,
                        "Interval": "1K-2K-1K",
                        "Recovery": "Walk 90 seconds",
                        "Cooldown": "2km",
                        "Distance": 10
                    },
                    "12 x 300M": {
                        "Warm-Up": "2km",
                        "Reps": 12,
                        "Pace": "5k",
                        "PaceOffset": -30,
                        "Interval": "300M",
                        "Recovery": "Walk 60 seconds",
                        "Cooldown": "2km",
                        "Distance": 7.6
                    },
                    "4 x 1200M": {
                        "Warm-Up": "2km",
                        "Reps": 4,
                        "Pace": "5k",
                        "PaceOffset": 0,
                        "Interval": "1200M",
                        "Recovery": "Walk 90 seconds",
                        "Cooldown": "2km",
                        "Distance": 8.8
                    },
                    "8 x 400M": {
                        "Warm-Up": "2km",
                        "Reps": 8,
                        "Pace": "5k",
                        "PaceOffset": -30,
                        "Interval": "400M",
                        "Recovery": "Walk 90 seconds",
                        "Cooldown": "2km",
                        "Distance": 7.2
                    },
                    "6 x 800M": {
                        "Warm-Up": "2km",
                        "Reps": 6,
                        "Pace": "5k",
                        "PaceOffset": -10,
                        "Interval": "800M",
                        "Recovery": "Walk 90 seconds",
                        "Cooldown": "1.5km",
                        "Distance": 10.7
                    },
                    "5 x 1km": {
                        "Warm-Up": "2km",
                        "Reps": 5,
                        "Pace": "5k",
                        "PaceOffset": 0,
                        "Interval": "1K",
                        "Recovery": "Walk 90 seconds",
                        "Cooldown": "2km",
                        "Distance": 9
                    },
                    "Hill Repeats x 10": {
                        "Warm-Up": "3km",
                        "Reps": 10,
                        "Pace": "Hard",
                        "PaceOffset": 0,
                        "Interval": "1 Minute",
                        "Recovery": "Walk 90 seconds",
                        "Cooldown": "2km",
                        "Distance": 7
                    }
                }

                tempo_types = {
                    "Tempo 3-2-1": {
                        "Warm-Up": "2km",
                        "Reps": 3,
                        "Pace": "3K Moderate, 2K Harder, 1K Hard",
                        "PaceOffset": 0,
                        "Interval": ["3K", "2K", "1K"],
                        "Recovery": None,
                        "Cooldown": "2km",
                        "Distance": 10
                    },
                    "Tempo 2-2-1": {
                        "Warm-Up": "2km",
                        "Reps": 3,
                        "Pace": "2K Hard, 2K Hard, 1K Hard",
                        "PaceOffset": 0,
                        "Interval": ["2K", "2K", "1K"],
                        "Recovery": None,
                        "Cooldown": "2km",
                        "Distance": 9
                    },
                    "Tempo 3K x 2": {
                        "Warm-Up": "2km",
                        "Reps": 2,
                        "Pace": "10k",
                        "PaceOffset": -20,
                        "Interval": "3K",
                        "Recovery": "Walk 120 seconds",
                        "Cooldown": "2km",
                        "Distance": 10
                    },
                    "Over Under 1Ks": {
                        "Warm-Up": "2km",
                        "Reps": 3,
                        "Pace": "Over: 5K pace, Under: 5K pace + 60 seconds",
                        "PaceOffset": 0,
                        "Interval": ["1K", "1K"],
                        "Recovery": None,
                        "Cooldown": "2km",
                        "Distance": 10
                    },
                    "Continuous Tempo 8K": {
                        "Warm-Up": "2km",
                        "Reps": 1,
                        "Pace": "10k",
                        "PaceOffset": +30,
                        "Interval": "8K",
                        "Recovery": None,
                        "Cooldown": "2km",
                        "Distance": 12
                    },
                    "Progression 10K": {
                        "Warm-Up": "2km",
                        "Reps": 1,
                        "Pace": "Start Easy, Finish at 10K pace",
                        "PaceOffset": 0,
                        "Interval": "10K",
                        "Recovery": None,
                        "Cooldown": "1km",
                        "Distance": 13
                    }
                }

            # Interval/Tempo types for Intermediate runners which have a Half-Marathon or Marathon race
            elif level == "Intermediate" and race in ["half", "marathon"]:
                interval_types = {
                    "4 x 2km": {
                        "Warm-Up": "2km",
                        "Reps": 4,
                        "Pace": "half",
                        "PaceOffset": 0,
                        "Interval": "2K",
                        "Recovery": "Walk 120 seconds",
                        "Cooldown": "2km",
                        "Distance": 12
                    },
                    "3 x 3km": {
                        "Warm-Up": "2km",
                        "Reps": 3,
                        "Pace": "half",
                        "PaceOffset": 0,
                        "Interval": "3K",
                        "Recovery": "Walk 120 seconds",
                        "Cooldown": "2km",
                        "Distance": 13
                    },
                    "Hill Repeats x 12": {
                        "Warm-Up": "3km",
                        "Reps": 12,
                        "Pace": "Hard",
                        "PaceOffset": 0,
                        "Interval": "1 Minute",
                        "Recovery": "90 seconds downhill",
                        "Cooldown": "2km",
                        "Distance": 8
                    },
                    "6 x 1km": {
                        "Warm-Up": "2km",
                        "Reps": 6,
                        "Pace": "10k",
                        "PaceOffset": 0,
                        "Interval": "1K",
                        "Recovery": "Walk 90 seconds",
                        "Cooldown": "2km",
                        "Distance": 10
                    },
                    "5 x mile": {
                        "Warm-Up": "2.5km",
                        "Reps": 5,
                        "Pace": "5k",
                        "PaceOffset": 0,
                        "Interval": "Mile",
                        "Recovery": "Walk 90 seconds",
                        "Cooldown": "2km",
                        "Distance": 12.5
                    }
                }
                tempo_types = {
                    "Continuous Tempo 12K": {
                        "Warm-Up": "2km",
                        "Reps": 1,
                        "Pace": "half",
                        "PaceOffset": 0,
                        "Interval": "12K",
                        "Recovery": None,
                        "Cooldown": "2km",
                        "Distance": 16
                    },
                    "Alternating Tempo 2Ks": {
                        "Warm-Up": "3km",
                        "Reps": 3,
                        "Pace": "(2K Threshold / 1K Marathon pace)",
                        "PaceOffset": 0,
                        "Interval": ["2K", "1K"],
                        "Recovery": None,
                        "Cooldown": "2km",
                        "Distance": 14
                    },
                    "Tempo 5K x 2": {
                        "Warm-Up": "2km",
                        "Reps": 5,
                        "Pace": "10k",
                        "PaceOffset": -20,
                        "Interval": "5K",
                        "Recovery": "Walk 120 seconds",
                        "Cooldown": "2km",
                        "Distance": 14
                    },
                    "Tempo 6K x 2": {
                        "Warm-Up": "2km",
                        "Reps": 2,
                        "Pace": "marathon",
                        "PaceOffset": 0,
                        "Interval": "6K",
                        "Recovery": "Walk 120 seconds",
                        "Cooldown": "2km",
                        "Distance": 16
                    }

                }

            # Interval/Tempo types for Advanced runners which have a 5k or 10k race
            elif level == "Advanced" and race in ["5k", "10k"]:
                interval_types = {
                    "10 x 600M": {
                        "Warm-Up": "3km",
                        "Reps": 10,
                        "Pace": "5k",
                        "PaceOffset": -20,
                        "Interval": "600M",
                        "Recovery": "Walk 75 seconds",
                        "Cooldown": "3km",
                        "Distance": 12
                    },
                    "6 x 1200M": {
                        "Warm-Up": "3km",
                        "Reps": 6,
                        "Pace": "5k",
                        "PaceOffset": -5,
                        "Interval": "1200M",
                        "Recovery": "Walk 90 seconds",
                        "Cooldown": "3km",
                        "Distance": 13.2
                    },
                    "12 x 400M": {
                        "Warm-Up": "3km",
                        "Reps": 12,
                        "Pace": "5k",
                        "PaceOffset": -30,
                        "Interval": "400M",
                        "Recovery": "Walk 90 seconds",
                        "Cooldown": "3km",
                        "Distance": 11
                    },
                    "9 x 800M": {
                        "Warm-Up": "2.5km",
                        "Reps": 9,
                        "Pace": "5k",
                        "PaceOffset": -10,
                        "Interval": "800M",
                        "Recovery": "Walk 90 seconds",
                        "Cooldown": "2.5km",
                        "Distance": 12.2
                    },
                    "5 x 1km": {
                        "Warm-Up": "3km",
                        "Reps": 5,
                        "Pace": "5k",
                        "PaceOffset": 0,
                        "Interval": "1K",
                        "Recovery": "Walk 90 seconds",
                        "Cooldown": "3km",
                        "Distance": 11
                    },
                    "3 x mile": {
                        "Warm-Up": "3km",
                        "Reps": 3,
                        "Pace": "5k",
                        "PaceOffset": +10,
                        "Interval": "Mile",
                        "Recovery": "Walk 90 seconds",
                        "Cooldown": "3km",
                        "Distance": 10.8
                    }
                }
                tempo_types = {
                    "Over Under 1Ks": {
                        "Warm-Up": "2km",
                        "Reps": 5,
                        "Pace": "Over: 5K pace, Under: 5K pace + 60 seconds",
                        "PaceOffset": 0,
                        "Interval": ["1K", "1K"],
                        "Recovery": None,
                        "Cooldown": "2km",
                        "Distance": 12
                    },
                    "Tempo 3-2-1": {
                        "Warm-Up": "3km",
                        "Reps": 1,
                        "Pace": "3K Moderate, 2K Harder, 1K Hard",
                        "PaceOffset": 0,
                        "Interval": ["3K", "2K", "1K"],
                        "Recovery": None,
                        "Cooldown": "3km",
                        "Distance": 12
                    },
                    "Tempo 2-2-1": {
                        "Warm-Up": "3km",
                        "Reps": 1,
                        "Pace": "2K Hard, 2K Hard, 1K Hard",
                        "PaceOffset": 0,
                        "Interval": ["2K", "2K", "1K"],
                        "Recovery": None,
                        "Cooldown": "3km",
                        "Distance": 11
                    },
                    "Tempo 3K x 2": {
                        "Warm-Up": "3km",
                        "Reps": 2,
                        "Pace": "10k",
                        "PaceOffset": -20,
                        "Interval": "3K",
                        "Recovery": "Walk 120 seconds",
                        "Cooldown": "3km",
                        "Distance": 12
                    },
                    "Tempo + Fast Finish": {
                        "Warm-Up": "3km",
                        "Reps": 1,
                        "Pace": "6K at 10K pace, final 2K at 5K pace",
                        "PaceOffset": 0,
                        "Interval": ["6K", "2K"],
                        "Recovery": None,
                        "Cooldown": "3km",
                        "Distance": 14
                    }

                }

            # Interval/Tempo types for Advanced runners which have a Half-Marathon or Marathon race
            elif level == "Advanced" and race in ["half", "marathon"]:
                interval_types = {
                    "8 x 1km": {
                        "Warm-Up": "2.5km",
                        "Reps": 8,
                        "Pace": "5k",
                        "PaceOffset": 0,
                        "Interval": "1K",
                        "Recovery": "Walk 90 seconds",
                        "Cooldown": "2km",
                        "Distance": 12.5
                    },
                    "Pyramid Intervals": {
                        "Warm-Up": "2km",
                        "Reps": 1,
                        "Pace": "5k",
                        "PaceOffset": 0,
                        "Interval": "400M-800M-1200M-1600M-1200M-800M-400M",
                        "Recovery": "Walk 90 seconds in between",
                        "Cooldown": "2km",
                        "Distance": 10
                    },
                    "5 x mile": {
                        "Warm-Up": "2.5km",
                        "Reps": 5,
                        "Pace": "5k",
                        "PaceOffset": 0,
                        "Interval": "Mile",
                        "Recovery": "Walk 90 seconds",
                        "Cooldown": "2km",
                        "Distance": 12.5
                    },
                    "5 x 2km": {
                        "Warm-Up": "2.5km",
                        "Reps": 5,
                        "Pace": "10k",
                        "PaceOffset": 0,
                        "Interval": "2K",
                        "Recovery": "Walk 180 seconds",
                        "Cooldown": "2.5km",
                        "Distance": 15
                    },
                    "4 x 3km": {
                        "Warm-Up": "2.5km",
                        "Reps": 4,
                        "Pace": "10k",
                        "PaceOffset": 0,
                        "Interval": "3K",
                        "Recovery": "Walk 120 seconds",
                        "Cooldown": "2km",
                        "Distance": 16.5
                    },
                    "2K-3K-4K-3K-2K": {
                        "Warm-Up": "2.5km",
                        "Reps": 1,
                        "Pace": "10k",
                        "PaceOffset": 0,
                        "Interval": "2K-3K-4K-3K-2K",
                        "Recovery": "Walk 120 seconds in between",
                        "Cooldown": "2km",
                        "Distance": 18.5
                    }
                }

                tempo_types = {
                    "Tempo 3K x 5": {
                        "Warm-Up": "2km",
                        "Reps": 5,
                        "Pace": "half",
                        "PaceOffset": 0,
                        "Interval": "3K",
                        "Recovery": "Walk 120 seconds",
                        "Cooldown": "2km",
                        "Distance": 19
                    },
                    "Tempo 5K x 3": {
                        "Warm-Up": "2km",
                        "Reps": 3,
                        "Pace": "half",
                        "PaceOffset": 0,
                        "Interval": "5K",
                        "Recovery": "Walk 120 seconds",
                        "Cooldown": "2km",
                        "Distance": 19
                    },
                    "Tempo 10K x 2": {
                        "Warm-Up": "2km",
                        "Reps": 2,
                        "Pace": "marathon",
                        "PaceOffset": 0,
                        "Interval": "10K",
                        "Recovery": "Walk 120 seconds",
                        "Cooldown": "2km",
                        "Distance": 24
                    },
                    "Continuous Tempo 16K": {
                        "Warm-Up": "2km",
                        "Reps": 1,
                        "Pace": "marathon",
                        "PaceOffset": 0,
                        "Interval": "16K",
                        "Recovery": None,
                        "Cooldown": "2km",
                        "Distance": 20
                    },
                    "Tempo Sandwich": {
                        "Warm-Up": "2km",
                        "Reps": 1,
                        "Pace": "5K Threshold / 3K Marathon / 5K Threshold",
                        "PaceOffset": 0,
                        "Interval": ["5K", "3K", "5K"],
                        "Recovery": None,
                        "Cooldown": "2km",
                        "Distance": 17
                    },
                    "Alternating Tempo 3Ks": {
                        "Warm-Up": "3km",
                        "Reps": 3,
                        "Pace": "(3K Threshold / 1K Marathon pace)",
                        "PaceOffset": 0,
                        "Interval": ["3K", "1K"],
                        "Recovery": None,
                        "Cooldown": "3km",
                        "Distance": 18
                    },
                    "Marathon Progression": {
                        "Warm-Up": "2km",
                        "Reps": 1,
                        "Pace": "Start Easy, Finish at Marathon pace",
                        "PaceOffset": 0,
                        "Interval": ["4K", "4K", "4K", "4K"],
                        "Recovery": None,
                        "Cooldown": "2km",
                        "Distance": 20
                    }

                }

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

                # Created a recovery week every 4 weeks which decrease the load
                recovery_week = False

                if week % 4 == 0:
                    recovery_week = True
                    weekly_miles *= 0.8
                else:
                    weekly_miles *= 1.05

                for day in days:
                    # Default
                    workout = {
                        "type": "Rest"
                    }
                    plan[week_name]["workouts"][day] = workout

                    # Long run
                    if day == long_run_day:

                        # Create a Starting Distance Memory
                        starting_distance = longest_run

                        # What the target long run of the plan will be.
                        target_long_run = race_settings[race]["max_long_run"]

                        # Calculate gradual progression towards target
                        long_run_progress = (target_long_run - starting_distance) / max(plan_length - 1, 1)

                        long_run_distance = (
                                starting_distance +
                                long_run_progress * (week - 1)
                        )

                        # Prevent going over max
                        if long_run_distance > race_settings[race]["max_long_run"]:
                            long_run_distance = race_settings[race]["max_long_run"]

                        if recovery_week:
                            long_run_distance *= 0.8

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

                                # Get Session name and session info from tempo types.
                                session, session_info = random.choice(list(tempo_types.items()))

                                # Get Pace from Session info.
                                pace = session_info["Pace"]

                                # If there is a PaceOffset then get that from session info.
                                if "PaceOffset" in session_info:
                                    paceoffset = session_info["PaceOffset"]

                                    # If the pace is in list of races
                                    if pace in ["5k", "10k", "half", "marathon"]:

                                        # Get that race PB
                                        P = float(data.get(f"{pace}_pb", 2))

                                        # RacePace = Race PB + or - paceoffset
                                        racePace = P + paceoffset

                                        # If race is a 5k divide it by 5 and formatRunPace for the interval pace
                                        if pace == "5k":
                                            new_race_pace = racePace / 5
                                            interval_pace = self.formatRunPace(new_race_pace)
                                            workout_pace = interval_pace

                                        # If race is a 10k divide it by 10 and formatRunPace for the interval pace
                                        elif pace == "10k":
                                            new_race_pace = racePace / 10
                                            interval_pace = self.formatRunPace(new_race_pace)
                                            workout_pace = interval_pace

                                        # If race is a Half-Marathon divide it by 21 and formatRunPace for the interval pace
                                        elif pace == "half":
                                            new_race_pace = racePace / 21
                                            interval_pace = self.formatRunPace(new_race_pace)
                                            workout_pace = interval_pace

                                        # If race is a Marathon divide it by 42 and formatRunPace for the interval pace
                                        elif pace == "marathon":
                                            new_race_pace = racePace / 42
                                            interval_pace = self.formatRunPace(new_race_pace)
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
                                description = self.formatRunDescription(warmup, reps, recovery, workout_pace, interval,
                                                                        cooldown)
                                print(description)


                            else:
                                # Session type is tempo run.
                                hard_type = "Interval Run"

                                # Get Session name and session info from tempo types.
                                session, session_info = random.choice(list(interval_types.items()))

                                pace = session_info["Pace"]

                                if "PaceOffset" in session_info:
                                    paceoffset = session_info["PaceOffset"]

                                    if pace in ["5k", "10k", "half", "marathon"]:
                                        P = float(data.get(f"{pace}_pb", 2))
                                        racePace = P + paceoffset

                                        if pace == "5k":
                                            new_race_pace = racePace / 5
                                            interval_pace = self.formatRunPace(new_race_pace)
                                            workout_pace = interval_pace
                                        elif pace == "10k":
                                            new_race_pace = racePace / 10
                                            interval_pace = self.formatRunPace(new_race_pace)
                                            workout_pace = interval_pace
                                        elif pace == "half":
                                            new_race_pace = racePace / 21
                                            interval_pace = self.formatRunPace(new_race_pace)
                                            workout_pace = interval_pace
                                        elif pace == "marathon":
                                            new_race_pace = racePace / 42
                                            interval_pace = self.formatRunPace(new_race_pace)
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

                                description = self.formatRunDescription(warmup, reps, recovery, workout_pace, interval,
                                                                        cooldown)
                                print(description)

                            # Create nested dict to store everything for the run
                            workout = {
                                "type": hard_type,
                                "session": session,
                                "distance": session_info["Distance"],
                                "pace": workout_pace
                            }
                            plan[week_name]["workouts"][day] = workout

                            current_weekly_distance += session_info["Distance"]

                        # Remaining = easy runs
                        else:
                            easy_distance = (
                                (weekly_miles / len(activity_days))
                            )

                            # Prevent going over max
                            if easy_distance > race_settings[race]["max_easy_run"]:
                                easy_distance = race_settings[race]["max_easy_run"]

                            if recovery_week:
                                easy_distance *= 0.8

                            # Create nested dict to store everything for the run
                            workout = {
                                "type": "Easy Run",
                                "distance": int(easy_distance),
                                "pace": easy_pace
                            }
                            plan[week_name]["workouts"][day] = workout
                            current_weekly_distance += easy_distance

                        # No more than one hard run a week right now.
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
                            plan[week_name]["workouts"][day] = workout
                        if day == "Sunday":
                            workout = {
                                "type": "Race Day!",
                                "distance": race.capitalize(),
                                "pace": race_pace
                            }
                            plan[week_name]["workouts"][day] = workout

                # Reset for next week
                plan[week_name]["distance"] = round(current_weekly_distance)
                weekly_hard_run = 0
                weekly_miles = current_weekly_distance
                current_weekly_distance = 0

            App.get_running_app().data["GeneratedPlan"] = plan

            return plan

        # Format their paces

    def createPredictedTimes(self):
        data = self.data
        pb_5k = float(data.get("5k_pb", 2))
        pb_10k = float(data.get("10k_pb", 2))
        pb_half = float(data.get("half_pb", 2))
        pb_marathon = float(data.get("marathon_pb", 2))
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
                    time_half * (42.195 / 21.0975) * 1.05
                )

                active_pbs["marathon"] = predicted_marathon

        for distance, pb in active_pbs.items():
            active_pbs[distance] = self.format_time(pb)
            App.get_running_app().data[f"{distance}_pb"] = pb
            App.get_running_app().data[f"prediction_{distance}"] = self.format_time(pb)

        return print(active_pbs)

    def formatRunPace(self, PB):

        # Turn seconds into minutes and seconds rounded to the nearest division of 5.
        minutes = int(PB // 60)
        seconds = 5 * int(round((PB % 60) / 5))

        # Return the formated string.
        return f"{minutes}:{seconds:02d}/km"

    def format_time(self, seconds):
        seconds = int(seconds)

        hours = seconds // 3600
        minutes = (seconds % 3600) // 60

        return f"{hours:02d}:{minutes:02d}:00"

        # Format the run Description.

    def formatRunDescription(self, warmup, reps, recovery, pace, interval, cooldown):

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
