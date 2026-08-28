
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

# Import all classes for each Screen.
from Dev.UI.DefaultScreens.IntroScreen import IntroScreen
from Dev.UI.RunningScreens.RunningDistances import RunningDistances
from Dev.UI.RunningScreens.RunningTimesScreen import RunningTimeScreen
from Dev.UI.RunningScreens.RunningInfoScreen import RunningInfoScreen
from Dev.UI.RunningScreens.LevelScreen import LevelScreen
from Dev.UI.CyclingScreens.CyclingScreen import CyclingScreen, CyclingTimeScreen
from Dev.UI.SwimmingScreens.SwimmingScreen import SwimmingScreen, SwimmingPace
from Dev.UI.DefaultScreens.RaceScreen import RaceScreen
from Dev.UI.DefaultScreens.BuildPlanScreen import BuildPlan
from Dev.UI.DefaultScreens.PlanPage import PlanPage

from kivy.core.window import Window
from kivy.utils import get_color_from_hex


class MainApp(App):
    def build(self):

        self.data = {}  # store everything here

        Window.clearcolor = get_color_from_hex("#0F172A")

        sm = ScreenManager()

        sm.add_widget(IntroScreen(name="intro"))
        sm.add_widget(RaceScreen(name="race"))
        sm.add_widget(RunningDistances(name="running"))
        sm.add_widget(CyclingScreen(name="cycle"))
        sm.add_widget(SwimmingScreen(name="swim"))

        # Running Screens2
        sm.add_widget(RunningTimeScreen(
            name="RunningTimeMarathon",
            distance="Marathon"))
        sm.add_widget(RunningTimeScreen(
            name="RunningTimeHalf",
            distance="Half-Marathon"))
        sm.add_widget(RunningTimeScreen(
            name="RunningTime10k",
            distance="10K"))
        sm.add_widget(RunningTimeScreen(
            name="RunningTime5k",
            distance="5K"))

        sm.add_widget(LevelScreen(name="level"))
        sm.add_widget(RunningInfoScreen(name="runningInfo"))

        # Swimming DefaultScreens
        sm.add_widget(SwimmingPace(
            name="Pace400M",
            distance="400M"
        ))
        sm.add_widget(SwimmingPace(
            name="Pace1500M",
            distance="1500M"
        ))
        sm.add_widget(SwimmingPace(
            name="Pace3000M",
            distance="3000M"
        ))
        sm.add_widget(SwimmingPace(
            name="Pace5000M",
            distance="5000M"
        ))

        # Cycling DefaultScreens
        sm.add_widget(CyclingTimeScreen(
            name="Cycling20K",
            distance="20K"
        ))
        sm.add_widget(CyclingTimeScreen(
            name="Cycling50K",
            distance="50K"
        ))
        sm.add_widget(CyclingTimeScreen(
            name="Cycling100K",
            distance="100K"
        ))
        sm.add_widget(CyclingTimeScreen(
            name="Cycling160K",
            distance="160K"
        ))

        sm.add_widget(BuildPlan(name="BuildPlan"))
        sm.add_widget(PlanPage(name="plan"))

        return sm


if __name__ == "__main__":
    # Run App
    MainApp().run()
