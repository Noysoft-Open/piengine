import numpy

class OBJloader:

    def __init__(self):
        self.raw_vertices   = []
        self.raw_textures   = []
        self.raw_normals    = []
        self.raw_faces      = []
        self.raw_indices    = []
        self.final_raw      = []
        self.vertices       = numpy.array([], dtype=numpy.float64)
        self.textures       = numpy.array([], dtype=numpy.float64)
        self.normals        = numpy.array([], dtype=numpy.float64)
        self.faces          = numpy.array([], dtype=numpy.uint32)

    def load_data(self, filepath):
        try:
            file = open(filepath, 'r')
        except:
            raise Exception("File not found: %s" % filepath)
        for line in file:
            line = line.split()
            if line[0] == 'v':
                self.raw_vertices.append(line[1:])
            if line[0] == 'vt':
                self.raw_textures.append(line[1:])
            if line[0] == 'vn':
                self.raw_normals.append(line[1:])
            if line[0] == 'f':
                for value in line[1:]:
                    value = value.split('/')
                    self.raw_faces.append(value)
                    self.raw_indices.append(value[0])
        file.close()
        self.assign_data_types()
        self.indexed_data()

    def assign_data_types(self):
        f_temp = []
        self.vertices = numpy.array(self.raw_vertices, dtype=numpy.float64)
        self.textures = numpy.array(self.raw_textures, dtype=numpy.float64)
        self.normals = numpy.array(self.raw_normals, dtype= numpy.float64)
        for face in self.raw_faces:
            for value in face:
                f_temp.append(int(value)-1)
        self.faces = numpy.array(f_temp, dtype=numpy.int64)

    def indexed_data(self):
        identity = 'v'
        for index in self.faces:
            if identity == 'v':
                self.final_raw.extend(self.vertices[index])
                identity = 'vt'
            elif identity == 'vt':
                self.final_raw.extend(self.textures[index])
                identity = 'vn'
            elif identity == 'vn':
                self.final_raw.extend(self.normals[index])
                identity = 'v'

    def get_indexed_data(self):
        return numpy.array(self.final_raw, dtype=numpy.float32)

    def get_index(self):
        return numpy.array(self.raw_indices, dtype=numpy.uint32)
