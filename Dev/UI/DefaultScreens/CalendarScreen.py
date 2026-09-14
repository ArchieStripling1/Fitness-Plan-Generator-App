from kivy.app import App
from kivy.graphics import Color, RoundedRectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from Dev.UI.Theme import TEXT, CARD
from datetime import date, timedelta


class CalendarScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # setup Kivy screen

        self.scroll = ScrollView()

        self.content = BoxLayout(
            orientation='vertical',
            spacing=30,
            padding=25,
            size_hint_y=None
        )

        self.content.bind(
            minimum_height=self.content.setter('height')
        )
        self.scroll.add_widget(self.content)

        self.add_widget(self.scroll)

    def on_enter(self):

        self.content.clear_widgets()

        data = App.get_running_app().data

        dates = self.workout_dates()

        plan = data["GeneratedPlan"]

        print(dates, plan)

        # Initialize Card
        header_card = BoxLayout(
            orientation='vertical',
            spacing=15,
            padding=20,
            size_hint_y=None
        )

        # Dynamic height
        header_card.bind(minimum_height=header_card.setter("height"))

        # Card background
        with header_card.canvas.before:
            Color(*CARD)
            header_card.rect = RoundedRectangle(
                pos=header_card.pos,
                size=header_card.size,
                radius=[25]
            )

        # Keep card updated
        def update_rect(instance, value):
            instance.rect.pos = instance.pos
            instance.rect.size = instance.size

        # Bind Card with updated variables
        header_card.bind(pos=update_rect, size=update_rect)

        header = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height=70,
            spacing=5
        )

        title_label = Label(
            text="Your Calender",
            font_size=32,
            bold=True,
            color=TEXT,
            size_hint_y=None,
            height=40
        )

        header.add_widget(title_label)

        header_card.add_widget(header)

        self.content.add_widget(header_card)

    # Function to create dates for each day of plan.
    def workout_dates(self):

        # Date of today
        today = date.today()

        print(today)

        # Days until start of next week
        days_until_monday = 7 - today.weekday()
        # date of start of the week
        next_monday = today + timedelta(days=days_until_monday)

        # Create instance of week offset
        week_offset = 0
        print(next_monday)

        data = App.get_running_app().data

        plan = data["GeneratedPlan"]

        # Create empty dict of workouts and dates of workouts
        workout_dates = {}

        print(plan)

        # Get week and workouts form plan.
        for week, week_data in plan.items():

            workouts = week_data["workouts"]

            # turn week into week number
            week_num = int(week[5:])

            # Offset is week * days in week
            week_offset = (week_num - 1) * 7

            print(week)
            print(week_offset)

            # Get day out of workouts.
            for day, workout in workouts.items():
                print(day)

        return workout_dates
