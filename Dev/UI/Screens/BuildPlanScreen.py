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
from Dev.UI.Theme import *

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

        # Level
        self.level_label = Label(font_size=20, size_hint_y=None, height=30, color = TEXT)


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
        content.add_widget(self.level_label)
        content.add_widget(self.length)
        content.add_widget(self.planLength)
        content.add_widget(self.activityDays)
        content.add_widget(grid)
        content.add_widget(self.longActivityDay)
        content.add_widget(self.longActivityBtn)

        # ERROR MESSAGE
        self.error_label = Label(
            text="",
            font_size=18,
            color=(1, 0.3, 0.3, 1),
            size_hint_y=None,
            height=30
        )

        content.add_widget(self.error_label)

        content.add_widget((buildPlanBtn))
        scroll.add_widget(content)
        layout.add_widget(scroll)
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

    def on_enter(self):
        data = App.get_running_app().data
        race = data.get("race")
        level = data.get("level")
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
            self.activityDays.text = "What days do you want to Run: "
            self.longActivityDay.text = "What day do you want to do your long Run: "
            self.race_label.text = f"Race: {race.upper()}"
            self.level_label.text = f"Level Runner: {level}"
            self.longest_label.text = f"Longest Run: {longestRun} KM"
            self.weekly_label.text = f"Current Weekly Running Distance: {weeklyRunDistance} KM"
            self.currentPB_label.text = f"Your Current {race.upper()} PB is: {currentRunPB}"

        # if Race is a Swimming Race
        elif race in raceSwim:
            self.activityDays.text = "What days do you want to Swim: "
            self.longActivityDay.text = "What day do you want to do your long Swim: "
            self.race_label.text = f"Race: {race.upper()}"
            self.longest_label.text = f"Longest Swim: {longestSwim} M"
            self.weekly_label.text = f"Current Weekly Swimming Distance: {weeklySwimDistance} M"
            self.currentPB_label.text = f"Your Current {race.upper()} PB is: {currentSwimPB}"

        # if Race is a Cycling Race
        elif race in raceCycle:
            self.activityDays.text = "What days do you want to Cycle: "
            self.longActivityDay.text = "What day do you want to do your long Ride: "
            self.race_label.text = f"Race: {race.upper()}"
            self.longest_label.text = f"Longest Cycle: {longestCycle} KM"
            self.weekly_label.text = f"Current Weekly Cycling Distance: {weeklyCycleDistance} KM"
            self.currentPB_label.text = f"Your Current {race.upper()} Average is: {currentCyclePB} KMH"

        # if Race is a Triathlon Race
        elif race in raceTriathlon:

            # Needs changing so it outputs all of this data
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

    def build_plan(self, instance):

        # Validate plan Length
        if not self.validate_plan_length():
            return

        # Validate activity days
        if not self.validate_activity_days():
            return

        # Validate long activity day
        if not self.validate_longActivityDay():
            return

        self.manager.current = "plan"
