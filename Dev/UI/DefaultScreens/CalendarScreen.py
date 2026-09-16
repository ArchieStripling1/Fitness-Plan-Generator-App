from kivy.app import App
from kivy.graphics import Color, RoundedRectangle
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
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

        # Columns for calendar
        cols = 7

        # Titles for the days of the week
        weekdays = ["Monday", "Tuesday", "Wednesday",
                         "Thursday", "Friday", "Saturday", "Sunday"]

        # Today's date and month
        today = date.today()
        current_month = today.month

        # First day of the month and what day the month starts on
        first_day = today.replace(day=1)
        first_day_num = first_day.weekday()
        number_of_blanks = first_day_num

        current_day = first_day

        # Create grid for calendar
        grid = GridLayout(
            cols=cols,
            size_hint_y=None,
            spacing=dp(6)
        )

        grid.bind(minimum_height=grid.setter("height"))

        # Add weekdays to top of calendar
        for title in weekdays:
            grid.add_widget(Label(text=title))

        # Create blank sections for previous month
        blank = 0
        while blank < number_of_blanks:
            grid.add_widget(self.create_button(""))
            blank += 1

        # Add days of the month
        while current_day.month == current_month:
            grid.add_widget(self.create_button(str(current_day.day)))
            current_day += timedelta(days=1)

        self.content.add_widget(grid)


    def create_button(self, day_date):
        btn = Button(
            text=day_date,
            size_hint=(1, None),
            height=dp(55),
            font_size=dp(14),
            background_normal="",
            background_color=(0.12, 0.16, 0.24, 1),
            color=TEXT,
            bold=True,
            border=(0, 0, 0, 0)
        )
        return btn

    # Function to create dates for each day of plan.
    def workout_dates(self):

        # Date of today
        today = date.today()

        print(today)

        # Days until start of next week
        days_until_monday = 7 - today.weekday()
        # date of start of the week
        next_monday = today + timedelta(days=days_until_monday)

        print(next_monday)

        data = App.get_running_app().data

        plan = data["GeneratedPlan"]

        # Create empty dict of workouts and dates of workouts
        workout_dates = {}

        days = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]

        print(today.weekday())
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

                # Skip Rest days
                if workout["type"] != "Rest":

                    print(day)

                    # Get weekday in number form.
                    weekday_offset = days.index(day)
                    print(weekday_offset)

                    # Calculate for workout date.
                    workout_date = next_monday + timedelta(days=week_offset) + timedelta(days=weekday_offset)
                    print(workout_date)

                    # Add workout date and workout to dictionary workout dates.
                    workout_dates[workout_date] = workout

        return workout_dates
