class LongRunData:

    # Long runs types for novice level
    novice_long_run_types = {

        "easy_long_run": {
            "description": "Entire run at easy conversational effort.",
            "easy_portion": 1.0,
            "quality_portion": 0.0,
            "quality_type": None,
            "phase": "base",
        },

        "easy_steady_finish": {
            "description": "Mostly easy running with a controlled steady finish.",
            "easy_portion": 0.80,
            "quality_portion": 0.20,
            "quality_type": "steady",
            "phase": "base"
        },

        "easy_10k_finish": {
            "description": "Easy long run finishing with a short controlled 10K-effort section.",
            "easy_portion": 0.75,
            "quality_portion": 0.25,
            "quality_type": "10k",
            "phase": "build"
        },

        "progression_long_run": {
            "description": "Gradually increases from easy to steady/moderate effort.",
            "stages": [
                {"portion": 0.60, "pace": "easy"},
                {"portion": 0.25, "pace": "steady"},
                {"portion": 0.15, "pace": "moderate"},
            ],
            "quality_type": "progression",
            "phase": "build"
        },

        "fast_finish": {
            "description": "Easy long run with a short faster finish.",
            "easy_portion": 0.80,
            "quality_portion": 0.20,
            "quality_type": "fast_finish",
            "phase": "build"
        },

        "steady_finish": {
            "description": "Easy running followed by a longer steady finish.",
            "easy_portion": 0.70,
            "quality_portion": 0.30,
            "quality_type": "steady",
            "phase": "build"
        },

        "race_practice_long_run": {
            "description": "Long run containing a short race-specific practice section.",
            "easy_portion": 0.80,
            "quality_portion": 0.20,
            "quality_type": "race_pace",
            "phase": "peak"
        },

        "easy_with_strides": {
            "description": "Easy long run with short relaxed strides near the end.",
            "easy_portion": 0.95,
            "quality_portion": 0.05,
            "quality_type": "strides",
            "phase": "base"
        },

        "cutback_long_run": {
            "description": "Reduced-volume easy long run for recovery weeks.",
            "easy_portion": 1.0,
            "quality_portion": 0.0,
            "quality_type": None,
            "phase": "recovery"
        },

        "taper_long_run": {
            "description": "Short easy long run during taper.",
            "easy_portion": 1.0,
            "quality_portion": 0.0,
            "quality_type": None,
            "phase": "taper"
        }
    }

    # Long runs types for intermediate level
    intermediate_long_run_types = {

        "easy_long_run": {
            "description": "Entire run at easy aerobic effort.",
            "easy_portion": 1.0,
            "quality_portion": 0.0,
            "quality_type": None,
            "phase": "base"
        },

        "easy_with_strides": {
            "description": "Easy aerobic long run with relaxed strides at the end.",
            "easy_portion": 0.95,
            "quality_portion": 0.05,
            "quality_type": "strides",
            "phase": "base"
        },

        "easy_steady": {
            "description": "Easy opening followed by a controlled steady section.",
            "easy_portion": 0.65,
            "quality_portion": 0.35,
            "quality_type": "steady",
            "phase": "base"
        },

        "easy_tempo": {
            "description": "Long easy run containing a controlled tempo section.",
            "easy_portion": 0.65,
            "quality_portion": 0.35,
            "quality_type": "tempo",
            "phase": "build"
        },

        "easy_race_pace": {
            "description": "Easy long run with a race-specific pace block.",
            "easy_portion": 0.70,
            "quality_portion": 0.30,
            "quality_type": "race_pace",
            "phase": "build"
        },

        "progression": {
            "description": "Progresses through several controlled effort levels.",
            "stages": [
                {"portion": 0.50, "pace": "easy"},
                {"portion": 0.25, "pace": "steady"},
                {"portion": 0.15, "pace": "tempo"},
                {"portion": 0.10, "pace": "race_pace"},
            ],
            "quality_type": "progression",
            "phase": "build"
        },

        "fast_finish": {
            "description": "Easy long run with a stronger final section.",
            "easy_portion": 0.75,
            "quality_portion": 0.25,
            "quality_type": "fast_finish",
            "phase": "build"
        },

        "easy_steady_easy": {
            "description": "Easy running, steady middle section, then easy running.",
            "stages": [
                {"portion": 0.35, "pace": "easy"},
                {"portion": 0.30, "pace": "steady"},
                {"portion": 0.35, "pace": "easy"},
            ],
            "quality_type": "steady",
            "phase": "build"
        },

        "alternating_pace": {
            "description": "Alternates controlled faster running with easy running.",
            "stages": [
                {"portion": 0.20, "pace": "easy"},
                {"portion": 0.10, "pace": "race_pace"},
                {"portion": 0.10, "pace": "easy"},
                {"portion": 0.10, "pace": "race_pace"},
                {"portion": 0.10, "pace": "easy"},
                {"portion": 0.10, "pace": "race_pace"},
                {"portion": 0.30, "pace": "easy"},
            ],
            "quality_type": "alternating",
            "phase": "peak"
        },

        "race_pace_blocks": {
            "description": "Easy long run containing repeated race-pace blocks.",
            "easy_portion": 0.70,
            "quality_portion": 0.30,
            "quality_type": "race_pace_blocks",
            "blocks": {
                "block_count": 3,
                "block_portion": 0.10,
                "recovery_between": "easy",
            },
            "phase": "peak"
        },

        "tempo_blocks": {
            "description": "Long run with controlled tempo blocks separated by easy running.",
            "stages": [
                {"portion": 0.25, "pace": "easy"},
                {"portion": 0.15, "pace": "tempo"},
                {"portion": 0.10, "pace": "easy"},
                {"portion": 0.15, "pace": "tempo"},
                {"portion": 0.35, "pace": "easy"},
            ],
            "quality_type": "tempo_blocks",
            "phase": "peak"
        },

        "race_practice_long_run": {
            "description": "Long race-specific session used close to the goal race.",
            "easy_portion": 0.75,
            "quality_portion": 0.25,
            "quality_type": "race_pace",
            "phase": "peak"
        },

        "cutback_long_run": {
            "description": "Reduced easy long run for a recovery week.",
            "easy_portion": 1.0,
            "quality_portion": 0.0,
            "quality_type": None,
            "phase": "recovery"
        },

        "taper_long_run": {
            "description": "Reduced easy long run during taper.",
            "easy_portion": 1.0,
            "quality_portion": 0.0,
            "quality_type": None,
            "phase": "taper"
        }
    }

    # Long runs types for Advanced level
    advanced_long_run_types = {

        "easy_long_run": {
            "description": "Easy aerobic long run used to absorb training.",
            "easy_portion": 1.0,
            "quality_portion": 0.0,
            "quality_type": None,
            "phase": "base"
        },

        "steady_middle": {
            "description": "Easy opening, sustained steady middle, easy finish.",
            "stages": [
                {"portion": 0.30, "pace": "easy"},
                {"portion": 0.40, "pace": "steady"},
                {"portion": 0.30, "pace": "easy"},
            ],
            "quality_type": "steady",
            "phase": "base"
        },

        "easy_marathon_pace_easy": {
            "description": "Easy running, sustained marathon pace, then easy running.",
            "stages": [
                {"portion": 0.40, "pace": "easy"},
                {"portion": 0.40, "pace": "marathon"},
                {"portion": 0.20, "pace": "easy"},
            ],
            "quality_type": "marathon",
            "phase": "build"
        },

        "easy_threshold_easy": {
            "description": "Easy running surrounding a controlled threshold section.",
            "stages": [
                {"portion": 0.40, "pace": "easy"},
                {"portion": 0.20, "pace": "threshold"},
                {"portion": 0.40, "pace": "easy"},
            ],
            "quality_type": "threshold",
            "phase": "build"
        },

        "3_stage_progression": {
            "description": "Three-stage progression from easy through steady to race-specific effort.",
            "stages": [
                {"portion": 0.50, "pace": "easy"},
                {"portion": 0.25, "pace": "steady"},
                {"portion": 0.25, "pace": "race_pace"},
            ],
            "quality_type": "progression",
            "phase": "build"
        },

        "surge_long_run": {
            "description": "Mostly easy long run containing short controlled surges.",
            "stages": [
                {"portion": 0.25, "pace": "easy"},
                {"portion": 0.05, "pace": "surge"},
                {"portion": 0.15, "pace": "easy"},
                {"portion": 0.05, "pace": "surge"},
                {"portion": 0.15, "pace": "easy"},
                {"portion": 0.05, "pace": "surge"},
                {"portion": 0.30, "pace": "easy"},
            ],
            "quality_type": "surges",
            "phase": "build"
        },

        "fast_finish": {
            "description": "Easy aerobic running followed by a strong controlled finish.",
            "easy_portion": 0.75,
            "quality_portion": 0.25,
            "quality_type": "fast_finish",
            "phase": "build"
        },

        "alternating_pace": {
            "description": "Repeated changes between race-specific and easy running.",
            "stages": [
                {"portion": 0.20, "pace": "easy"},
                {"portion": 0.10, "pace": "race_pace"},
                {"portion": 0.10, "pace": "easy"},
                {"portion": 0.10, "pace": "race_pace"},
                {"portion": 0.10, "pace": "easy"},
                {"portion": 0.10, "pace": "race_pace"},
                {"portion": 0.30, "pace": "easy"},
            ],
            "quality_type": "alternating",
            "phase": "peak"
        },

        "race_pace_blocks": {
            "description": "Long run built around repeated race-pace blocks.",
            "stages": [
                {"portion": 0.25, "pace": "easy"},
                {"portion": 0.10, "pace": "race_pace"},
                {"portion": 0.10, "pace": "easy"},
                {"portion": 0.10, "pace": "race_pace"},
                {"portion": 0.10, "pace": "easy"},
                {"portion": 0.10, "pace": "race_pace"},
                {"portion": 0.25, "pace": "easy"},
            ],
            "quality_type": "race_pace_blocks",
            "phase": "peak"
        },

        "marathon_progression": {
            "description": "Progressive long run finishing around marathon pace.",
            "stages": [
                {"portion": 0.35, "pace": "easy"},
                {"portion": 0.25, "pace": "steady"},
                {"portion": 0.20, "pace": "marathon"},
                {"portion": 0.20, "pace": "marathon"},
            ],
            "quality_type": "marathon_progression",
            "phase": "peak"
        },

        "half_marathon_specific": {
            "description": "Long run with sustained half-marathon-specific work.",
            "stages": [
                {"portion": 0.35, "pace": "easy"},
                {"portion": 0.20, "pace": "steady"},
                {"portion": 0.15, "pace": "half"},
                {"portion": 0.15, "pace": "easy"},
                {"portion": 0.15, "pace": "half"},
            ],
            "quality_type": "half",
            "phase": "peak"
        },

        "10k_specific": {
            "description": "Long run containing controlled 10K-specific sections.",
            "stages": [
                {"portion": 0.45, "pace": "easy"},
                {"portion": 0.15, "pace": "10k"},
                {"portion": 0.10, "pace": "easy"},
                {"portion": 0.15, "pace": "10k"},
                {"portion": 0.15, "pace": "easy"},
            ],
            "quality_type": "10k",
            "phase": "peak"
        },

        "tempo_blocks": {
            "description": "Multiple controlled threshold/tempo blocks inside a long run.",
            "stages": [
                {"portion": 0.25, "pace": "easy"},
                {"portion": 0.15, "pace": "tempo"},
                {"portion": 0.10, "pace": "easy"},
                {"portion": 0.15, "pace": "tempo"},
                {"portion": 0.10, "pace": "easy"},
                {"portion": 0.10, "pace": "tempo"},
                {"portion": 0.15, "pace": "easy"},
            ],
            "quality_type": "tempo_blocks",
            "phase": "peak"
        },

        "practice_race_long_run": {
            "description": "Race simulation or controlled race-practice session.",
            "stages": [
                {"portion": 0.35, "pace": "easy"},
                {"portion": 0.30, "pace": "race_pace"},
                {"portion": 0.10, "pace": "easy"},
                {"portion": 0.25, "pace": "race_pace"},
            ],
            "quality_type": "race_practice",
            "phase": "peak"
        },

        "cutback_long_run": {
            "description": "Reduced-volume easy long run for recovery.",
            "easy_portion": 1.0,
            "quality_portion": 0.0,
            "quality_type": None,
            "phase": "recovery"
        },

        "taper_long_run": {
            "description": "Reduced easy long run during taper.",
            "easy_portion": 1.0,
            "quality_portion": 0.0,
            "quality_type": None,
            "phase": "taper"
        }
    }
