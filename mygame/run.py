import settings
import glfw
import pyrr
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader

from piengine import Game
from piengine import Piengine
from piengine import Shader
from piengine import Model
from piengine import Callback
from piengine import Settings
from piengine import Camera

class MyGame(Game):

    def __init__(self, **window):
        super().__init__(**window)
        glfw.init()

    def initialize(self, window):
        ### CALLBACKS
        #glfw.set_cursor_enter_callback(window, Callback.mouse_enter_clb)
        #glfw.set_cursor_pos_callback(window, Callback.mouse_look_clb)
        glfw.set_key_callback(window, Callback.key_input_clb)
        glfw.set_input_mode(window, glfw.CURSOR, glfw.CURSOR_DISABLED)

        # Shader
        self.shader = Shader(
            Settings.get_base_directory() + "/assets/shaders/vertex.glsl",
            Settings.get_base_directory() + "/assets/shaders/fragment.glsl"
        )

        self.camera = Camera()
        self.camera.set_position(pyrr.Vector3([0, 0, 0]))

        # model
        self.model = Model(shader=self.shader.getShader(), textured=True, normals=True)
        self.model.load_mesh(Settings.get_base_directory() + "/assets/meshes/stall.obj")
        self.model.load_texture(Settings.get_base_directory() + "/assets/textures/stallTexture.png")
        self.model.set_projection(Settings.get_width() / Settings.get_height())
        self.model.set_position(pyrr.Vector3([0, 0, -50]))
        self.model.set_uniform_location()
        self.model.set_uniform_matrix()

    def update(self, currentime):
        self.model.set_rotation_y(currentime)
        self.model.set_camera_view(Callback.camera.get_view_matrix())
        Callback.do_move()

    def render(self):
        self.model.render()

    def close(self):
        self.model.clean()


if __name__ == "__main__":

    settings.init()
    piengine = Piengine(
        MyGame(
            title=Settings.get_title(),
            width=Settings.get_width(),
            height=Settings.get_height()
        )
    )
    piengine.run()
