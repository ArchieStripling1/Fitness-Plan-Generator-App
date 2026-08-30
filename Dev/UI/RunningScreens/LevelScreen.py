from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen
from kivy.uix.togglebutton import ToggleButton
from Dev.UI.Theme import TEXT, PRIMARY, SUBTEXT
from kivy.graphics import Color, RoundedRectangle
from kivy.metrics import dp
from Dev.Core.UserDataValidation import UserDataValidation


class LevelScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.selected_level = None
        self.level_buttons = {}

        layout = BoxLayout(
            orientation='vertical',
            padding=[dp(35), dp(25), dp(35), dp(25)],
            spacing=dp(15)
        )

        title = Label(
            text="What Level Runner are you?",
            font_size=36,
            size_hint_y=None,
            height=dp(55),
            bold=True,
            color=TEXT
        )
        subtitle = Label(
            text="Choose the level that best describes your experience",
            font_size=15,
            size_hint_y=None,
            height=dp(35),
            color=TEXT
        )

        layout.add_widget(title)
        layout.add_widget(subtitle)

        scroll = ScrollView(
            size_hint_y=1,
            bar_width=dp(4)
        )

        content = BoxLayout(
            orientation="vertical",
            spacing=dp(12),
            size_hint_y=None
        )

        content.bind(
            minimum_height=content.setter("height")
        )

        level_descriptions = {
            "Beginner": (
                "A runner who is new to structured training, "
                "has not consistently run beyond 5km,"
                "and is building their running base."
            ),

            "Novice": (
                "A runner who regularly runs 5-10km,"
                "has some experience with structured workouts, "
                "and is beginning to build endurance and speed."
            ),

            "Intermediate": (
                "A runner who consistently trains,"
                "can comfortably complete 10-20km runs, "
                "and has experience racing distances up to the Half Marathon."
            ),

            "Advanced": (
                "A highly experienced runner who regularly"
                "completes 30km+ runs and has completed"
                "Marathons or Ultras."
            )
        }

        level_list = [
            "Beginner",
            "Novice",
            "Intermediate",
            "Advanced"
        ]

        for level in level_list:
            level_card = self.create_card(dp(100))

            # Level title
            btn = ToggleButton(
                text=level,
                size_hint_y=None,
                height=dp(35),
                font_size=dp(19),
                background_normal="",
                background_color=(0.12, 0.16, 0.24, 1),
                color=TEXT,
                bold=True,
                border=(0, 0, 0, 0),
                group="running_level"
            )

            # Description
            description = Label(
                text=level_descriptions[level],
                font_size=dp(13),
                color=SUBTEXT,
                halign="center",
                valign="middle",
                size_hint_y=None,
                height=dp(40)
            )

            description.bind(
                size=lambda instance, value:
                setattr(instance, "text_size", value)
            )

            btn.bind(
                on_press=self.set_level
            )

            self.level_buttons[level] = btn

            level_card.add_widget(btn)
            level_card.add_widget(description)

            content.add_widget(level_card)

        scroll.add_widget(content)

        layout.add_widget(scroll)

        # ERROR MESSAGE (outside loop)
        self.error_label = Label(
            text="",
            font_size=18,
            color=(1, 0.3, 0.3, 1),
            size_hint_y=None,
            height=30
        )

        layout.add_widget(self.error_label)

        # Buttons
        btn_box = BoxLayout(
            size_hint_y=None,
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

    def create_card(self, height=None):

        card = BoxLayout(
            orientation="vertical",
            padding=[dp(20), dp(12)],
            spacing=dp(5),
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

    def set_level(self, instance):

        # If clicking the currently selected level,
        # deselect it.
        if self.selected_level == instance.text:
            self.selected_level = None

            instance.background_color = (
                0.12,
                0.16,
                0.24,
                1
            )

            return

        # Select the new level
        self.selected_level = instance.text

        # Reset all buttons
        for level, button in self.level_buttons.items():
            button.background_color = (
                0.12,
                0.16,
                0.24,
                1
            )

        # Highlight selected button
        instance.background_color = (
            0.2,
            0.6,
            1,
            1
        )

        # Clear error
        self.error_label.text = ""


    def go_next(self, instance):

        # Validate Level
        valid, error = UserDataValidation.validate_level(
            self.selected_level
        )
        if not valid:
            self.error_label.text = error
            return

        App.get_running_app().data["level"] = self.selected_level

        self.manager.current = "runningInfo"

    def go_back(self, instance):
        self.manager.current = "race"
