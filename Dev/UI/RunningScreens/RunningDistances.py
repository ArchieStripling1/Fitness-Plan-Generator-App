from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.screenmanager import Screen
from Dev.UI.Theme import TEXT, PRIMARY, SUBTEXT
from kivy.graphics import Color, RoundedRectangle
from kivy.metrics import dp


class RunningDistances(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation='vertical',
            padding=[dp(35), dp(25), dp(35), dp(25)],
            spacing=dp(15)
        )

        # Header
        title = Label(
            text="Running Profile",
            font_size=36,
            size_hint=(1, None),
            height=dp(50),
            bold=True,
            color=TEXT
        )

        subtitle = Label(
            text="Tell us about your current running",
            font_size=17,
            size_hint=(1, None),
            height=dp(30),
            color=SUBTEXT
        )

        layout.add_widget(title)
        layout.add_widget(subtitle)

        # Longest Run
        longest_box = BoxLayout(
            orientation='vertical',
            spacing=dp(8),
            padding=[dp(20), dp(15), dp(20), dp(15)],
            size_hint=(1, None),
            height=dp(145)
        )

        with longest_box.canvas.before:
            Color(0.12, 0.15, 0.23, 1)
            longest_background = RoundedRectangle(
                pos=longest_box.pos,
                size=longest_box.size,
                radius=[dp(15)]
            )

        longest_box.bind(
            pos=lambda instance, value:
            setattr(longest_background, 'pos', value),
            size=lambda instance, value:
            setattr(longest_background, 'size', value)
        )

        longest_label = Label(
            text="Longest Recent Run (km)",
            font_size=15,
            color=SUBTEXT,
            bold=True,
            size_hint_y=None,
            height=dp(25)
        )

        self.longest_value = Label(
            text="1 km",
            font_size=27,
            color=TEXT,
            bold=True,
            size_hint_y=None,
            height=dp(38)
        )

        # Slider
        self.longest_slider = Slider(min=1, max=60, value=1, step=1)
        self.longest_slider.bind(value=self.update_longest)

        longest_box.add_widget(longest_label)
        longest_box.add_widget(self.longest_value)
        longest_box.add_widget(self.longest_slider)

        layout.add_widget(longest_box)

        # Weekly Distance
        weekly_box = BoxLayout(
            orientation='vertical',
            spacing=dp(8),
            padding=[dp(20), dp(15), dp(20), dp(15)],
            size_hint=(1, None),
            height=dp(145)
        )

        with weekly_box.canvas.before:
            Color(0.12, 0.15, 0.23, 1)
            weekly_background = RoundedRectangle(
                pos=weekly_box.pos,
                size=weekly_box.size,
                radius=[dp(15)]
            )

        weekly_box.bind(
            pos=lambda instance, value:
            setattr(weekly_background, 'pos', value),
            size=lambda instance, value:
            setattr(weekly_background, 'size', value)
        )

        weekly_label = Label(
            text="Current Weekly Distance (km)",
            font_size=15,
            color=SUBTEXT,
            bold=True,
            size_hint_y=None,
            height=dp(25)
        )

        self.weekly_value = Label(
            text="1 km",
            font_size=27,
            color=TEXT,
            bold=True,
            size_hint_y=None,
            height=dp(38)
        )

        # Slider
        self.weekly_slider = Slider(min=1, max=150, value=1, step=1)
        self.weekly_slider.bind(value=self.update_weekly)

        weekly_box.add_widget(weekly_label)
        weekly_box.add_widget(self.weekly_value)
        weekly_box.add_widget(self.weekly_slider)

        layout.add_widget(weekly_box)

        # ERROR MESSAGE
        self.error_label = Label(
            text="",
            font_size=16,
            color=(1, 0.3, 0.3, 1),
            size_hint_y=None,
            height=dp(35)
        )

        layout.add_widget(self.error_label)

        # Buttons
        btn_box = BoxLayout(
            size_hint=(1, None),
            height=dp(55),
            spacing=dp(15)
        )

        back_btn = Button(
            text="Previous",
            font_size=19,
            background_normal="",
            background_color=(0, 0, 0, 0),
            color=TEXT,
            bold=True
        )

        with back_btn.canvas.before:
            Color(0.15, 0.18, 0.27, 1)
            back_background = RoundedRectangle(
                pos=back_btn.pos,
                size=back_btn.size,
                radius=[dp(12)]
            )

        back_btn.bind(
            pos=lambda instance, value:
            setattr(back_background, 'pos', value),
            size=lambda instance, value:
            setattr(back_background, 'size', value)
        )

        next_btn = Button(
            text="Next",
            font_size=19,
            background_normal="",
            background_color=(0, 0, 0, 0),
            color=TEXT,
            bold=True
        )

        with next_btn.canvas.before:
            Color(*PRIMARY)
            next_background = RoundedRectangle(
                pos=next_btn.pos,
                size=next_btn.size,
                radius=[dp(12)]
            )

        next_btn.bind(
            pos=lambda instance, value:
            setattr(next_background, 'pos', value),
            size=lambda instance, value:
            setattr(next_background, 'size', value)
        )

        back_btn.bind(on_press=self.go_back)
        next_btn.bind(on_press=self.go_next)

        btn_box.add_widget(back_btn)
        btn_box.add_widget(next_btn)

        layout.add_widget(btn_box)

        self.add_widget(layout)

    # Update Slider Value
    def update_longest(self, instance, value):
        longest_distance = int(value)

        self.longest_value.text = f"{longest_distance} km"

        self.validate_distances()

    # Update Slider Value
    def update_weekly(self, instance, value):
        weekly_distance = int(value)

        self.weekly_value.text = f"{weekly_distance} km"

        self.validate_distances()

    def validate_distances(self):

        longest_distance = int(
            self.longest_slider.value
        )

        weekly_distance = int(
            self.weekly_slider.value
        )

        if weekly_distance < longest_distance:
            self.error_label.text = (
                "Weekly distance cannot be lower "
                "than your longest run."
            )

            return False

        self.error_label.text = ""

        return True

    def go_next(self, instance):
        longestDistance = int(self.longest_slider.value)
        weeklyDistance = int(self.weekly_slider.value)

        # Prevent invalid data
        if not self.validate_distances():
            return

        App.get_running_app().data["Longest_Run"] = longestDistance
        App.get_running_app().data["Weekly_Distance"] = weeklyDistance

        if longestDistance < 5:
            self.error_label.text = (
                "Your longest run should be at least 5 km."
            )

            return
        if 5 <= longestDistance < 10:
            self.manager.current = "RunningTime5k"
        elif 10 <= longestDistance < 21:
            self.manager.current = "RunningTime10k"
        elif 21 <= longestDistance < 42:
            self.manager.current = "RunningTimeHalf"
        elif longestDistance >= 42:
            self.manager.current = "RunningTimeMarathon"

    def go_back(self, instance):
        self.manager.current = "race"
