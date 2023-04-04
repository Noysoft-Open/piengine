import glfw
from OpenGL.GL import *

class Piewindow:

    def __init__(self, **window):
        self.title = window['title']
        self.width = window['width']
        self.height = window['height']
        self.window = None

    def initialize(self):
        if not glfw.init():
            return

        self.set_context_hints()

        self.window = glfw.create_window(
            self.width,
            self.height,
            self.title,
            None,
            None,
        )
        if not self.window:
            glfw.terminate()

        monitor = glfw.get_primary_monitor()
        vidmode = glfw.get_video_mode(monitor)

        max_width = vidmode.size.width
        max_height = vidmode.size.height

        glfw.set_window_pos(
            self.window,
            int((max_width/2)-(self.width/2)),
            int((max_height/2)-(self.height/2))
        )

        glfw.make_context_current(self.window)
        glViewport(0, 0, self.width, self.height)

    def set_window(self):
        self.window = glfw.create_window(
            self.width,
            self.height,
            self.title,
            None,
            None,
        )
        if not self.window:
            glfw.terminate()

    def set_context_hints(self):
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 0)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, True)
        glfw.window_hint(glfw.SAMPLES, 4)
        glfw.window_hint(glfw.RESIZABLE, False)

    def set_context(self, window):
        glfw.make_context_current(window)

    def get_window(self):
        return self.window

    def get_title(self):
        return self.title

    def get_window_size(self):
        return [self.width, self.height]
