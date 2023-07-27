import glfw
from OpenGL.GL import *
from .window import Piewindow

class Piengine:

    def __init__(self, game):

        if not glfw.init():
            return

        self.piewindow = Piewindow(
            title=game.get_title(),
            width=game.get_width(),
            height=game.get_height()
        )

        self.game = game

    def mainloop(self):
        
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        self.game.initialize(self.piewindow.get_window())

        fps = 1.0 / 60.0
        lastime = glfw.get_time()
        timer = lastime
        deltatime = 0.0
        currentime = 0.0
        frame = 0

        while not glfw.window_should_close(self.piewindow.get_window()):

            glfw.poll_events()
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            glClearColor(0.1, 0.1, 0.1, 1)

            currentime = glfw.get_time()
            deltatime += (currentime - lastime) / fps
            lastime = currentime

            while deltatime >= 1.0:
                self.game.update(currentime)
                deltatime-=1.0

            # render
            self.game.render()

            frame+=1
            if glfw.get_time() - timer > 1.0:
                timer+=1
                fpstring = " | FPS: %s" % frame
                glfw.set_window_title(
                    self.piewindow.get_window(),
                    self.piewindow.get_title() + fpstring
                )
                frame=0

            glfw.swap_buffers(self.piewindow.get_window())

    def stop(self):
        self.game.close()
        glfw.terminate()

    def run(self):
        #self.piewindow.set_full_screen()
        self.piewindow.set_window()
        self.mainloop()
        self.stop()
