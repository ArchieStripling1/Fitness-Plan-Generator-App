from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from kivy.uix.togglebutton import ToggleButton

from RaceScreen import selected
from Theme import *


class RunningScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Header
        title = Label(
            text="Running Profile",
            font_size=34,
            size_hint=(1, 0.15),
            bold=True,
            color=TEXT,
        )
        layout.add_widget(title)

        # Longest Run
        longest_box = BoxLayout(orientation='vertical', spacing=10)
        longest_label = Label(text="Longest Recent Run (km)", font_size=20, color=TEXT, bold=True)

        self.longest_value = Label(text="1 km", font_size=26)

        # Slider
        self.longest_slider = Slider(min=1, max=60, value=1, step=1)
        self.longest_slider.bind(value=self.update_longest)

        longest_box.add_widget(longest_label)
        longest_box.add_widget(self.longest_value)
        longest_box.add_widget(self.longest_slider)

        layout.add_widget(longest_box)

        # Weekly Distance
        weekly_box = BoxLayout(orientation='vertical', spacing=10)

        weekly_label = Label(text="Current Weekly Distance (km)", font_size=20, color=TEXT, bold=True)

        self.weekly_value = Label(text="1 km", font_size=26)

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
            font_size=18,
            color=(1, 0.3, 0.3, 1),
            size_hint_y=None,
            height=30
        )

        layout.add_widget(self.error_label)

        # Buttons
        btn_box = BoxLayout(size_hint=(1, 0.2), spacing=20)

        back_btn = Button(
            text="Previous",
            font_size=22,
            background_normal="",
            background_color=PRIMARY,
            color=TEXT,
            bold=True
        )
        next_btn = Button(
            text="Next",
            font_size=22,
            background_normal="",
            background_color=PRIMARY,
            color=TEXT,
            bold=True
        )

        # Bind Buttons
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

        #reachable dictionary of PBs for distances
        self.inputs = {}
        layout = BoxLayout(orientation='vertical', padding=15, spacing=15)

        # Create list of all the PBs they will have depending on their furthest run.
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
            title = Label(
                text=f"Enter your best recent {dist.upper()} time",
                font_size=30,
                color=TEXT,
                bold=True
            )

            self.pb_input = TextInput(
                hint_text="HH:MM:SS",
                font_size=24,
                height=30,
                size_hint=(1, 0.3),
                multiline=False
            )

            self.inputs[dist] = self.pb_input

            layout.add_widget(title)
            layout.add_widget(self.pb_input)

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
            size_hint=(1, 0.2),
            spacing=20
        )

        back_btn = Button(
            text="Previous",
            font_size=22,
            background_normal="",
            background_color=PRIMARY,
            color=TEXT,
            bold=True
        )
        next_btn = Button(
            text="Next",
            font_size=22,
            background_normal="",
            background_color=PRIMARY,
            color=TEXT,
            bold=True
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
                    "Your Marathon PB must be longer than your Half Marathon PB."
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
            padding=15,
            spacing=15
        )

        title = Label(
            text="What Level Runner are you?",
            font_size=30,
            color=TEXT,
            bold=True
        )

        layout.add_widget(title)

        content = BoxLayout(
            orientation='vertical',
            spacing=20,
            size_hint_y=None
        )

        content.bind(
            minimum_height=content.setter("height")
        )

        level_descriptions = {
            "Beginner": "A runner who has not completed a run longer than 10km and is building their running base.",
            "Intermediate": "A runner who has completed a Half Marathon and has experience with consistent training.",
            "Advanced": "A runner who regularly completes 30km+ runs or has completed Marathons or Ultras."
        }

        level_list = [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]

        for level in level_list:
            level_box = BoxLayout(
                orientation="vertical",
                spacing=5,
                size_hint_y=None,
                height=90
            )

            btn = ToggleButton(
                text=level,
                size_hint_y=None,
                height=44,
                background_normal="",
                background_color=PRIMARY,
                color=TEXT,
                bold=True,
                border=(0, 0, 0, 0)
            )

            description = Label(
                text=level_descriptions[level],
                font_size=16,
                color=SUBTEXT,
                halign="center",
                valign="middle",
                size_hint_y=None,
                height=40,
                text_size=(500, None)
            )

            btn.bind(on_press=self.set_level)

            self.level_buttons[level] = btn

            level_box.add_widget(btn)
            level_box.add_widget(description)

            content.add_widget(level_box)

        # ERROR MESSAGE (outside loop)
        self.error_label = Label(
            text="",
            font_size=18,
            color=(1, 0.3, 0.3, 1),
            size_hint_y=None,
            height=30
        )

        layout.add_widget(content)
        layout.add_widget(self.error_label)

        # BUTTONS (outside loop)
        btn_box = BoxLayout(
            size_hint=(1, 0.2),
            spacing=20
        )

        back_btn = Button(
            text="Previous",
            font_size=22,
            background_normal="",
            background_color=PRIMARY,
            color=TEXT,
            bold=True
        )

        next_btn = Button(
            text="Next",
            font_size=22,
            background_normal="",
            background_color=PRIMARY,
            color=TEXT,
            bold=True
        )

        back_btn.bind(on_press=self.go_back)
        next_btn.bind(on_press=self.go_next)

        btn_box.add_widget(back_btn)
        btn_box.add_widget(next_btn)

        layout.add_widget(btn_box)

        self.add_widget(layout)

    def set_level(self, instance):

        self.selected_level = instance.text

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

