import glfw
import pyrr
from settings import MySettings

from piengine import Game
from piengine import Piengine
from piengine import Shader
from piengine import Model
from piengine import Callback
from piengine import Camera

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
        self.model = Model(shader=self.shader.get_shader())
        self.model.load_mesh(self.piesettings.get_base_directory() + "/assets/meshes/dragon.obj")
        self.model.load_texture(self.piesettings.get_base_directory() + "/assets/textures/chibi.png")
        self.model.set_projection(self.piesettings.get_width() / self.piesettings.get_height())
        self.model.set_position(pyrr.Vector3([0, 0, -50]))
        self.model.set_uniform_location()
        self.model.set_uniform_matrix()

        # chibi
        self.chibi = Model(shader=self.shader.get_shader())
        self.chibi.load_mesh(self.piesettings.get_base_directory() + "/assets/meshes/chibi.obj")
        self.chibi.load_texture(self.piesettings.get_base_directory() + "/assets/textures/chibi.png")
        self.chibi.set_projection(self.piesettings.get_width() / self.piesettings.get_height())
        self.chibi.set_position(pyrr.Vector3([-20, 0, -50]))
        self.chibi.set_uniform_location()
        self.chibi.set_uniform_matrix()
        self.chibi.set_scale(0.5)

        # stall 
        self.stall = Model(shader=self.shader.get_shader())
        self.stall.load_mesh(self.piesettings.get_base_directory() + "/assets/meshes/stall.obj")
        self.stall.load_texture(self.piesettings.get_base_directory() + "/assets/textures/stallTexture.png")
        self.stall.set_projection(self.piesettings.get_width() / self.piesettings.get_height())
        self.stall.set_position(pyrr.Vector3([20, 0, -50]))
        self.stall.set_uniform_location()
        self.stall.set_uniform_matrix()

    def update(self, currentime):
        self.chibi.set_rotation_z(currentime, 0.8)
        self.model.set_rotation_x(currentime, 0.8)
        self.stall.set_rotation_y(currentime, 0.8)
        self.model.set_camera_view(Callback.camera.get_view_matrix())
        Callback.do_move()

    def render(self):
        self.model.render()
        self.chibi.render()
        self.stall.render()

    def close(self):
        self.model.clean()
        self.chibi.clean()
        self.stall.clean()
        Callback.close()

if __name__ == "__main__":
    mysettings = MySettings()
    mysettings.set()
    Piengine(MyGame(mysettings.get_settings())).run()
 

 