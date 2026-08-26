from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from RaceScreen import selected
from Theme import *

class CyclingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # setup Kivy screen

        layout = BoxLayout(orientation='vertical', padding=30, spacing=30)

        # Header
        title = Label(
            text="Cycling Profile",
            font_size=24,
            size_hint=(1, 0.15),
            bold=True,
            color=TEXT
        )
        layout.add_widget(title)

        # Longest Swim
        longest_box = BoxLayout(orientation='vertical', spacing=10)
        longest_label = Label(text="Longest Cycle (km)", color=TEXT, font_size=24)

        self.longest_value = Label(text="0 km", font_size=26)

        # Slider
        self.longest_slider = Slider(min=1, max=200, value=0)
        self.longest_slider.bind(value=self.update_longest)

        longest_box.add_widget(longest_label)
        longest_box.add_widget(self.longest_value)
        longest_box.add_widget(self.longest_slider)

        layout.add_widget(longest_box)

        # Weekly Distance
        weekly_box = BoxLayout(orientation='vertical', spacing=10)

        weekly_label = Label(text="Weekly Distance (km)", color=TEXT, font_size=20)

        self.weekly_value = Label(text="0 km", font_size=26)

        # Slider
        self.weekly_slider = Slider(min=0, max=800, value=0)
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

        # Button Binds
        back_btn.bind(on_press=self.go_back)
        next_btn.bind(on_press=self.go_next)

        btn_box.add_widget(back_btn)
        btn_box.add_widget(next_btn)

        layout.add_widget(btn_box)

        self.add_widget(layout)

    # Update Slider value
    def update_longest(self, instance, value):
        self.longest_value.text = f"{int(value)} km"

    # Update Slider value
    def update_weekly(self, instance, value):
        self.weekly_value.text = f"{int(value)} km"


    def go_next(self, instance):
        CyclingDistance = int(self.longest_slider.value)
        weeklyCycling = int(self.weekly_slider.value)
        App.get_running_app().data["Longest_Cycle"] = CyclingDistance
        App.get_running_app().data["Weekly_Cycle"] = weeklyCycling
        if 20 <= CyclingDistance < 50:
            self.manager.current = "Cycling20K"
        elif 50 <= CyclingDistance < 100:
            self.manager.current = "Cycling50K"
        elif 100 <= CyclingDistance < 160:
            self.manager.current = "Cycling100K"
        elif CyclingDistance >= 160:
            self.manager.current = "Cycling160K"


    def go_back(self, instance):
        self.manager.current = "race"


class CyclingTimeScreen(Screen):
    def __init__(self, distance, **kwargs):
        super().__init__(**kwargs)  # setup Kivy screen

        # reachable dictionary of PBs for distances
        self.inputs = {}

        layout = BoxLayout(orientation='vertical', padding=30, spacing=30)

        # Create list of all the PBs they will have depending on their furthest run.
        lst = []
        if distance == "160K":
            lst = ["cycle_160", "cycle_100"]
        elif distance == "100K":
            lst = ["cycle_100", "cycle_50"]
        elif distance == "50K":
            lst = ["cycle_50", "cycle_20"]
        elif distance == "20K":
            lst = ["cycle_20"]


        #Enter your Average Time
        for dist in lst:
            # Enter Longest Distance Time
            title = Label(
                text=f"What is your average pace per {dist} (KMH)",
                font_size=30,
                color=TEXT,
                bold=True
            )

            pb_input = TextInput(
                hint_text="KMH",
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
            text = pb_input.text

            try:
                App.get_running_app().data[f"{dist}_pb"] = text
            except:
                print(f"Invalid time for {dist}")


    def go_next(self, instance):
        selected.remove('cycle')
        print(selected)

        # For each sport go through Process
        length = len(selected)
        for i in range(length):
            self.manager.current = selected[i]

        if not selected:
            self.manager.current = "BuildPlan"

    def go_back(self, instance):
        self.manager.current = "race"