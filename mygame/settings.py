import os
from pathlib import Path
from piengine import Settings


def init():
    base = Path(__file__).resolve().parent.parent
    Settings.set_base_directory(os.path.join(base, "mygame"))
    Settings.set_window_dimension("My Game", 1200, 680)
    Settings.print_something()