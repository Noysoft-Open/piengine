from OpenGL.GL import *
from OpenGL.GL.shaders import compileShader, compileProgram

class Shader:

    def __init__(self, vertexfilepath, fragmentfilepath):
        self.vertexfilepath = vertexfilepath
        self.fragmentfilepath = fragmentfilepath
        self.shader = self.compile()

    def compile(self):
        with open(self.vertexfilepath, 'r') as f:
            vertex_src = f.readlines()
        with open(self.fragmentfilepath, 'r') as f:
            fragment_src = f.readlines()
        
        shader = compileProgram(
            compileShader(vertex_src, GL_VERTEX_SHADER),
            compileShader(fragment_src, GL_FRAGMENT_SHADER)
        )

        return shader
    
    def getShader(self):
        return self.shader