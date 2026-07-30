from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from kivy.uix.togglebutton import ToggleButton
from kivy.app import App
from Theme import *

class BuildPlan(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # setup Kivy screen

        self.daysSelected = []

        layout = BoxLayout(orientation='vertical', padding=25, spacing=25)

            # Header
        title = Label(
            text="Build Plan",
            font_size=36,
            size_hint=(1, 0.15),
            bold=True,
            color = TEXT
        )

        layout.add_widget(title)

        scroll = ScrollView(size_hint=(1, 0.75))
        content = BoxLayout(
            orientation='vertical',
            spacing=20,
            size_hint_y=None
        )
        content.bind(minimum_height=content.setter('height'))

        #Race Type
        self.race_label = Label(font_size=22, size_hint_y=None, height=30, color = TEXT)

        #Distance

        # Current Weekly Mileage
        self.weekly_label = Label(font_size=20, size_hint_y=None, height=30, color = TEXT)

        # Current Longest Effort
        self.longest_label = Label(font_size=20, size_hint_y=None, height=30, color = TEXT)

        # Current PB
        self.currentPB_label = Label(font_size=20, size_hint_y=None, height=30, color = TEXT)

        # Level Section for basing workout off of how much experience you have running.
        self.expertise = Label(
            text="What level Athlete are you: ",
            font_size=20
        )
        # Creates Dropdown
        self.dropdown = DropDown()

        level_list = ["Beginner", "Intermediate", "Advanced"]
        # For each day in days
        for level in level_list:
            btn = Button(
                text=level,
                size_hint_y=None,
                height=44,
                background_normal="",
                background_color=PRIMARY,
                color = TEXT,
                bold=True,
                border=(0, 0, 0, 0)
            )
            # On button click it selects the text from the day and creates a button using an anonymous function
            btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))

            self.dropdown.add_widget(btn)

        self.levelBtn = Button(
            text="Select Level",
            size_hint=(1, None),
            height=50,
            background_normal="",
            background_color=(0.22, 0.74, 0.97, 1),
            color=(1, 1, 1, 1),
            bold=True,
            border=(0, 0, 0, 0)
        )

        self.levelBtn.bind(on_release=self.dropdown.open)
        # Dropdown uses x as the day and sets the long run day variable.
        self.dropdown.bind(on_select=lambda instance, x: self.set_level(x))

        #Length of Plan
        self.length = Label(
            text="How many weeks do you want this plan to be: ",
            font_size=20,
            size_hint_y=None,
            height=30,
            color=TEXT,
        )
        self.planLength = TextInput(
            hint_text="No. Weeks",
            font_size=22,
            size_hint=(1, None),
            height=55,
            multiline=False,
            background_normal="",
            background_active="",
            background_color=(1, 1, 1, 1),
            foreground_color=(0, 0, 0, 1),
            padding=[10, 15]
        )

        self.planLength.bind(on_text_validate=self.update_length)


        # Days Available
        self.activityDays = Label(
            text="What days do you want to do a workout: ",
            font_size=20,
            color = TEXT
        )
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        grid = GridLayout(
            rows=1,
            cols=7,
            size_hint_y=None,
            height=60,
            spacing=5
        )


        for day in days:
            grid.add_widget(self.create_button(day))

        # Long Distance Effort Day
        self.longActivityDay = Label(
            text="What day do you want to do your long workout: ",
            font_size=20,
            color = TEXT
        )
        #Creates Dropdown
        self.dropdown2 = DropDown()

        #For each day in days
        for day in days:
            btn = Button(
                text=day,
                size_hint_y=None,
                height=44,
                background_normal="",
                background_color=PRIMARY,
                color=TEXT,
                bold=True,
                border=(0, 0, 0, 0)
            )
            #On button click it selects the text from the day and creates a button using an anonymous function
            btn.bind(on_release=lambda btn: self.dropdown2.select(btn.text))

            self.dropdown2.add_widget(btn)

        self.longActivityBtn = Button(
            text="Select Day",
            size_hint=(1, None),
            height=50,
            background_normal="",
            background_color=PRIMARY,
            color=TEXT,
            bold=True,
            border=(0, 0, 0, 0)
        )

        self.longActivityBtn.bind(on_release=self.dropdown2.open)
        #Dropdown uses x as the day and sets the long run day variable.
        self.dropdown2.bind(on_select=lambda instance, x: self.set_long_Activty_day(x))

        # Build Plan Button
        buildPlanBtn = Button(
            text="Build Plan",
            size_hint=(1, None),
            height=50,
            background_normal="",
            background_color=PRIMARY,
            color=TEXT,
            bold=True,
            border=(0, 0, 0, 0)
        )
        buildPlanBtn.bind(on_press = self.build_plan)

        content.add_widget(self.race_label)
        content.add_widget(self.weekly_label)
        content.add_widget(self.longest_label)
        content.add_widget(self.currentPB_label)
        content.add_widget(self.expertise)
        content.add_widget(self.levelBtn)
        content.add_widget(self.length)
        content.add_widget(self.planLength)
        content.add_widget(self.activityDays)
        content.add_widget(grid)
        content.add_widget(self.longActivityDay)
        content.add_widget(self.longActivityBtn)
        content.add_widget((buildPlanBtn))
        scroll.add_widget(content)
        layout.add_widget(scroll)
        self.add_widget(layout)

    def on_enter(self):
        data = App.get_running_app().data
        race = data.get("race")
        print(race)

        # Race Types
        raceRun = ['5k', '10k', 'half', 'marathon']
        raceCycle = ['cycle_20', 'cycle_50', 'cycle_100', 'cycle_160']
        raceSwim = ['swim_400', 'swim_1500', 'swim_3000', 'swim_5000']
        raceTriathlon = ['olympic_triathlon','ironman_70.3', 'ironman_140.6']

        weeklyRunDistance = data.get("Weekly_Distance")
        weeklySwimDistance = data.get("Weekly_Swimming")
        weeklyCycleDistance = data.get("Weekly_Cycle")
        longestRun = data.get("Longest_Run")
        longestSwim = data.get("Longest_Swim")
        longestCycle = data.get("Longest_Cycle")
        #Find out what their race pb is.
        currentRunPB = data.get(f"{race}_pb")
        currentSwimPB = data.get(f"{race}_pb")
        print(currentSwimPB)
        currentCyclePB = data.get(f"{race}_pb")

        # if Race is a Running Race
        if race in raceRun:
            self.expertise.text = "What level Runner are you: "
            self.activityDays.text = "What days do you want to Run: "
            self.longActivityDay.text = "What day do you want to do your long Run: "
            self.race_label.text = f"Race: {race.upper()}"
            self.longest_label.text = f"Longest Run: {longestRun} KM"
            self.weekly_label.text = f"Current Weekly Running Distance: {weeklyRunDistance} KM"
            self.currentPB_label.text = f"Your Current {race.upper()} PB is: {currentRunPB}"

        # if Race is a Swimming Race
        elif race in raceSwim:
            self.expertise.text = "What level Swimmer are you: "
            self.activityDays.text = "What days do you want to Swim: "
            self.longActivityDay.text = "What day do you want to do your long Swim: "
            self.race_label.text = f"Race: {race.upper()}"
            self.longest_label.text = f"Longest Swim: {longestSwim} M"
            self.weekly_label.text = f"Current Weekly Swimming Distance: {weeklySwimDistance} M"
            self.currentPB_label.text = f"Your Current {race.upper()} PB is: {currentSwimPB}"

        # if Race is a Cycling Race
        elif race in raceCycle:
            self.expertise.text = "What level Cyclist are you: "
            self.activityDays.text = "What days do you want to Cycle: "
            self.longActivityDay.text = "What day do you want to do your long Ride: "
            self.race_label.text = f"Race: {race.upper()}"
            self.longest_label.text = f"Longest Cycle: {longestCycle} KM"
            self.weekly_label.text = f"Current Weekly Cycling Distance: {weeklyCycleDistance} KM"
            self.currentPB_label.text = f"Your Current {race.upper()} Average is: {currentCyclePB} KMH"

        # if Race is a Triathlon Race
        elif race in raceTriathlon:

            # Needs changing so it outputs all of this data
            self.race_label.text = f"Race: {race.upper()}"
            self.longest_label.text = f"Longest Run: {longestRun} KM"
            self.longest_label.text = f"Longest Cycle: {longestCycle} KM"
            self.longest_label.text = f"Longest Swim: {longestSwim} M"

            self.weekly_label.text = f"Current Weekly Running Distance: {weeklyRunDistance} KM"
            self.weekly_label.text = f"Current Weekly Cycling Distance: {weeklyCycleDistance} KM"
            self.weekly_label.text = f"Current Weekly Swimming Distance: {weeklySwimDistance} M"

    def update_length(self, instance):
        App.get_running_app().data["CurrentPlanLength"] = self.planLength.text

    def update_sessions(self, instance):
        App.get_running_app().data["CurrentAmountSessions"] = self.noSessions.text

    def create_button(self, day):
        btn = ToggleButton(
            text=day,
            size_hint=(1, None),
            height=60,
            font_size=20,
            background_normal="",
            background_color=PRIMARY,
            color=TEXT,
            bold=True,
            border=(1, 1, 1, 1)
        )
        btn.bind(on_press=lambda instance: self.toggle_day(instance, day))
        return btn

    def toggle_day(self, instance, day):
        if instance.state == "down":
            instance.background_color = (0.2, 0.6, 1, 1)
            if day not in self.daysSelected:
                self.daysSelected.append(day)
        else:
            instance.background_color = (0.9, 0.9, 0.9, 1)
            if day in self.daysSelected:
                self.daysSelected.remove(day)

        print("Selected days:", self.daysSelected)

        # Save globally
        App.get_running_app().data["ActivityDays"] = self.daysSelected

    def set_long_Activty_day(self, day):
        self.longActivityBtn.text = day
        App.get_running_app().data["LongActivityDay"] = day
        print("Long Activity day:", day)

    def set_level(self, level):
        self.levelBtn.text = level
        App.get_running_app().data["Level"] = level
        print("Level:", level)


    def build_plan(self, instance):
        self.manager.current = "plan"
