
from ..utils.settings import Piesettings

class Game:

    def __init__(self):
        self.piesettings = Piesettings()

    def initialize(self, window):
        pass

    def update(self, currentime):
        pass

    def render(self):
        pass

    def close(self):
        pass

    def __str__(self):
        return self.piesettings.get_title()

    def get_title(self):
        return self.piesettings.get_title()

    def get_width(self):
        return self.piesettings.get_width()

    def get_height(self):
        return self.piesettings.get_height()
