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

        # # model
        # self.model = Model(shader=self.shader.get_shader())
        # self.model.load_mesh(self.piesettings.get_base_directory() + "/assets/meshes/dragon.obj")
        # self.model.load_texture(self.piesettings.get_base_directory() + "/assets/textures/chibi.png")
        # self.model.set_projection(self.piesettings.get_width() / self.piesettings.get_height())
        # self.model.set_position(pyrr.Vector3([0, 0, -50]))
        # self.model.set_uniform_location()
        # self.model.set_uniform_matrix()

        # chibi
        self.chibi = Model(shader=self.shader.get_shader())
        self.chibi.load_mesh(self.piesettings.get_base_directory() + "/assets/meshes/chibi.obj")
        self.chibi.load_texture(self.piesettings.get_base_directory() + "/assets/textures/chibi.png")
        self.chibi.set_projection(self.piesettings.get_width() / self.piesettings.get_height())
        self.chibi.set_position(pyrr.Vector3([0, 0, 0]))
        self.chibi.set_uniform_location()
        self.chibi.set_uniform_matrix()
        self.chibi.set_scale(0.2)
        

        # stall 
        self.stall = Model(shader=self.shader.get_shader())
        self.stall.load_mesh(self.piesettings.get_base_directory() + "/assets/meshes/stall.obj")
        self.stall.load_texture(self.piesettings.get_base_directory() + "/assets/textures/stallTexture.png")
        self.stall.set_projection(self.piesettings.get_width() / self.piesettings.get_height())
        self.stall.set_position(pyrr.Vector3([20, 0, -50]))
        self.stall.set_uniform_location()
        self.stall.set_uniform_matrix()
        self.stall.set_scale(1)
        self.stall.set_rotation_y(1, 3.18)

        # building
        self.building = Model(shader=self.shader.get_shader())
        self.building.load_mesh(self.piesettings.get_base_directory() + "/assets/meshes/dragon.obj")
        self.building.load_texture(self.piesettings.get_base_directory() + "/assets/textures/cottage.png")
        self.building.set_projection(self.piesettings.get_width() / self.piesettings.get_height())
        self.building.set_position(pyrr.Vector3([0, 0, -50]))
        self.building.set_uniform_location()
        self.building.set_uniform_matrix()
        self.building.set_scale(1)


    def update(self, currentime):
        #self.chibi.set_rotation_z(currentime, 0.8)
        #self.model.set_rotation_x(currentime, 0.8)
        #self.stall.set_rotation_y(currentime, 0.8)
        #self.stall.set_camera_view(Callback.camera.get_view_matrix())
        Callback.move()
        self.chibi.set_position(pyrr.Vector3([
            Callback.camera.get_camera_position().x,
            Callback.camera.get_camera_position().y - 4,
            Callback.camera.get_camera_position().z - 15]))
        self.chibi.set_camera_view(Callback.camera.get_view_matrix())
        self.chibi.set_rotation_y(1, 3.2)

    def render(self):
        #self.model.render()
        self.chibi.render()
        self.stall.render()
        self.building.render()

    def close(self):
        #self.model.clean()
        self.chibi.clean()
        self.stall.clean()
        self.building.clean()
        Callback.close()

if __name__ == "__main__":
    mysettings = MySettings()
    Piengine(MyGame(mysettings.get_settings())).run()
 

 