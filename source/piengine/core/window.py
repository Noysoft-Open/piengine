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
        
        self.setContextHints()

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

    def setWindow(self):
        self.window = glfw.create_window(
            self.width, 
            self.height, 
            self.title,
            None, 
            None, 
        )
        if not self.window:
            glfw.terminate()

    def setContextHints(self):
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 0)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, False)
        glfw.window_hint(glfw.SAMPLES, 4)
        glfw.window_hint(glfw.RESIZABLE, False)


    def setContext(self, window):
        glfw.make_context_current(window)

    def getWindow(self):
        return self.window
    
    def getTitle(self):
        return self.title
    
    def getWindowSize(self):
        return [self.width, self.height]

