import glfw
import pyrr
from settings import MySettings

from piengine import Game
from piengine import Piengine
from piengine import Shader
from piengine import Model
from piengine import Callback
from piengine import Camera
from piengine import Piesettings

class MyGame(Game):

    def __init__(self, settings):
        super().__init__()
        glfw.init()
        self.piesettings = settings

    def initialize(self, window):
        ### CALLBACKS
        #glfw.set_cursor_enter_callback(window, Callback.mouse_enter_clb)
        #glfw.set_cursor_pos_callback(window, Callback.mouse_look_clb)
        glfw.set_key_callback(window, Callback.key_input_clb)
        #glfw.set_input_mode(window, glfw.CURSOR, glfw.CURSOR_DISABLED)

        # Shader
        self.shader = Shader(
            self.piesettings.get_base_directory() + "/assets/shaders/vertex.glsl",
            self.piesettings.get_base_directory() + "/assets/shaders/fragment.glsl"
        )

        self.camera = Camera()
        self.camera.set_position(pyrr.Vector3([0, 0, 0]))

        # model
        self.model = Model(shader=self.shader.get_shader(), textured=True, normals=True)
        self.model.load_mesh(self.piesettings.get_base_directory() + "/assets/meshes/floor.obj")
        self.model.load_texture(self.piesettings.get_base_directory() + "/assets/textures/floor.jpg")
        self.model.set_projection(self.piesettings.get_width() / self.piesettings.get_height())
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
        Callback.close()

if __name__ == "__main__":
    mysettings = MySettings()
    mysettings.set()
    Piengine(MyGame(mysettings.get_settings())).run()
