from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from Dev.UI.Screens.RaceScreen import selected
from Dev.UI.Theme import TEXT,PRIMARY


class SwimmingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # setup Kivy screen

        layout = BoxLayout(orientation='vertical', padding=30, spacing=30)

        # Header

        title = Label(
            text="Swimming Profile",
            font_size=24,
            size_hint=(1, 0.15),
            bold=True,
            color=TEXT
        )
        layout.add_widget(title)

        # Longest Swim
        longest_box = BoxLayout(orientation='vertical', spacing=10)
        longest_label = Label(text="Longest Swim (Meters)", font_size=24, color=TEXT)

        self.longest_value = Label(text="0 m", font_size=26)

        # Slider
        self.longest_slider = Slider(min=1, max=6000, value=0)
        self.longest_slider.bind(value=self.update_longest)

        longest_box.add_widget(longest_label)
        longest_box.add_widget(self.longest_value)
        longest_box.add_widget(self.longest_slider)

        layout.add_widget(longest_box)

        # Weekly Distance
        weekly_box = BoxLayout(orientation='vertical', spacing=10)

        weekly_label = Label(text="Weekly Distance (Meters)",
                             font_size=20, color=TEXT)

        self.weekly_value = Label(text="0 m", font_size=26)

        # Slider
        self.weekly_slider = Slider(min=0, max=12000, value=0)
        self.weekly_slider.bind(value=self.update_weekly)

        weekly_box.add_widget(weekly_label)
        weekly_box.add_widget(self.weekly_value)
        weekly_box.add_widget(self.weekly_slider)

        layout.add_widget(weekly_box)

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
        self.longest_value.text = f"{int(value)} meters"

    # Update Slider Value
    def update_weekly(self, instance, value):
        self.weekly_value.text = f"{int(value)} meters"

    def go_next(self, instance):
        SwimmingDistance = int(self.longest_slider.value)
        weeklySwimming = int(self.weekly_slider.value)
        App.get_running_app().data["Longest_Swim"] = SwimmingDistance
        App.get_running_app().data["Weekly_Swimming"] = weeklySwimming

        if 400 <= SwimmingDistance < 1500:
            self.manager.current = "Pace400M"
        elif 1500 <= SwimmingDistance < 3000:
            self.manager.current = "Pace1500M"
        elif 3000 <= SwimmingDistance < 5000:
            self.manager.current = "Pace3000M"
        elif 5000 <= SwimmingDistance:
            self.manager.current = "Pace5000M"

    def go_back(self, instance):
        self.manager.current = "sport"


class SwimmingPace(Screen):
    def __init__(self, distance, **kwargs):
        super().__init__(**kwargs)  # setup Kivy screen

        self.inputs = {}

        layout = BoxLayout(orientation='vertical', padding=30, spacing=30)

        # Create list of all the PBs they will
        # have depending on their furthest run.
        lst = []
        if distance == "5000M":
            lst = ["swim_5000", "swim_3000"]
        elif distance == "3000M":
            lst = ["swim_3000", "swim_1500"]
        elif distance == "1500M":
            lst = ["swim_1500", "swim_400"]
        elif distance == "400M":
            lst = ["swim_400"]

        for dist in lst:
            # Enter Longest Distance Time
            title = Label(
                text=f"Enter your {dist} time",
                font_size=30,
                color=TEXT,
                bold=True
            )

            pb_input = TextInput(
                hint_text="HH:MM:SS",
                font_size=24,
                height=30,
                size_hint=(1, 0.3),
                multiline=False
            )

            self.inputs[dist] = pb_input

            pb_input.bind(on_text_validate=self.update_input)

            layout.add_widget(title)
            layout.add_widget(pb_input)

        #Buttons
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

    def update_input(self, instance):
        for dist, pb_input in self.inputs.items():
            text = pb_input.text.strip()

            # If text is accepted try split it using ':'
            # for hour minutes and seconds.
            if not text:
                continue

            try:
                hours, minutes, seconds = map(int, text.split(":"))

                # Sum for the amount of seconds.
                total = (
                        hours * 3600
                        + minutes * 60
                        + seconds
                )

                App.get_running_app().data[f"{dist}_pb"] = total

                print(dist, total)

            except Exception:
                print(f"Invalid time for {dist}")

    def go_next(self, instance):
        selected.remove('swim')
        print(selected)

        # For Each Sport go through process
        length = len(selected)
        for i in range(length):
            self.manager.current = selected[i]

        if not selected:
            self.manager.current = "BuildPlan"

    def go_back(self, instance):
        self.manager.current = "race"
