

class SpeedWorkoutData:


    Beginner_Interval_Types = {
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
    Beginner_Tempo_Types = {
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

    Intermediate_Short_Interval_Types = {
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
    Intermediate_Short_Tempo_Types = {
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

    Intermediate_Long_Interval_Types = {
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
    Intermediate_Long_Tempo_Types = {
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

    Advanced_Short_Interval_Types = {
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
    Advanced_Short_Tempo_Types = {
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

    Advanced_Long_Interval_Types = {
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
    Advanced_Long_Tempo_Types = {
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