from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.app import App
from Dev.UI.Theme import TEXT
from kivy.graphics import Color, RoundedRectangle
from kivy.metrics import dp


class BuildPlan(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # setup Kivy screen

        layout = BoxLayout(
            orientation='vertical',
            padding=[dp(35), dp(25), dp(35), dp(25)],
            spacing=dp(15)
        )

        # Header
        title = Label(
            text="Your Plan",
            font_size=36,
            size_hint=(1, None),
            height=dp(55),
            bold=True,
            color=TEXT
        )

        subtitle = Label(
            text="Review your training information before building your plan.",
            font_size=15,
            size_hint=(1, None),
            height=dp(35),
            color=TEXT
        )

        layout.add_widget(title)
        layout.add_widget(subtitle)

        content = BoxLayout(
            orientation='vertical',
            spacing=dp(10),
            size_hint_y=1
        )

        race_card = BoxLayout(
            orientation='vertical',
            padding=[dp(20), dp(10)],
            size_hint_y=None,
            height=dp(65)
        )

        with race_card.canvas.before:
            Color(
                0.10, 0.14, 0.22, 1
            )
            race_card.background = RoundedRectangle(
                pos=race_card.pos,
                size=race_card.size,
                radius=[dp(12)]
            )

        race_card.bind(
            pos=lambda instance, value:
            setattr(instance.background, 'pos', value)
        )

        race_card.bind(
            size=lambda instance, value:
            setattr(instance.background, 'size', value)
        )
        self.race_label = Label(
            text="Race",
            font_size=23,
            bold=True,
            color=TEXT,
            halign='left',
            valign='middle'
        )

        self.race_label.bind(
            size=lambda instance, value:
            setattr(instance, 'text_size', value)
        )

        race_card.add_widget(self.race_label)

        # Current Training Title

        training_title = Label(
            text="CURRENT TRAINING",
            font_size=13,
            bold=True,
            color=TEXT,
            size_hint_y=None,
            height=dp(30),
            halign='left'
        )

        training_title.bind(
            size=lambda instance, value:
            setattr(instance, 'text_size', value)
        )

        content.add_widget(training_title)

        # Current Weekly Mileage

        weekly_card = BoxLayout(
            padding=[dp(20), dp(5)],
            size_hint_y=None,
            height=dp(48)
        )

        with weekly_card.canvas.before:
            Color(0.07, 0.10, 0.17, 1)
            weekly_card.background = RoundedRectangle(
                pos=weekly_card.pos,
                size=weekly_card.size,
                radius=[dp(10)]
            )

        weekly_card.bind(
            pos=lambda instance, value:
            setattr(instance.background, 'pos', value),
            size=lambda instance, value:
            setattr(instance.background, 'size', value)
        )

        self.weekly_label = Label(
            font_size=17,
            color=TEXT,
            halign='left',
            valign='middle'
        )

        self.weekly_label.bind(
            size=lambda instance, value:
            setattr(instance, 'text_size', value)
        )

        weekly_card.add_widget(self.weekly_label)
        content.add_widget(weekly_card)

        # Longest Effort

        longest_card = BoxLayout(
            padding=[dp(20), dp(5)],
            size_hint_y=None,
            height=dp(48)
        )

        with longest_card.canvas.before:
            Color(0.07, 0.10, 0.17, 1)
            longest_card.background = RoundedRectangle(
                pos=longest_card.pos,
                size=longest_card.size,
                radius=[dp(10)]
            )

        longest_card.bind(
            pos=lambda instance, value:
            setattr(instance.background, 'pos', value),
            size=lambda instance, value:
            setattr(instance.background, 'size', value)
        )

        self.longest_label = Label(
            font_size=17,
            color=TEXT,
            halign='left',
            valign='middle'
        )

        self.longest_label.bind(
            size=lambda instance, value:
            setattr(instance, 'text_size', value)
        )

        longest_card.add_widget(self.longest_label)
        content.add_widget(longest_card)

        # PB

        pb_card = BoxLayout(
            padding=[dp(20), dp(5)],
            size_hint_y=None,
            height=dp(48)
        )

        with pb_card.canvas.before:
            Color(0.07, 0.10, 0.17, 1)
            pb_card.background = RoundedRectangle(
                pos=pb_card.pos,
                size=pb_card.size,
                radius=[dp(10)]
            )

        pb_card.bind(
            pos=lambda instance, value:
            setattr(instance.background, 'pos', value),
            size=lambda instance, value:
            setattr(instance.background, 'size', value)
        )

        self.currentPB_label = Label(
            font_size=17,
            color=TEXT,
            halign='left',
            valign='middle'
        )

        self.currentPB_label.bind(
            size=lambda instance, value:
            setattr(instance, 'text_size', value)
        )

        pb_card.add_widget(self.currentPB_label)
        content.add_widget(pb_card)

        # Plan Details Title

        plan_title = Label(
            text="PLAN DETAILS",
            font_size=13,
            bold=True,
            color=TEXT,
            size_hint_y=None,
            height=dp(30),
            halign='left'
        )

        plan_title.bind(
            size=lambda instance, value:
            setattr(instance, 'text_size', value)
        )

        content.add_widget(plan_title)

        # Level

        level_card = BoxLayout(
            padding=[dp(20), dp(5)],
            size_hint_y=None,
            height=dp(48)
        )

        with level_card.canvas.before:
            Color(0.07, 0.10, 0.17, 1)
            level_card.background = RoundedRectangle(
                pos=level_card.pos,
                size=level_card.size,
                radius=[dp(10)]
            )

        level_card.bind(
            pos=lambda instance, value:
            setattr(instance.background, 'pos', value),
            size=lambda instance, value:
            setattr(instance.background, 'size', value)
        )

        self.level_label = Label(
            font_size=17,
            color=TEXT,
            halign='left',
            valign='middle'
        )

        self.level_label.bind(
            size=lambda instance, value:
            setattr(instance, 'text_size', value)
        )

        level_card.add_widget(self.level_label)
        content.add_widget(level_card)

        # Plan Length

        length_card = BoxLayout(
            padding=[dp(20), dp(5)],
            size_hint_y=None,
            height=dp(48)
        )

        with length_card.canvas.before:
            Color(0.07, 0.10, 0.17, 1)
            length_card.background = RoundedRectangle(
                pos=length_card.pos,
                size=length_card.size,
                radius=[dp(10)]
            )

        length_card.bind(
            pos=lambda instance, value:
            setattr(instance.background, 'pos', value),
            size=lambda instance, value:
            setattr(instance.background, 'size', value)
        )

        self.plan_length_label = Label(
            font_size=17,
            color=TEXT,
            halign='left',
            valign='middle'
        )

        self.plan_length_label.bind(
            size=lambda instance, value:
            setattr(instance, 'text_size', value)
        )

        length_card.add_widget(self.plan_length_label)
        content.add_widget(length_card)

        layout.add_widget(content)

        # Build Plan Button

        buildPlanBtn = Button(
            text="Build Plan",
            font_size=18,
            size_hint=(1, None),
            height=dp(58),
            background_normal="",
            background_color=(0.12, 0.16, 0.24, 1),
            color=TEXT,
            bold=True,
            border=(0, 0, 0, 0)
        )

        buildPlanBtn.bind(
            on_press=self.build_plan
        )

        layout.add_widget(buildPlanBtn)

        self.add_widget(layout)

    def on_enter(self):
        data = App.get_running_app().data
        race = data.get("race")
        level = data.get("level")
        plan_length = data.get("CurrentPlanLength")
        print(race)

        # Race Types
        raceRun = ['5k', '10k', 'half', 'marathon']
        raceCycle = ['cycle_20', 'cycle_50', 'cycle_100', 'cycle_160']
        raceSwim = ['swim_400', 'swim_1500', 'swim_3000', 'swim_5000']
        raceTriathlon = ['olympic_triathlon', 'ironman_70.3', 'ironman_140.6']

        weeklyRunDistance = data.get("Weekly_Distance")
        weeklySwimDistance = data.get("Weekly_Swimming")
        weeklyCycleDistance = data.get("Weekly_Cycle")
        longestRun = data.get("Longest_Run")
        longestSwim = data.get("Longest_Swim")
        longestCycle = data.get("Longest_Cycle")
        # Find out what their race pb is.
        currentRunPB = data.get(f"{race}_pb")
        currentSwimPB = data.get(f"{race}_pb")
        print(currentSwimPB)
        currentCyclePB = data.get(f"{race}_pb")

        # if Race is a Running Race
        if race in raceRun:
            self.race_label.text = f"Race: {race.upper()}"
            self.level_label.text = f"Level Runner: {level}"
            self.longest_label.text = \
                f"Longest Run: {longestRun} KM"
            self.weekly_label.text = \
                f"Current Weekly Running Distance: {weeklyRunDistance} KM"
            self.currentPB_label.text = \
                f"Your Current {race.upper()} PB is: {currentRunPB}"
            self.plan_length_label.text = \
                f"Plan Length: {plan_length} Weeks"

        # if Race is a Swimming Race
        elif race in raceSwim:
            self.activityDays.text = \
                "What days do you want to Swim: "
            self.longActivityDay.text = \
                "What day do you want to do your long Swim: "
            self.race_label.text = f"Race: {race.upper()}"
            self.longest_label.text = f"Longest Swim: {longestSwim} M"
            self.weekly_label.text = \
                f"Current Weekly Swimming Distance: {weeklySwimDistance} M"
            self.currentPB_label.text = \
                f"Your Current {race.upper()} PB is: {currentSwimPB}"

        # if Race is a Cycling Race
        elif race in raceCycle:
            self.activityDays.text = \
                "What days do you want to Cycle: "
            self.longActivityDay.text = \
                "What day do you want to do your long Ride: "
            self.race_label.text = \
                f"Race: {race.upper()}"
            self.longest_label.text = \
                f"Longest Cycle: {longestCycle} KM"
            self.weekly_label.text = \
                f"Current Weekly Cycling Distance: {weeklyCycleDistance} KM"
            self.currentPB_label.text = \
                f"Your Current {race.upper()} Average is: {currentCyclePB} KMH"

        # if Race is a Triathlon Race
        elif race in raceTriathlon:

            # Needs changing so it outputs all of this data
            self.longest_label.text = f"Longest Run: {longestRun} KM"
            self.longest_label.text = f"Longest Cycle: {longestCycle} KM"
            self.longest_label.text = f"Longest Swim: {longestSwim} M"

            self.weekly_label.text = \
                (f"Current Weekly Running Distance:"
                 f" {weeklyRunDistance} KM")
            self.weekly_label.text = \
                (f"Current Weekly Cycling Distance:"
                 f" {weeklyCycleDistance} KM")
            self.weekly_label.text = \
                (f"Current Weekly Swimming Distance:"
                 f" {weeklySwimDistance} M")

    def build_plan(self, instance):
        self.manager.current = "plan"
