import glfw
import pyrr
import numpy
from OpenGL.GL import *
from PIL import Image

from ..core.objectldr import OBJloader

class Model:

    def __init__(self, **modelargs):
        glfw.init()
        self.vertices    = None
        self.indices     = None
        self.model_loc   = None
        self.proj_loc    = None
        self.view_loc    = None
        self.projection  = None
        self.view        = None
        self.position    = None
        self.newposition = None
        self.model       = None
        self.temp_model  = None
        self.scale       = None
        self.scaled      = False
        self.shader      = modelargs['shader']
        self.vao         = glGenVertexArrays(1)
        self.vbo         = glGenBuffers(1)
        self.texture     = glGenTextures(1)
        self.objldr      = OBJloader()

    def load_mesh(self, filepath):
        self.objldr.load_data(filepath)
        self.vertices = self.objldr.get_indexed_data()
        self.indices = self.objldr.get_index()
        # vao
        glBindVertexArray(self.vao)
        # vertex buffer object
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)
        # vertices
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, self.vertices.itemsize * 8, ctypes.c_void_p(0))
        # textures
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, self.vertices.itemsize * 8, ctypes.c_void_p(12))
        # normals
        glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, self.vertices.itemsize * 8, ctypes.c_void_p(20))
        glEnableVertexAttribArray(2)

    def load_texture(self, filepath):
        glBindTexture(GL_TEXTURE_2D, self.texture)
        # Set the texture wrapping parameters
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        # Set texture filtering parameters
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        image = Image.open(filepath)
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
        img_data = image.convert("RGBA").tobytes()
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.width, image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)

    def set_uniform_location(self):
        self.model_loc = glGetUniformLocation(self.shader, "model")
        self.proj_loc = glGetUniformLocation(self.shader, "projection")
        self.view_loc = glGetUniformLocation(self.shader, "view")

    def set_uniform_matrix(self):
        glUseProgram(self.shader)
        glUniformMatrix4fv(self.proj_loc, 1, GL_FALSE, self.projection)
        #glUniformMatrix4fv(self.view_loc, 1, GL_FALSE, self.view)

    def set_projection(self, aspect_ratio):
        self.projection = pyrr.matrix44.create_perspective_projection_matrix(45, aspect_ratio, 0.1, 100)
        #self.view = pyrr.matrix44.create_look_at(pyrr.Vector3([0, 0, 10]), pyrr.Vector3([0, 0, 0]), pyrr.Vector3([0, 1, 0]))

    def set_camera_view(self, camera_view):
        self.view = camera_view
        glUniformMatrix4fv(self.view_loc, 1, GL_FALSE, self.view)

    def set_position(self, position):
        self.position = pyrr.matrix44.create_from_translation(position)
        self.model = pyrr.matrix44.multiply(
            pyrr.matrix44.create_from_translation(
                pyrr.Vector3([1, 1, 1])
            ),
            self.position
        )

    def set_rotation_y(self, time, speed):
        rotation_y = pyrr.matrix44.create_from_y_rotation(speed * time)
        if self.scaled:
            self.temp_model = pyrr.matrix44.multiply(rotation_y, self.scale)
            self.model = pyrr.matrix44.multiply(self.temp_model, self.position)
        else:
            self.model = pyrr.matrix44.multiply(rotation_y, self.position)

    def set_rotation_x(self, time, speed):
        rotation_x = pyrr.matrix44.create_from_x_rotation(speed * time)
        if self.scaled:
            self.temp_model = pyrr.matrix44.multiply(rotation_x, self.scale)
            self.model = pyrr.matrix44.multiply(self.temp_model, self.position)
        else:
            self.model = pyrr.matrix44.multiply(rotation_x, self.position)

    def set_rotation_z(self, time, speed):
        rotation_z = pyrr.matrix44.create_from_z_rotation(speed * time)
        if self.scaled:
            self.temp_model = pyrr.matrix44.multiply(rotation_z, self.scale)
            self.model = pyrr.matrix44.multiply(self.temp_model, self.position)
        else:
            self.model = pyrr.matrix44.multiply(rotation_z, self.position)

    def set_scale(self, size):
        self.scaled = True
        self.scale = pyrr.matrix44.create_from_scale(pyrr.Vector4([size, size, size, 1]))
        self.model = pyrr.matrix44.multiply(self.scale, self.position)

    def move(self, newposition):
        self.newposition = pyrr.matrix44.create_from_translation(newposition)
        self.model = pyrr.matrix44.multiply(self.newposition, self.position)

    def get_position(self):
        return self.position

    def get_new_position(self):
        return self.newposition

    def render(self):
        glBindVertexArray(self.vao)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glUniformMatrix4fv(self.model_loc, 1, GL_FALSE, self.model)
        glDrawArrays(GL_TRIANGLES, 0, len(self.indices))

    def clean(self):
        glfw.terminate()
