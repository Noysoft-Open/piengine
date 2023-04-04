import os
from pathlib import Path
from piengine import Piesettings

class MySettings:

    def __init__(self):
        self.title = "My Game"
        self.width = 1200
        self.height = 680
        self.base_directory = Path(__file__).resolve().parent.parent
        self.piesettings = Piesettings()

    def set(self):
        self.piesettings.set_base_directory(os.path.join(self.base_directory, "mygame"))
        self.piesettings.set_window_dimension(self.title, self.width, self.height)

    def get_settings(self):
        return self.piesettings
