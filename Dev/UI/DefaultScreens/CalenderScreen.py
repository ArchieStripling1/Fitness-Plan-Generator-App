from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
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

