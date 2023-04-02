import glfw
from piengine import Camera
from piengine import Piesettings
from OpenGL.GL import *

class Callback:

    glfw.init()

    camera = Camera()
    piesettings = Piesettings()

    LAST_X = piesettings.get_width() / 2
    LAST_Y = piesettings.get_height() / 2
    FIRST_MOUSE = True
    LEFT = False
    RIGHT = False
    FORWARD = False
    BACKWARD = False
    UP = False
    DOWN = False

    def key_input_clb(window, key, scancode, action, mode):
        if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
            glfw.set_window_should_close(window, True)

        if key == glfw.KEY_W and action == glfw.PRESS:
            Callback.FORWARD = True
        elif key == glfw.KEY_W and action == glfw.RELEASE:
            Callback.FORWARD = False

        if key == glfw.KEY_S and action == glfw.PRESS:
            Callback.BACKWARD = True
        elif key == glfw.KEY_S and action == glfw.RELEASE:
            Callback.BACKWARD = False

        if key == glfw.KEY_A and action == glfw.PRESS or \
           key == glfw.KEY_LEFT and action == glfw.PRESS:
            Callback.LEFT = True
        elif key == glfw.KEY_A and action == glfw.RELEASE or \
           key == glfw.KEY_LEFT and action == glfw.RELEASE:
            Callback.LEFT = False

        if key == glfw.KEY_D and action == glfw.PRESS or \
           key == glfw.KEY_RIGHT and action == glfw.PRESS:
            Callback.RIGHT = True
        elif key == glfw.KEY_D and action == glfw.RELEASE or \
           key == glfw.KEY_RIGHT and action == glfw.RELEASE:
            Callback.RIGHT = False

        if key == glfw.KEY_UP and action == glfw.PRESS:
            Callback.UP = True
        elif key == glfw.KEY_UP and action == glfw.RELEASE:
            Callback.UP = False

        if key == glfw.KEY_DOWN and action == glfw.PRESS:
            Callback.DOWN = True
        elif key == glfw.KEY_DOWN and action == glfw.RELEASE:
            Callback.DOWN = False

        if key == glfw.KEY_F and action == glfw.PRESS:
            if not Callback.CLICKED:
                Callback.FULL_SCREEN = True
                Callback.CLICKED = True
            else:
                Callback.FULL_SCREEN = False
                Callback.CLICKED = False

    def do_move():
        if Callback.LEFT:
            Callback.camera.process_keyboard("LEFT", 0.2)
        if Callback.RIGHT:
            Callback.camera.process_keyboard("RIGHT", 0.2)
        if Callback.FORWARD:
            Callback.camera.process_keyboard("FORWARD", 0.2)
        if Callback.BACKWARD:
            Callback.camera.process_keyboard("BACKWARD", 0.2)
        if Callback.UP:
            Callback.camera.process_keyboard('UP', 0.2)
        if Callback.DOWN:
            Callback.camera.process_keyboard('DOWN', 0.2)

    def mouse_look_clb(window, xpos, ypos):
        if Callback.FIRST_MOUSE:
            Callback.LAST_X = xpos
            Callback.LAST_Y = ypos

        xoffset = xpos - Callback.LAST_X
        yoffset = Callback.LAST_Y  - ypos

        Callback.LAST_X = xpos
        Callback.LAST_Y = ypos

        Callback.camera.process_mouse_movement(xoffset, yoffset)

    def mouse_enter_clb(window, entered):
        if entered:
            Callback.FIRST_MOUSE = False
        else:
            Callback.FIRST_MOUSE = True

    def close():
        glfw.terminate()
