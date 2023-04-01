import os
import glfw
from OpenGL.GL import *
from pathlib import Path
from piengine import Settings

WIDTH = 1200
HEIGHT = 680

def init():
    base = Path(__file__).resolve().parent.parent
    Settings.set_base_directory(os.path.join(base, "mygame"))
    Settings.set_window_dimension("My Game", WIDTH, HEIGHT)
    Settings.print_something()

def mouse_cursor(window):
    glfw.init()
