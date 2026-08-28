from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from kivy.uix.togglebutton import ToggleButton
from Dev.UI.DefaultScreens.RaceScreen import selected
from Dev.UI.Theme import TEXT, SUBTEXT
from kivy.graphics import Color, RoundedRectangle
from kivy.metrics import dp


class RunningInfoScreen(Screen):
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

        scroll = ScrollView(
            size_hint_y=1,
            bar_width=dp(4)
        )

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
            size_hint_y=None,
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
            size_hint_y=None,
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

        scroll.add_widget(content)

        layout.add_widget(scroll)

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
