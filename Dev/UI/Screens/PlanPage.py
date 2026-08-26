
from kivy.graphics import Color, RoundedRectangle, Line
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen
from Dev.Core.RunningPlanGenerator import RunningPlanGenerator
from kivy.app import App
from Dev.UI.Theme import *

class PlanPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # setup Kivy screen

        # Scroll area
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

        generator = RunningPlanGenerator(data)

        plan = generator.generate_running_plan()

        App.get_running_app().data["GeneratedPlan"] = plan

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
        race = data.get("race")

        title_label = Label(
            text=f"Your {race} Plan!",
            font_size=32,
            bold=True,
            color=TEXT,
            size_hint_y=None,
            height=40
        )

        prediction_race = data.get(f"prediction_{race}")
        prediction_label = Label(
            text=f"Your predicted {race} time is : {prediction_race}!",
            font_size=18,
            color=SUBTEXT,
            size_hint_y=None,
            height=25
        )

        header.add_widget(title_label)
        header.add_widget(prediction_label)

        header_card.add_widget(header)

        self.content.add_widget(header_card)

        # Get Week and workout in that week
        for week, week_data in plan.items():

            workouts = week_data["workouts"]
            weekly_distance = week_data["distance"]

            # Initialize Card
            card = BoxLayout(
                orientation='vertical',
                spacing=15,
                padding=20,
                size_hint_y=None
            )

            # Dynamic height
            card.bind(minimum_height=card.setter("height"))

            # Card background
            with card.canvas.before:
                Color(*CARD)
                card.rect = RoundedRectangle(
                    pos=card.pos,
                    size=card.size,
                    radius=[25]
                )

            # Keep card updated
            def update_rect(instance, value):
                instance.rect.pos = instance.pos
                instance.rect.size = instance.size

            # Bind Card with updated variables
            card.bind(pos=update_rect, size=update_rect)

            header = BoxLayout(
                orientation="vertical",
                size_hint_y=None,
                height=70,
                spacing=5
            )

            week_label = Label(
                text=week,
                font_size=32,
                bold=True,
                color=TEXT,
                size_hint_y=None,
                height=40
            )

            distance_label = Label(
                text=f"{weekly_distance} km planned",
                font_size=18,
                color=SUBTEXT,
                size_hint_y=None,
                height=25
            )

            header.add_widget(week_label)
            header.add_widget(distance_label)

            card.add_widget(header)

            # Get the day and workout in workouts
            for day, workout in workouts.items():

                # Skip rest days as these don't need to be displayed in the plan section
                if workout["type"] == "Rest":
                    continue

                # Get all Workout info
                workout_text = f"[b]{day}[/b]\n"
                workout_text += f"{workout['type']}\n"

                if "session" in workout:
                    workout_text += f"Session: {workout['session']}\n"

                if "distance" in workout:
                    workout_text += f"Distance: {workout['distance']}\n"

                if "pace" in workout:
                    workout_text += f"Pace: {workout['pace']}"

                # Workout Card
                colour = {
                    "Easy Run": EASY,
                    "Recovery Run": EASY,
                    "Long Run": LONG,
                    "Interval Run": INTERVAL,
                    "Tempo Run": TEMPO,
                    "Race Practice Session!": TEMPO,
                    "Race Day!": RACE,
                }.get(workout["type"], SUBTEXT)

                workout_card = BoxLayout(
                    orientation='vertical',
                    padding=20,
                    spacing=8,
                    size_hint_y=None,
                    height=140,
                )

                # Workout card background
                with workout_card.canvas.before:

                    Color(*CARD)
                    workout_card.rect = RoundedRectangle(
                        pos=workout_card.pos,
                        size=workout_card.size,
                        radius=[24]
                    )
                    # Border
                    Color(*colour)
                    workout_card.border = Line(
                        rounded_rectangle=(
                            workout_card.x,
                            workout_card.y,
                            workout_card.width,
                            workout_card.height,
                            24
                        ),
                        width=2
                    )

                # Keep Workout Updated
                def update_workout_rect(instance, value):
                    instance.rect.pos = instance.pos
                    instance.rect.size = instance.size

                    instance.border.rounded_rectangle = (
                        instance.x,
                        instance.y,
                        instance.width,
                        instance.height,
                        24
                    )

                # Bind Card with updated variables
                workout_card.bind(
                    pos=update_workout_rect,
                    size=update_workout_rect
                )

                # Day workouts
                day_label = Label(
                    text=workout_text,
                    markup=True,
                    font_size=18,
                    color=TEXT,
                    halign="left",
                    valign="middle",
                    text_size=(650, None)
                )
                # Add day and workout to workout card
                workout_card.add_widget(day_label)

                # Add workout card to week card.
                card.add_widget(workout_card)

            # Add whole week card
            self.content.add_widget(card)




    def restart(self, instance):

        self.manager.current = "intro"
        self.data = {}





