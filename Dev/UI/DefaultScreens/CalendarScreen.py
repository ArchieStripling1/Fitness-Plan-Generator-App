from kivy.app import App
from kivy.graphics import Color, RoundedRectangle
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from Dev.UI.Theme import TEXT, CARD, SUBTEXT
from datetime import date
from Dev.Core.CalendarGenerator import CalendarGenerator


class CalendarScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # setup Kivy screen

        self.current_day = date.today()
        self.current_month = self.current_day.month
        self.current_year = self.current_day.year

        # Main scroll area
        self.scroll = ScrollView(
            size_hint=(1, 1),
            do_scroll_x=False
        )

        self.content = BoxLayout(
            orientation="vertical",
            spacing=dp(20),
            padding=[dp(20), dp(20), dp(20), dp(20)],
            size_hint_y=None
        )

        self.content.bind(
            minimum_height=self.content.setter("height")
        )
        self.scroll.add_widget(self.content)

        self.calendar_container = BoxLayout(
            orientation="vertical",
            size_hint_y=None
        )

        self.calendar_container.bind(
            minimum_height=self.calendar_container.setter("height")
        )

        self.content.add_widget(self.calendar_container)

        self.add_widget(self.scroll)

        self. data = App.get_running_app().data

        self.generator = CalendarGenerator(self.data, self.calendar_container)

    def on_enter(self):

        self.content.clear_widgets()

        # Initialize Card
        header_card = BoxLayout(
            orientation="vertical",
            padding=[dp(20), dp(18)],
            spacing=dp(5),
            size_hint_y=None,
            height=dp(90)
        )

        with header_card.canvas.before:
            Color(*CARD)

            header_card.rect = RoundedRectangle(
                pos=header_card.pos,
                size=header_card.size,
                radius=[dp(20)]
            )

        header_card.bind(
            pos=self.generator.update_background,
            size=self.generator.update_background
        )

        title = Label(
            text="Your Calendar",
            font_size=dp(28),
            bold=True,
            color=TEXT,
            size_hint_y=None,
            height=dp(38),
            halign="left",
            valign="middle"
        )

        subtitle = Label(
            text="Keep track of your upcoming training",
            font_size=dp(14),
            color=SUBTEXT,
            size_hint_y=None,
            height=dp(22),
            halign="left",
            valign="middle"
        )

        header_card.add_widget(title)
        header_card.add_widget(subtitle)

        self.content.add_widget(header_card)

        self.content.add_widget(self.calendar_container)

        # Calendar
        self.generator.build_calendar()

        # Nav Buttons

        btn_box = BoxLayout(
            size_hint=(1, None),
            height=dp(52),
            spacing=dp(10)
        )

        calendar_btn = Button(
            text="Calendar",
            font_size=dp(14),
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

        weekly_btn = Button(
            text="Weekly Plan",
            font_size=dp(14),
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

        settings_btn = Button(
            text="Settings",
            font_size=dp(14),
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

        calendar_btn.bind(
            on_press=self.go_calendar
        )

        weekly_btn.bind(
            on_press=self.go_calendar
        )

        settings_btn.bind(
            on_press=self.go_calendar
        )

        btn_box.add_widget(calendar_btn)
        btn_box.add_widget(weekly_btn)
        btn_box.add_widget(settings_btn)

        self.content.add_widget(btn_box)

    def go_calendar(self, instance):

        self.current_day = date.today()
        self.current_month = self.current_day.month
        self.current_year = self.current_day.year

        self.generator.build_calendar()

        self.manager.current = "calendar"
