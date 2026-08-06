import random
from asyncio.windows_events import NULL

from docutils.nodes import description
from kivy.graphics import Color, RoundedRectangle, Line
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from kivy.uix.togglebutton import ToggleButton

from kivy.app import App
from Theme import *

class PlanPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # setup Kivy screen

        # Scroll area
        self.scroll = ScrollView()

        self.content = BoxLayout(
            orientation='vertical',
            spacing=30,
            padding=25,
            size_hint_y=None
        )

        self.content.bind(
            minimum_height=self.content.setter('height')
        )
        self.scroll.add_widget(self.content)

        self.add_widget(self.scroll)


    def on_enter(self):

        self.content.clear_widgets()

        data = App.get_running_app().data
        race = data.get("race")
        plan_length = int(data.get("CurrentPlanLength", 0))
        PB = float(data.get(f"{race}_pb", 2))
        longest_run = int(data.get("Longest_Run"))
        weekly_miles = int(data.get("Weekly_Distance"))
        activity_days = data.get("ActivityDays")
        long_run_day = data.get("LongActivityDay")
        level = data.get("Level")
        weekly_hard_run = 0

        #Days in the week
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


        runlst = ["5k", "10k", "half", "marathon"]
        ridelst = ["cycle_20", "cycle_50", "cycle_100", "cycle_160"]
        swimlst = ["swim_400", "swim_1500", "swim_3000", "swim_5000"]

        if race not in runlst:
            return

            # Make sure the activity days exist
        if not activity_days:
            return


        if race in runlst:

            #Variable settings that change for each race.

            if race == "5k":
                raceDistance = 5

                # Work out what their race pace based off their last PB
                predictedPace = PB - plan_length * 10
                race_pace = predictedPace / 5

                # Create different paces for different runs.
                easy_pace = self.formatRunPace(race_pace + 120)
                tempo_pace = self.formatRunPace(race_pace)


            elif race == "10k":
                # if user has not run that far it will get the PB that they have,
                # not run a half-marathon yet so they will use their 10k PB for reference.
                raceDistance = 10

                if PB == 2.0:
                    PB = float(data.get("5k_pb", 2))
                    race_pace = PB / 5

                else:
                    # Work out what their race pace based off their last PB
                    predictedPace = PB - plan_length * 15
                    race_pace = predictedPace/ 10

                    # Create different paces for different runs.
                    easy_pace = self.formatRunPace(race_pace + 105)
                    tempo_pace = self.formatRunPace(race_pace)

            elif race == "half":
                raceDistance = 21.1
                if PB == 2.0:
                    PB = float(data.get("10k_pb", 2))
                    race_pace = PB / 10
                else:
                    # Work out what their race pace based off their last PB
                    predictedPace = PB - plan_length * 20
                    race_pace = predictedPace / 21.1

                    # Create different paces for different runs.
                    easy_pace = self.formatRunPace(race_pace + 90)
                    tempo_pace = self.formatRunPace(race_pace)

            elif race == "marathon":
                raceDistance = 42.2
                if PB == 2.0:
                    PB = float(data.get("half_pb", 2))
                    race_pace = PB / 21.1
                else:
                    # Work out what their race pace based off their last PB
                    predictedPace = PB - plan_length * 25
                    race_pace = predictedPace / 42.2

                    # Create different paces for different runs.
                    easy_pace = self.formatRunPace(race_pace + 75)
                    tempo_pace = self.formatRunPace(race_pace)

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
                        "max_long_run": 14,
                        "max_easy_run": 8,
                        "speed": "semi-fast"

                    },
                    "half": {
                        "max_long_run": 23,
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
                        "Interval": ["1K","1K"],
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
                        "Interval": ["2K","1K"],
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
                        "Cooldown": "2km",
                        "Distance": 20
                    }

                }

            #Dictionary for the plan.
            plan = {}
            current_weekly_distance = 0

            # For week in range 1 to the length of the current plan
            for week in range(1, plan_length + 1):
                week_name = f"Week {week}"

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
                        distance_to_cover = (
                                race_settings[race]["max_long_run"] - longest_run
                        )

                        weekly_increase = (
                                distance_to_cover / max(plan_length - 2, 1)
                        )

                        long_run_distance = (
                                longest_run +
                                (weekly_increase * week)
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

                                description = self.formatRunDescription(warmup, reps, recovery, workout_pace, interval, cooldown)
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
                                "pace": tempo_pace
                            }
                            plan[week_name]["workouts"][day] = workout
                        if day == "Sunday":
                            workout = {
                                "type": "Race Day!",
                                "distance": race.capitalize(),
                                "pace": self.formatRunPace(race_pace)
                            }
                            plan[week_name]["workouts"][day] = workout

                # Reset for next week
                plan[week_name]["distance"] = round(current_weekly_distance)
                weekly_hard_run = 0
                weekly_miles = current_weekly_distance
                current_weekly_distance = 0

            App.get_running_app().data["GeneratedPlan"] = plan

            # Get Week and workout in that week
            for week, week_data in plan.items():

                workouts = week_data["workouts"]
                weekly_distance = week_data["distance"]

                # Initialize Card
                card = BoxLayout(
                    orientation='vertical',
                    spacing=15,
                    padding=20,
                    size_hint_y=None
                )

                # Dynamic height
                card.bind(minimum_height=card.setter("height"))

                # Card background
                with card.canvas.before:
                    Color(*CARD)
                    card.rect = RoundedRectangle(
                        pos=card.pos,
                        size=card.size,
                        radius=[25]
                    )

                # Keep card updated
                def update_rect(instance, value):
                    instance.rect.pos = instance.pos
                    instance.rect.size = instance.size

                # Bind Card with updated variables
                card.bind(pos=update_rect, size=update_rect)

                header = BoxLayout(
                    orientation="vertical",
                    size_hint_y=None,
                    height=70,
                    spacing=5
                )

                week_label = Label(
                    text=week,
                    font_size=32,
                    bold=True,
                    color=TEXT,
                    size_hint_y=None,
                    height=40
                )

                distance_label = Label(
                    text=f"{weekly_distance} km planned",
                    font_size=18,
                    color=SUBTEXT,
                    size_hint_y=None,
                    height=25
                )

                header.add_widget(week_label)
                header.add_widget(distance_label)

                card.add_widget(header)

                # Get the day and workout in workouts
                for day, workout in workouts.items():

                    # Skip rest days as these don't need to be displayed in the plan section
                    if workout["type"] == "Rest":
                        continue

                    # Get all Workout info
                    workout_text = f"[b]{day}[/b]\n"
                    workout_text += f"{workout['type']}\n"

                    if "session" in workout:
                        workout_text += f"Session: {workout['session']}\n"

                    if "distance" in workout:
                        workout_text += f"Distance: {workout['distance']}\n"

                    if "pace" in workout:
                        workout_text += f"Pace: {workout['pace']}"

                    # Workout Card
                    colour = {
                        "Easy Run": EASY,
                        "Recovery Run": EASY,
                        "Long Run": LONG,
                        "Interval Run": INTERVAL,
                        "Tempo Run": TEMPO,
                        "Race Practice Session!": TEMPO,
                        "Race Day!": RACE,
                    }.get(workout["type"], SUBTEXT)

                    workout_card = BoxLayout(
                        orientation='vertical',
                        padding=20,
                        spacing = 8,
                        size_hint_y=None,
                        height=140,
                    )

                    # Workout card background
                    with workout_card.canvas.before:

                        Color(*CARD)
                        workout_card.rect = RoundedRectangle(
                            pos=workout_card.pos,
                            size=workout_card.size,
                            radius=[24]
                        )
                        # Border
                        Color(*colour)
                        workout_card.border = Line(
                            rounded_rectangle=(
                                workout_card.x,
                                workout_card.y,
                                workout_card.width,
                                workout_card.height,
                                24
                            ),
                            width=2
                        )

                    # Keep Workout Updated
                    def update_workout_rect(instance, value):
                        instance.rect.pos = instance.pos
                        instance.rect.size = instance.size

                        instance.border.rounded_rectangle = (
                            instance.x,
                            instance.y,
                            instance.width,
                            instance.height,
                            24
                        )

                    # Bind Card with updated variables
                    workout_card.bind(
                        pos=update_workout_rect,
                        size=update_workout_rect
                    )

                    # Day workouts
                    day_label = Label(
                        text=workout_text,
                        markup=True,
                        font_size=18,
                        color=TEXT,
                        halign="left",
                        valign="middle",
                        text_size=(650, None)
                    )
                    # Add day and workout to workout card
                    workout_card.add_widget(day_label)

                    # Add workout card to week card.
                    card.add_widget(workout_card)

                # Add whole week card
                self.content.add_widget(card)

    def restart(self, instance):

        self.manager.current = "intro"
        self.data = {}

        # Format their paces
    def formatRunPace(self, PB):

        # Turn seconds into minutes and seconds rounded to the nearest division of 5.
        minutes = int(PB // 60)
        seconds = 5 * int(round((PB % 60) / 5))

        # Return the formated string.
        return f"{minutes}:{seconds:02d}/km"


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






