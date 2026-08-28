from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from kivy.uix.togglebutton import ToggleButton
from Dev.UI.Screens.RaceScreen import selected
from Dev.UI.Theme import TEXT, PRIMARY, SUBTEXT
from kivy.graphics import Color, RoundedRectangle
from kivy.metrics import dp


class RunningScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation='vertical',
            padding=[dp(35), dp(25), dp(35), dp(25)],
            spacing=dp(15)
        )

        # Header
        title = Label(
            text="Running Profile",
            font_size=36,
            size_hint=(1, None),
            height=dp(50),
            bold=True,
            color=TEXT
        )

        subtitle = Label(
            text="Tell us about your current running",
            font_size=17,
            size_hint=(1, None),
            height=dp(30),
            color=SUBTEXT
        )

        layout.add_widget(title)
        layout.add_widget(subtitle)

        # Longest Run
        longest_box = BoxLayout(
            orientation='vertical',
            spacing=dp(8),
            padding=[dp(20), dp(15), dp(20), dp(15)],
            size_hint=(1, None),
            height=dp(145)
        )

        with longest_box.canvas.before:
            Color(0.12, 0.15, 0.23, 1)
            longest_background = RoundedRectangle(
                pos=longest_box.pos,
                size=longest_box.size,
                radius=[dp(15)]
            )

        longest_box.bind(
            pos=lambda instance, value:
            setattr(longest_background, 'pos', value),
            size=lambda instance, value:
            setattr(longest_background, 'size', value)
        )

        longest_label = Label(
            text="Longest Recent Run (km)",
            font_size=15,
            color=SUBTEXT,
            bold=True,
            size_hint_y=None,
            height=dp(25)
        )

        self.longest_value = Label(
            text="1 km",
            font_size=27,
            color=TEXT,
            bold=True,
            size_hint_y=None,
            height=dp(38)
        )

        # Slider
        self.longest_slider = Slider(min=1, max=60, value=1, step=1)
        self.longest_slider.bind(value=self.update_longest)

        longest_box.add_widget(longest_label)
        longest_box.add_widget(self.longest_value)
        longest_box.add_widget(self.longest_slider)

        layout.add_widget(longest_box)

        # Weekly Distance
        weekly_box = BoxLayout(
            orientation='vertical',
            spacing=dp(8),
            padding=[dp(20), dp(15), dp(20), dp(15)],
            size_hint=(1, None),
            height=dp(145)
        )

        with weekly_box.canvas.before:
            Color(0.12, 0.15, 0.23, 1)
            weekly_background = RoundedRectangle(
                pos=weekly_box.pos,
                size=weekly_box.size,
                radius=[dp(15)]
            )

        weekly_box.bind(
            pos=lambda instance, value:
            setattr(weekly_background, 'pos', value),
            size=lambda instance, value:
            setattr(weekly_background, 'size', value)
        )

        weekly_label = Label(
            text="Current Weekly Distance (km)",
            font_size=15,
            color=SUBTEXT,
            bold=True,
            size_hint_y=None,
            height=dp(25)
        )

        self.weekly_value = Label(
            text="1 km",
            font_size=27,
            color=TEXT,
            bold=True,
            size_hint_y=None,
            height=dp(38)
        )

        # Slider
        self.weekly_slider = Slider(min=1, max=150, value=1, step=1)
        self.weekly_slider.bind(value=self.update_weekly)

        weekly_box.add_widget(weekly_label)
        weekly_box.add_widget(self.weekly_value)
        weekly_box.add_widget(self.weekly_slider)

        layout.add_widget(weekly_box)

        # ERROR MESSAGE
        self.error_label = Label(
            text="",
            font_size=16,
            color=(1, 0.3, 0.3, 1),
            size_hint_y=None,
            height=dp(35)
        )

        layout.add_widget(self.error_label)

        # Buttons
        btn_box = BoxLayout(
            size_hint=(1, None),
            height=dp(55),
            spacing=dp(15)
        )

        back_btn = Button(
            text="Previous",
            font_size=19,
            background_normal="",
            background_color=(0, 0, 0, 0),
            color=TEXT,
            bold=True
        )

        with back_btn.canvas.before:
            Color(0.15, 0.18, 0.27, 1)
            back_background = RoundedRectangle(
                pos=back_btn.pos,
                size=back_btn.size,
                radius=[dp(12)]
            )

        back_btn.bind(
            pos=lambda instance, value:
            setattr(back_background, 'pos', value),
            size=lambda instance, value:
            setattr(back_background, 'size', value)
        )

        next_btn = Button(
            text="Next",
            font_size=19,
            background_normal="",
            background_color=(0, 0, 0, 0),
            color=TEXT,
            bold=True
        )

        with next_btn.canvas.before:
            Color(*PRIMARY)
            next_background = RoundedRectangle(
                pos=next_btn.pos,
                size=next_btn.size,
                radius=[dp(12)]
            )

        next_btn.bind(
            pos=lambda instance, value:
            setattr(next_background, 'pos', value),
            size=lambda instance, value:
            setattr(next_background, 'size', value)
        )

        back_btn.bind(on_press=self.go_back)
        next_btn.bind(on_press=self.go_next)

        btn_box.add_widget(back_btn)
        btn_box.add_widget(next_btn)

        layout.add_widget(btn_box)

        self.add_widget(layout)

    # Update Slider Value
    def update_longest(self, instance, value):
        longest_distance = int(value)

        self.longest_value.text = f"{longest_distance} km"

        self.validate_distances()

    # Update Slider Value
    def update_weekly(self, instance, value):
        weekly_distance = int(value)

        self.weekly_value.text = f"{weekly_distance} km"

        self.validate_distances()

    def validate_distances(self):

        longest_distance = int(
            self.longest_slider.value
        )

        weekly_distance = int(
            self.weekly_slider.value
        )

        if weekly_distance < longest_distance:
            self.error_label.text = (
                "Weekly distance cannot be lower "
                "than your longest run."
            )

            return False

        self.error_label.text = ""

        return True

    def go_next(self, instance):
        longestDistance = int(self.longest_slider.value)
        weeklyDistance = int(self.weekly_slider.value)

        # Prevent invalid data
        if not self.validate_distances():
            return

        App.get_running_app().data["Longest_Run"] = longestDistance
        App.get_running_app().data["Weekly_Distance"] = weeklyDistance

        if longestDistance < 5:
            self.error_label.text = (
                "Your longest run should be at least 5 km."
            )

            return
        if 5 <= longestDistance < 10:
            self.manager.current = "RunningTime5k"
        elif 10 <= longestDistance < 21:
            self.manager.current = "RunningTime10k"
        elif 21 <= longestDistance < 42:
            self.manager.current = "RunningTimeHalf"
        elif longestDistance >= 42:
            self.manager.current = "RunningTimeMarathon"

    def go_back(self, instance):
        self.manager.current = "race"


class RunningTimeScreen(Screen):
    def __init__(self, distance, **kwargs):
        super().__init__(**kwargs)

        # reachable dictionary of PBs for distances
        self.inputs = {}
        layout = BoxLayout(
            orientation='vertical',
            padding=[dp(35), dp(25), dp(35), dp(25)],
            spacing=dp(15)
        )
        title = Label(
            text="Personal Bests",
            font_size=36,
            size_hint=(1, None),
            height=dp(50),
            bold=True,
            color=TEXT
        )

        subtitle = Label(
            text="Enter your best recent race times",
            font_size=17,
            size_hint=(1, None),
            height=dp(30),
            color=SUBTEXT
        )

        layout.add_widget(title)
        layout.add_widget(subtitle)

        # Create list of all the PBs they
        # will have depending on their furthest run.
        lst = []
        if distance == "Marathon":
            lst = ["marathon", "half", "10k", "5k"]
        elif distance == "Half-Marathon":
            lst = ["half", "10k", "5k"]
        elif distance == "10K":
            lst = ["10k", "5k"]
        elif distance == "5K":
            lst = ["5k"]

        for dist in lst:
            # Enter Longest Distance Time
            pb_box = BoxLayout(
                orientation='vertical',
                spacing=dp(8),
                padding=[dp(20), dp(12), dp(20), dp(12)],
                size_hint=(1, None),
                height=dp(105)
            )

            with pb_box.canvas.before:
                Color(0.12, 0.15, 0.23, 1)
                pb_background = RoundedRectangle(
                    pos=pb_box.pos,
                    size=pb_box.size,
                    radius=[dp(15)]
                )

            pb_box.bind(
                pos=lambda instance, value, bg=pb_background:
                setattr(bg, 'pos', value),
                size=lambda instance, value, bg=pb_background:
                setattr(bg, 'size', value)
            )

            title = Label(
                text=f"{dist.upper()} PERSONAL BEST",
                font_size=15,
                color=SUBTEXT,
                bold=True,
                size_hint_y=None,
                height=dp(25),
                halign="left"
            )

            title.bind(
                size=lambda instance, value:
                setattr(instance, 'text_size', value)
            )

            pb_input = TextInput(
                hint_text="HH:MM:SS",
                font_size=21,
                height=dp(45),
                size_hint=(1, None),
                multiline=False,
                padding=[dp(12), dp(8)],
                background_normal="",
                background_color=(0.08, 0.10, 0.16, 1),
                foreground_color=TEXT,
                hint_text_color=SUBTEXT
            )

            self.inputs[dist] = pb_input

            pb_box.add_widget(title)
            pb_box.add_widget(pb_input)

            layout.add_widget(pb_box)

            # ERROR MESSAGE
            self.error_label = Label(
                text="",
                font_size=18,
                color=(1, 0.3, 0.3, 1),
                size_hint_y=None,
                height=30
            )

            layout.add_widget(self.error_label)

        # Buttons

        btn_box = BoxLayout(
            size_hint=(1, None),
            height=dp(55),
            spacing=dp(15)
        )

        back_btn = Button(
            text="Previous",
            font_size=19,
            background_normal="",
            background_color=(0, 0, 0, 0),
            color=TEXT,
            bold=True
        )

        with back_btn.canvas.before:
            Color(0.15, 0.18, 0.27, 1)
            back_background = RoundedRectangle(
                pos=back_btn.pos,
                size=back_btn.size,
                radius=[dp(12)]
            )

        back_btn.bind(
            pos=lambda instance, value:
            setattr(back_background, 'pos', value),
            size=lambda instance, value:
            setattr(back_background, 'size', value)
        )

        next_btn = Button(
            text="Continue",
            font_size=19,
            background_normal="",
            background_color=(0, 0, 0, 0),
            color=TEXT,
            bold=True
        )

        with next_btn.canvas.before:
            Color(*PRIMARY)
            next_background = RoundedRectangle(
                pos=next_btn.pos,
                size=next_btn.size,
                radius=[dp(12)]
            )

        next_btn.bind(
            pos=lambda instance, value:
            setattr(next_background, 'pos', value),
            size=lambda instance, value:
            setattr(next_background, 'size', value)
        )

        back_btn.bind(on_press=self.go_back)
        next_btn.bind(on_press=self.go_next)

        btn_box.add_widget(back_btn)
        btn_box.add_widget(next_btn)

        layout.add_widget(btn_box)

        self.add_widget(layout)

    def validate_PBs(self):

        self.error_label.text = ""

        pb_times = {}

        # Validate format
        for dist, pb_input in self.inputs.items():

            text = pb_input.text.strip()

            # No blank entries
            if not text:
                self.error_label.text = (
                    f"Please enter a {dist.upper()} time.\n"
                    "Please use HH:MM:SS."
                )
                return False

            total_seconds = self.convert_time_to_seconds(text)

            if total_seconds is None:
                self.error_label.text = (
                    f"Invalid {dist.upper()} time.\n"
                    "Please use HH:MM:SS."
                )
                return False

            pb_times[dist] = total_seconds

        # Check PB consistency
        if "5k" in pb_times and "10k" in pb_times:
            if pb_times["10k"] <= pb_times["5k"]:
                self.error_label.text = (
                    "Your 10K PB must be longer than your 5K PB."
                )
                return False

        if "10k" in pb_times and "half" in pb_times:
            if pb_times["half"] <= pb_times["10k"]:
                self.error_label.text = (
                    "Your Half Marathon PB must be longer than your 10K PB."
                )
                return False

        if "half" in pb_times and "marathon" in pb_times:
            if pb_times["marathon"] <= pb_times["half"]:
                self.error_label.text = (
                    "Your Marathon PB must be longer"
                    " than your Half Marathon PB."
                )
                return False

        return True

    def convert_time_to_seconds(self, text):

        try:

            parts = text.strip().split(":")

            if len(parts) != 3:

                return None

            hours = int(parts[0])
            minutes = int(parts[1])
            seconds = int(parts[2])

            if minutes >= 60 or seconds >= 60:

                return None

            total_seconds = (
                hours * 3600
                + minutes * 60
                + seconds
            )

            return total_seconds

        except ValueError:

            return None

    # SAVE TIMES

    def save_inputs(self):

        data = App.get_running_app().data

        for dist, pb_input in self.inputs.items():

            text = pb_input.text.strip()

            if not text:

                continue

            total_seconds = (
                self.convert_time_to_seconds(text)
            )

            if total_seconds is None:

                print(
                    f"Invalid time entered for {dist}"
                )

                continue

            data[f"{dist}_pb"] = total_seconds

            print(
                f"{dist}: {total_seconds} seconds"
            )

    def go_next(self, instance):

        # Validate all PB's
        if not self.validate_PBs():
            return

        # Save all inputs when Next is pressed
        self.save_inputs()

        self.manager.current = "level"

    def go_back(self, instance):
        self.manager.current = "race"


class LevelScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.selected_level = None
        self.level_buttons = {}

        layout = BoxLayout(
            orientation='vertical',
            padding=[dp(35), dp(25), dp(35), dp(25)],
            spacing=dp(15)
        )

        title = Label(
            text="What Level Runner are you?",
            font_size=36,
            size_hint=(1, None),
            height=dp(55),
            bold=True,
            color=TEXT
        )
        subtitle = Label(
            text="Choose the level that best describes your experience",
            font_size=15,
            size_hint=(1, None),
            height=dp(35),
            color=TEXT
        )

        layout.add_widget(title)
        layout.add_widget(subtitle)

        content = BoxLayout(
            orientation="vertical",
            spacing=dp(12),
            size_hint_y=None
        )

        content.bind(
            minimum_height=content.setter("height")
        )

        level_descriptions = {
            "Beginner": (
                "A runner who is new to structured training, "
                "has not consistently run beyond 5km,"
                "and is building their running base."
            ),

            "Novice": (
                "A runner who regularly runs 5-10km,"
                "has some experience with structured workouts, "
                "and is beginning to build endurance and speed."
            ),

            "Intermediate": (
                "A runner who consistently trains,"
                "can comfortably complete 10-20km runs, "
                "and has experience racing distances up to the Half Marathon."
            ),

            "Advanced": (
                "A highly experienced runner who regularly"
                "completes 30km+ runs and has completed"
                "Marathons or Ultras."
            )
        }

        level_list = [
            "Beginner",
            "Novice",
            "Intermediate",
            "Advanced"
        ]

        for level in level_list:
            level_card = self.create_card(dp(100))

            # Level title
            btn = ToggleButton(
                text=level,
                size_hint=(1, None),
                height=dp(35),
                font_size=dp(19),
                background_normal="",
                background_color=(0.12, 0.16, 0.24, 1),
                color=TEXT,
                bold=True,
                border=(0, 0, 0, 0),
                group="running_level"
            )

            # Description
            description = Label(
                text=level_descriptions[level],
                font_size=dp(13),
                color=SUBTEXT,
                halign="center",
                valign="middle",
                size_hint=(1, None),
                height=dp(40)
            )

            description.bind(
                size=lambda instance, value:
                setattr(instance, "text_size", value)
            )

            btn.bind(
                on_press=self.set_level
            )

            self.level_buttons[level] = btn

            level_card.add_widget(btn)
            level_card.add_widget(description)

            content.add_widget(level_card)

        layout.add_widget(content)

        # ERROR MESSAGE (outside loop)
        self.error_label = Label(
            text="",
            font_size=18,
            color=(1, 0.3, 0.3, 1),
            size_hint_y=None,
            height=30
        )

        layout.add_widget(self.error_label)

        # Buttons
        btn_box = BoxLayout(
            size_hint=(1, None),
            height=dp(55),
            spacing=dp(15)
        )

        back_btn = Button(
            text="Previous",
            font_size=19,
            background_normal="",
            background_color=(0, 0, 0, 0),
            color=TEXT,
            bold=True
        )

        with back_btn.canvas.before:
            Color(0.15, 0.18, 0.27, 1)
            back_background = RoundedRectangle(
                pos=back_btn.pos,
                size=back_btn.size,
                radius=[dp(12)]
            )

        back_btn.bind(
            pos=lambda instance, value:
            setattr(back_background, 'pos', value),
            size=lambda instance, value:
            setattr(back_background, 'size', value)
        )

        next_btn = Button(
            text="Next",
            font_size=19,
            background_normal="",
            background_color=(0, 0, 0, 0),
            color=TEXT,
            bold=True
        )

        with next_btn.canvas.before:
            Color(*PRIMARY)
            next_background = RoundedRectangle(
                pos=next_btn.pos,
                size=next_btn.size,
                radius=[dp(12)]
            )

        next_btn.bind(
            pos=lambda instance, value:
            setattr(next_background, 'pos', value),
            size=lambda instance, value:
            setattr(next_background, 'size', value)
        )

        back_btn.bind(on_press=self.go_back)
        next_btn.bind(on_press=self.go_next)

        btn_box.add_widget(back_btn)
        btn_box.add_widget(next_btn)

        layout.add_widget(btn_box)

        self.add_widget(layout)

    def create_card(self, height=None):

        card = BoxLayout(
            orientation="vertical",
            padding=[dp(20), dp(12)],
            spacing=dp(5),
            size_hint_y=None,
            height=height
        )

        with card.canvas.before:
            Color(
                0.08, 0.11, 0.18, 1
            )

            card.rect = RoundedRectangle(
                pos=card.pos,
                size=card.size,
                radius=[dp(15)]
            )

        card.bind(
            pos=lambda instance, value:
            setattr(card.rect, "pos", value)
        )

        card.bind(
            size=lambda instance, value:
            setattr(card.rect, "size", value)
        )

        return card

    def set_level(self, instance):

        # If clicking the currently selected level,
        # deselect it.
        if self.selected_level == instance.text:
            self.selected_level = None

            instance.background_color = (
                0.12,
                0.16,
                0.24,
                1
            )

            return

        # Select the new level
        self.selected_level = instance.text

        # Reset all buttons
        for level, button in self.level_buttons.items():
            button.background_color = (
                0.12,
                0.16,
                0.24,
                1
            )

        # Highlight selected button
        instance.background_color = (
            0.2,
            0.6,
            1,
            1
        )

        # Clear error
        self.error_label.text = ""

    def validate_level(self):

        self.error_label.text = ""

        if self.selected_level is None:
            self.error_label.text = (
                "You must select what level runner you are."
            )
            return False

        return True

    def go_next(self, instance):

        if not self.validate_level():
            return

        App.get_running_app().data["level"] = self.selected_level

        self.manager.current = "runningInfo"

    def go_back(self, instance):
        self.manager.current = "race"


class RunningPlanInfoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.daysSelected = []

        # Main Layout
        layout = BoxLayout(
            orientation="vertical",
            padding=[dp(30), dp(25)],
            spacing=dp(15)
        )

        # Title
        title = Label(
            text="Running Plan",
            font_size=dp(34),
            color=TEXT,
            bold=True,
            size_hint_y=None,
            height=dp(45)
        )

        subtitle = Label(
            text="Set up your training schedule",
            font_size=dp(16),
            color=SUBTEXT,
            size_hint_y=None,
            height=dp(30)
        )

        layout.add_widget(title)
        layout.add_widget(subtitle)

        content = BoxLayout(
            orientation="vertical",
            spacing=dp(15),
            size_hint_y=None
        )

        content.bind(
            minimum_height=content.setter("height")
        )

        # Plan Details Card

        plan_card = self.create_card(dp(145))

        plan_title = Label(
            text="PLAN DETAILS",
            font_size=dp(14),
            color=SUBTEXT,
            bold=True,
            size_hint_y=None,
            height=dp(25)
        )

        self.plan_length_title = Label(
            text="How long do you want your plan to be?",
            font_size=dp(18),
            color=TEXT,
            bold=True,
            size_hint_y=None,
            height=dp(30)
        )

        self.planLength = TextInput(
            hint_text="Number of weeks (3-20)",
            font_size=dp(17),
            size_hint=(1, None),
            height=dp(50),
            multiline=False,
            background_normal="",
            background_active="",
            background_color=(0.12, 0.16, 0.24, 1),
            foreground_color=TEXT,
            hint_text_color=SUBTEXT,
            padding=[dp(15), dp(12)]
        )

        self.planLength.bind(
            on_text_validate=self.update_length
        )

        plan_card.add_widget(plan_title)
        plan_card.add_widget(self.plan_length_title)
        plan_card.add_widget(self.planLength)

        content.add_widget(plan_card)

        # Running Days Card

        activity_card = self.create_card(dp(150))

        self.activity_title = Label(
            text="TRAINING DAYS",
            font_size=dp(14),
            color=SUBTEXT,
            bold=True,
            size_hint_y=None,
            height=dp(25)
        )

        self.activity_description = Label(
            text="Select all the days you want to run.",
            font_size=dp(15),
            color=SUBTEXT,
            halign="center",
            valign="middle",
            size_hint_y=None,
            height=dp(25)
        )

        days = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        ]

        grid = GridLayout(
            rows=1,
            cols=7,
            size_hint_y=None,
            height=dp(55),
            spacing=dp(6)
        )

        for day in days:
            grid.add_widget(
                self.create_button(day)
            )

        activity_card.add_widget(self.activity_title)
        activity_card.add_widget(self.activity_description)
        activity_card.add_widget(grid)

        content.add_widget(activity_card)

        # Long Run Card

        long_run_card = self.create_card(dp(145))

        self.long_run_title = Label(
            text="LONG RUN",
            font_size=dp(14),
            color=SUBTEXT,
            bold=True,
            size_hint_y=None,
            height=dp(25)
        )

        self.long_run_description = Label(
            text="Choose the day for your longest workout.",
            font_size=dp(15),
            color=SUBTEXT,
            halign="center",
            valign="middle",
            size_hint_y=None,
            height=dp(25)
        )

        # DropDown

        self.dropdown2 = DropDown()

        for day in days:
            btn = Button(
                text=day,
                size_hint_y=None,
                height=dp(44),
                background_normal="",
                background_color=(0.12, 0.16, 0.24, 1),
                color=TEXT,
                bold=True,
                border=(0, 0, 0, 0)
            )

            btn.bind(
                on_release=lambda btn:
                self.dropdown2.select(btn.text)
            )

            self.dropdown2.add_widget(btn)

        self.longActivityBtn = Button(
            text="Select Day",
            size_hint=(1, None),
            height=dp(50),
            background_normal="",
            background_color=(0.12, 0.16, 0.24, 1),
            color=TEXT,
            bold=True,
            font_size=dp(17),
            border=(0, 0, 0, 0)
        )

        self.longActivityBtn.bind(
            on_release=self.dropdown2.open
        )

        self.dropdown2.bind(
            on_select=lambda instance, x:
            self.set_long_Activty_day(x)
        )

        long_run_card.add_widget(self.long_run_title)
        long_run_card.add_widget(self.longActivityBtn)
        long_run_card.add_widget(self.long_run_description)

        content.add_widget(long_run_card)

        layout.add_widget(content)

        # ERROR MESSAGE

        self.error_label = Label(
            text="",
            font_size=dp(15),
            color=(1, 0.3, 0.3, 1),
            size_hint_y=None,
            height=dp(30)
        )

        layout.add_widget(self.error_label)

        # Nav Buttons

        btn_box = BoxLayout(
            size_hint=(1, None),
            height=dp(52),
            spacing=dp(15)
        )

        back_btn = Button(
            text="Previous",
            font_size=dp(17),
            background_normal="",
            background_color=(0.12, 0.16, 0.24, 1),
            color=TEXT,
            bold=True,
            border=(0, 0, 0, 0)
        )

        next_btn = Button(
            text="Continue",
            font_size=dp(17),
            background_normal="",
            background_color=(0.12, 0.16, 0.24, 1),
            color=TEXT,
            bold=True,
            border=(0, 0, 0, 0)
        )

        back_btn.bind(
            on_press=self.go_back
        )

        next_btn.bind(
            on_press=self.go_next
        )

        btn_box.add_widget(back_btn)
        btn_box.add_widget(next_btn)

        layout.add_widget(btn_box)

        self.add_widget(layout)

    def validate_plan_length(self):

        self.error_label.text = ""

        planLength = self.planLength.text

        # No blank entries
        if not planLength:
            self.error_label.text = (
                "Please Input your plan length."
            )
            return False

        # Validate format
        if not planLength.isdigit():
            self.error_label.text = (
                "You must input a number"
            )
            return False

        # Plan can be no less than 3 weeks
        if int(planLength) < 3:
            self.error_label.text = (
                "The plan must be at least 3 weeks."
            )
            return False

        # Plan can be no more than 20 weeks
        if int(planLength) > 20:
            self.error_label.text = (
                "The plan length must be less than 30 weeks."
            )
            return False
        return True

    def validate_activity_days(self):

        self.error_label.text = ""

        days = self.daysSelected

        # No blank entries
        if not days:
            self.error_label.text = (
                "Please select your days."
            )
            return False

        # At least 2 running days
        if len(days) < 2:
            self.error_label.text = (
                "Please run at least 2 days."
            )
            return False
        return True

    def validate_longActivityDay(self):

        self.error_label.text = ""

        longActivityDay = self.longActivityBtn.text

        # No blank entries
        if longActivityDay == "Select Day":
            self.error_label.text = (
                "Please input your long activity day."
            )
            return False
        return True

    def update_length(self, instance):
        App.get_running_app().data["CurrentPlanLength"] = self.planLength.text

    def update_sessions(self, instance):
        App.get_running_app().data["CurrentPlanLength"] = self.noSessions.text

    def create_button(self, day):
        btn = ToggleButton(
            text=day[:3],
            size_hint=(1, None),
            height=dp(55),
            font_size=dp(14),
            background_normal="",
            background_color=(0.12, 0.16, 0.24, 1),
            color=TEXT,
            bold=True,
            border=(0, 0, 0, 0)
        )
        btn.bind(on_press=lambda instance: self.toggle_day(instance, day))
        return btn

    def toggle_day(self, instance, day):
        if instance.state == "down":
            instance.background_color = (
                0.2,
                0.6,
                1,
                1
            )
            if day not in self.daysSelected:
                self.daysSelected.append(day)
        else:
            instance.background_color = (
                0.12,
                0.16,
                0.24,
                1
            )
            if day in self.daysSelected:
                self.daysSelected.remove(day)

        print("Selected days:", self.daysSelected)

        # Save globally
        App.get_running_app().data["ActivityDays"] = self.daysSelected

    def set_long_Activty_day(self, day):
        self.longActivityBtn.text = day
        App.get_running_app().data["LongActivityDay"] = day
        print("Long Activity day:", day)

    def create_card(self, height=None):
        card = BoxLayout(
            orientation="vertical",
            padding=[dp(20), dp(15)],
            spacing=dp(10),
            size_hint_y=None,
            height=height
        )

        with card.canvas.before:
            Color(
                0.08, 0.11, 0.18, 1
            )
            card.rect = RoundedRectangle(
                pos=card.pos,
                size=card.size,
                radius=[dp(15)]
            )

        card.bind(
            pos=lambda instance, value:
            setattr(card.rect, "pos", value)
        )

        card.bind(
            size=lambda instance, value:
            setattr(card.rect, "size", value)
        )

        return card

    def go_next(self, instance):
        # Validate plan Length
        if not self.validate_plan_length():
            return

        # Validate activity days
        if not self.validate_activity_days():
            return

        # Validate long activity day
        if not self.validate_longActivityDay():
            return

        if "running" in selected:
            selected.remove("running")

        print("Remaining sports:", selected)

        # For each sport go through process

        length = len(selected)
        for i in range(length):
            self.manager.current = selected[i]

        if not selected:
            self.manager.current = "BuildPlan"

    def go_back(self, instance):
        self.manager.current = "race"
