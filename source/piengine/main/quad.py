from OpenGL.GL import * 
import numpy 

class Quad:

    def __init__(self):

        self.vertices = [
            -0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
             0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
            -0.5,  0.5, 0.0, 0.0, 0.0, 1.0,
             0.5,  0.5, 0.0, 1.0, 1.0, 1.0
        ]

        self.vertices = numpy.array(self.vertices, dtype=numpy.float32)

        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo )
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))

    def draw(self, shader):
        glUseProgram(shader)
        glDrawArrays(GL_TRIANGLE_STRIP, 0, 4)

    def delete(self):
        pass