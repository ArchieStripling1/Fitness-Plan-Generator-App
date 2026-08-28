from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen
from kivy.app import App
from Dev.UI.Theme import BG, TEXT, PRIMARY, SUBTEXT
from kivy.graphics import Color, RoundedRectangle
from kivy.metrics import dp

selected = []


class RaceScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # setup Kivy screen

        self.race_buttons = {}

        layout = BoxLayout(
            orientation="vertical",
            padding=[dp(30), dp(25)],
            spacing=dp(15)
        )

        # Background
        with layout.canvas.before:
            Color(*BG)

            self.background = RoundedRectangle(
                pos=layout.pos,
                size=layout.size
            )

        layout.bind(
            pos=self.update_rect,
            size=self.update_rect
        )

        # Header
        title = Label(
            text="Select Your Race",
            font_size=dp(34),
            color=TEXT,
            bold=True,
            size_hint_y=None,
            height=dp(45)
        )

        subtitle = Label(
            text="Choose the race you are training for",
            font_size=dp(16),
            color=SUBTEXT,
            size_hint_y=None,
            height=dp(30)
        )

        layout.add_widget(title)
        layout.add_widget(subtitle)

        # Scrollable area (important for many buttons)
        scroll = ScrollView(
            size_hint=(1, 1),
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

        # Running
        running_card = self.create_card()

        running_card.add_widget(
            self.section_label("RUNNING")
        )

        running_races = [
            ("5K", "5k"),
            ("10K", "10k"),
            ("Half Marathon", "half"),
            ("Marathon", "marathon"),
        ]

        for text, value in running_races:
            running_card.add_widget(
                self.create_button(text, value)
            )

        content.add_widget(running_card)

        # Cycling
        cycling_card = self.create_card()

        cycling_card.add_widget(
            self.section_label("CYCLING")
        )

        cycling_races = [
            ("20K Ride", "cycle_20"),
            ("50K Ride", "cycle_50"),
            ("100K Ride", "cycle_100"),
            ("160K Ride", "cycle_160")
        ]

        for text, value in cycling_races:
            cycling_card.add_widget(
                self.create_button(text, value)
            )

        content.add_widget(cycling_card)

        # Swimming
        swimming_card = self.create_card()

        swimming_card.add_widget(
            self.section_label("SWIMMING")
        )

        swimming_races = [
            ("400m", "swim_400"),
            ("1500m", "swim_1500"),
            ("3000m", "swim_3000"),
            ("5000m", "swim_5000"),
        ]

        for text, value in swimming_races:
            swimming_card.add_widget(
                self.create_button(text, value)
            )

        content.add_widget(swimming_card)

        # Triathlon
        triathlon_card = self.create_card()

        triathlon_card.add_widget(
            self.section_label("TRIATHLON")
        )

        triathlon_races = [
            ("Olympic Triathlon", "olympic_triathlon"),
            ("Half-IronMan", "ironman_70.3"),
            ("Full-IronMan", "ironman_140.6"),
        ]

        for text, value in triathlon_races:
            triathlon_card.add_widget(
                self.create_button(text, value)
            )

        content.add_widget(triathlon_card)

        scroll.add_widget(content)

        layout.add_widget(scroll)

        # ERROR MESSAGE

        self.error_label = Label(
            text="",
            font_size=dp(15),
            color=(1, 0.3, 0.3, 1),
            size_hint_y=None,
            height=dp(25),
            halign="center",
            valign="middle"
        )

        self.error_label.bind(
            size=lambda instance, value:
            setattr(instance, "text_size", value)
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

        self.selected_race = None

    def create_card(self):

        card = BoxLayout(
            orientation="vertical",
            padding=[dp(20), dp(15)],
            spacing=dp(8),
            size_hint_y=None
        )

        # Calculate height based on children
        card.bind(
            minimum_height=card.setter("height")
        )

        with card.canvas.before:
            Color(
                0.08,
                0.11,
                0.18,
                1
            )

            card.rect = RoundedRectangle(
                pos=card.pos,
                size=card.size,
                radius=[dp(15)]
            )

        card.bind(
            pos=lambda instance, value:
            setattr(card.rect, "pos", value),

            size=lambda instance, value:
            setattr(card.rect, "size", value)
        )

        return card

    def section_label(self, text):
        label = Label(
            text=text,
            font_size=dp(14),
            color=SUBTEXT,
            bold=True,
            size_hint_y=None,
            height=dp(25),
            halign="left",
            valign="middle"
        )

        label.bind(
            size=lambda instance, value:
            setattr(instance, "text_size", value)
        )

        return label

    # Create Button for each race value
    def create_button(self, text, value):
        btn = Button(
            text=text,
            size_hint=(1, None),
            height=dp(48),
            font_size=dp(16),
            background_normal="",
            background_color=(
                0.12,
                0.16,
                0.24,
                1
            ),
            color=TEXT,
            bold=True,
            border=(0, 0, 0, 0)
        )

        btn.bind(
            on_press=lambda instance:
            self.select_race(value)
        )

        self.race_buttons[value] = btn

        return btn

    def select_race(self, race_value):
        self.selected_race = race_value

        # Reset all race buttons
        for value, button in self.race_buttons.items():
            button.background_color = (
                0.12,
                0.16,
                0.24,
                1
            )

        # Highlight selected race
        self.race_buttons[
            race_value
        ].background_color = (
            0.2,
            0.6,
            1,
            1
        )

        if race_value in [
            "5k",
            "10k",
            "half",
            "marathon"
        ]:

            selected.clear()
            selected.append("running")

        elif race_value in [
            "cycle_20",
            "cycle_50",
            "cycle_100",
            "cycle_160"
        ]:

            selected.clear()
            selected.append("cycle")

        elif race_value in [
            "swim_400",
            "swim_1500",
            "swim_3000",
            "swim_5000"
        ]:

            selected.clear()
            selected.append("swim")

        elif race_value in [

            "olympic_triathlon",
            "ironman_70.3",
            "ironman_140.6"
        ]:

            selected.clear()
            selected.append("running")
            selected.append("cycle")
            selected.append("swim")

            # Save selected race

        App.get_running_app().data["race"] = race_value

        print("Selected race:", race_value)
        print("Selected sports:", selected)

        self.error_label.text = ""

    # go to first in queue of selected sports
    def go_next(self, instance):
        self.manager.current = selected[0]

    def go_back(self, instance):
        self.manager.current = "intro"

    def update_rect(self, *args):

        self.background.pos = self.pos
        self.background.size = self.size
