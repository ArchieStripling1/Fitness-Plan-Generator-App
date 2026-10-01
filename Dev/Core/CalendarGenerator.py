from kivy.app import App
from kivy.graphics import Color, RoundedRectangle
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from Dev.UI.Theme import TEXT, CARD, SUBTEXT
from datetime import date, timedelta


class CalendarGenerator:

    def __init__(self, data, calendar_container):
        self.data = data
        self.calendar_container = calendar_container

        self.current_day = date.today()
        self.current_month = self.current_day.month
        self.current_year = self.current_day.year

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

    def create_day_button(self, day_date, current_day):
        # Normal background
        background = (
            0.12,
            0.16,
            0.24,
            1
        )

        # Highlight today
        if current_day == date.today():
            background = (
                0.18,
                0.24,
                0.35,
                1
            )
        workout_dates = self.workout_dates()

        workout = workout_dates.get(current_day)

        if workout:
            workout_type = workout["type"]

            button_text = (
                f"{day_date}\n"
                f"{workout_type}"
            )
        else:
            button_text = str(day_date)

        button = Button(
            text=button_text,
            markup=True,
            font_size=dp(12),
            background_normal="",
            background_color=background,
            color=TEXT,
            bold=False,
            size_hint_y=None,
            height=dp(68),
            border=(0, 0, 0, 0)
        )
        return button

    def build_calendar(self):

        self.calendar_container.clear_widgets()

        # Titles for the days of the week
        weekdays = ["Monday", "Tuesday", "Wednesday",
                    "Thursday", "Friday", "Saturday", "Sunday"]
        months = ["January", "February", "March", "April",
                  "May", "June", "July", "August",
                  "September", "October", "November",
                  "December"]

        # First day of the month and what day the month starts on
        first_day = date(self.current_year, self.current_month, 1)
        first_day_num = first_day.weekday()
        number_of_blanks = first_day_num

        current_day = first_day

        month_name = months[self.current_month - 1]

        # Create Month Buttons
        month_header = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height=dp(55),
            spacing=dp(10)
        )

        prev_month = Button(
            text="‹",
            font_size=dp(32),
            background_normal="",
            background_color=(0.12, 0.16, 0.24, 1),
            color=TEXT,
            bold=True
        )

        prev_month.bind(
            on_press=self.go_prev_month
        )

        month_label = Label(
            text=f"{month_name} {self.current_year}",
            font_size=dp(21),
            bold=True,
            color=TEXT,
            halign="center",
            valign="middle"
        )

        next_month = Button(
            text="›",
            font_size=dp(32),
            background_normal="",
            background_color=(0.12, 0.16, 0.24, 1),
            color=TEXT,
            bold=True
        )
        next_month.bind(
            on_press=self.go_next_month
        )

        month_header.add_widget(prev_month)
        month_header.add_widget(month_label)
        month_header.add_widget(next_month)

        self.calendar_container.add_widget(month_header)

        # Create grid for calendar
        calendar_card = BoxLayout(
            orientation="vertical",
            padding=dp(12),
            spacing=dp(8),
            size_hint_y=None
        )

        with calendar_card.canvas.before:
            Color(*CARD)

            calendar_card.rect = RoundedRectangle(
                pos=calendar_card.pos,
                size=calendar_card.size,
                radius=[dp(20)]
            )

        calendar_card.bind(
            pos=self.update_background,
            size=self.update_background
        )

        weekday_grid = GridLayout(
            cols=7,
            size_hint_y=None,
            height=dp(30),
            spacing=dp(4)
        )

        # Add weekdays to top of calendar
        for weekday in weekdays:
            weekday_label = Label(
                text=weekday,
                font_size=dp(11),
                bold=True,
                color=SUBTEXT,
                halign="center",
                valign="middle"
            )

            weekday_grid.add_widget(weekday_label)

        calendar_card.add_widget(weekday_grid)

        calendar_grid = GridLayout(
            cols=7,
            spacing=dp(5),
            size_hint_y=None
        )

        calendar_grid.bind(
            minimum_height=calendar_grid.setter("height")
        )

        # Create blank sections for previous month
        blank = 0
        while blank < number_of_blanks:
            calendar_grid.add_widget(self.create_button(""))
            blank += 1

        # Add days of the month
        while current_day.month == self.current_month:
            day_button = self.create_day_button(
                str(current_day.day),
                current_day
            )

            calendar_grid.add_widget(day_button)
            current_day += timedelta(days=1)

        calendar_card.add_widget(calendar_grid)

        # Let card calculate its height
        calendar_card.bind(
            minimum_height=calendar_card.setter("height")
        )

        self.calendar_container.add_widget(calendar_card)

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

    def update_background(self, instance, value):

        instance.rect.pos = instance.pos
        instance.rect.size = instance.size

    def go_prev_month(self, instance):
        if self.current_month == 1:
            self.current_month = 12
            self.current_year -= 1
        else:
            self.current_month -= 1

        self.build_calendar()

    def go_next_month(self, instance):
        if self.current_month == 12:
            self.current_month = 1
            self.current_year += 1
        else:
            self.current_month += 1

        self.build_calendar()
