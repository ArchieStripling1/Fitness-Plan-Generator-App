class RaceSettingsData:

    distance_smaller = {
        "5k": {
            "max_long_run": 5,
            "max_easy_run": 3,
        },
        "10k": {
            "max_long_run": 10,
            "max_easy_run": 6,
        },
        "half": {
            "max_long_run": 20,
            "max_easy_run": 8,
        },
        "marathon": {
            "max_long_run": 34,
            "max_easy_run": 10,
        }
    }
    distance_greater = {
        "5k": {
            "distance": 6,
            "max_long_run": 12,
            "max_easy_run": 6,
        },
        "10k": {
            "distance": 9,
            "max_long_run": 16,
            "max_easy_run": 8,
        },
        "half": {
            "distance": 18,
            "max_long_run": 22,
            "min_long_run": 16,
            "max_easy_run": 13,
        },
        "marathon": {
            "distance": 34,
            "max_long_run": 34,
            "min_long_run": 25,
            "max_easy_run": 16,
        }
    }
