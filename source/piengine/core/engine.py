import glfw
from OpenGL.GL import *
from .window import Piewindow

class Piengine:

    def __init__(self, game):
    
        if not glfw.init():
            return

        self.piewindow = Piewindow(
            title=game.getTitle(), 
            width=game.getWidth(), 
            height=game.getHeight()
        )
 
        self.game = game

    def mainloop(self):
        
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        self.game.initialize(self.piewindow.getWindow())
        
        fps = 1.0 / 60.0
        lastime = glfw.get_time()
        timer = lastime
        deltatime = 0.0
        currentime = 0.0
        frame = 0


        while not glfw.window_should_close(self.piewindow.getWindow()):

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
                    self.piewindow.getWindow(),
                    self.piewindow.getTitle() + fpstring
                )
                frame=0

            glfw.swap_buffers(self.piewindow.getWindow())

    def stop(self):
        glfw.terminate()
        self.game.close()

    def run(self):
        self.piewindow.initialize()
        self.mainloop()
        self.stop()