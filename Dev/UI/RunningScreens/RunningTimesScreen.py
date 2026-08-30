from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from Dev.UI.Theme import TEXT, PRIMARY, SUBTEXT
from kivy.graphics import Color, RoundedRectangle
from kivy.metrics import dp
from Dev.Core.UserDataValidation import UserDataValidation


class RunningTimeScreen(Screen):
    def __init__(self, distance, **kwargs):
        super().__init__(**kwargs)

        # reachable dictionary of PBs for distances
        self.inputs = {}
        layout = BoxLayout(
            orientation='vertical',
            padding=[dp(35), dp(25), dp(35), dp(25)],
            spacing=dp(15)
        )
        title = Label(
            text="Personal Bests",
            font_size=36,
            size_hint_y=None,
            height=dp(50),
            bold=True,
            color=TEXT
        )

        subtitle = Label(
            text="Enter your best recent race times",
            font_size=17,
            size_hint_y=None,
            height=dp(30),
            color=SUBTEXT
        )

        layout.add_widget(title)
        layout.add_widget(subtitle)

        scroll = ScrollView(
            size_hint_y=1,
            bar_width=dp(4)
        )
        content = BoxLayout(
            orientation='vertical',
            spacing=dp(10),
            size_hint_y=None
        )
        content.bind(
            minimum_height=content.setter("height")
        )

        # Create list of all the PBs they
        # will have depending on their furthest run.
        lst = []
        if distance == "Marathon":
            lst = ["marathon", "half", "10k", "5k"]
        elif distance == "Half-Marathon":
            lst = ["half", "10k", "5k"]
        elif distance == "10K":
            lst = ["10k", "5k"]
        elif distance == "5K":
            lst = ["5k"]

        for dist in lst:
            # Enter Longest Distance Time
            pb_box = BoxLayout(
                orientation='vertical',
                spacing=dp(8),
                padding=[dp(20), dp(12), dp(20), dp(12)],
                size_hint_y=None,
                height=dp(105)
            )

            with pb_box.canvas.before:
                Color(0.12, 0.15, 0.23, 1)
                pb_background = RoundedRectangle(
                    pos=pb_box.pos,
                    size=pb_box.size,
                    radius=[dp(15)]
                )

            pb_box.bind(
                pos=lambda instance, value, bg=pb_background:
                setattr(bg, 'pos', value),
                size=lambda instance, value, bg=pb_background:
                setattr(bg, 'size', value)
            )

            title = Label(
                text=f"{dist.upper()} PERSONAL BEST",
                font_size=15,
                color=SUBTEXT,
                bold=True,
                size_hint_y=None,
                height=dp(25),
                halign="left"
            )

            title.bind(
                size=lambda instance, value:
                setattr(instance, 'text_size', value)
            )

            pb_input = TextInput(
                hint_text="HH:MM:SS",
                font_size=21,
                height=dp(45),
                size_hint_y=None,
                multiline=False,
                padding=[dp(12), dp(8)],
                background_normal="",
                background_color=(0.08, 0.10, 0.16, 1),
                foreground_color=TEXT,
                hint_text_color=SUBTEXT
            )

            self.inputs[dist] = pb_input

            pb_box.add_widget(title)
            pb_box.add_widget(pb_input)

            content.add_widget(pb_box)

        scroll.add_widget(content)

        layout.add_widget(scroll)

        # ERROR MESSAGE
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
            text="Continue",
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

    # SAVE TIMES

    def save_inputs(self):

        data = App.get_running_app().data

        for dist, pb_input in self.inputs.items():

            text = pb_input.text.strip()

            if not text:

                continue

            total_seconds = (
                UserDataValidation.convert_time_to_seconds(text)
            )

            if total_seconds is None:

                print(
                    f"Invalid time entered for {dist}"
                )

                continue

            data[f"{dist}_pb"] = total_seconds

            print(
                f"{dist}: {total_seconds} seconds"
            )

    def go_next(self, instance):

        # Validate all PB's
        valid, error = UserDataValidation.validate_pbs(
            self.inputs
        )
        if not valid:
            self.error_label.text = error
            return

        # Save all inputs when Next is pressed
        self.save_inputs()

        self.manager.current = "level"

    def go_back(self, instance):
        self.manager.current = "race"
