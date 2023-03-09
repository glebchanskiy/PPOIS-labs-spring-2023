from kivymd.app import MDApp

from lab2.app.services.controller import Controller
from lab2.app.services.model import Model
import os

class App(MDApp):
    model = None
    controller = None

    def on_start(self):
        pass

        # self.fps_monitor_start()

    def build(self):
        self.title = 'Kono Dio da'
        self.icon = os.path.join(os.path.dirname(os.path.realpath(__file__)), "asserts/icon.tiff")
        self.theme_cls.primary_palette = "Teal"
        
        self.controller = Controller()
        return self.controller.get_view()
