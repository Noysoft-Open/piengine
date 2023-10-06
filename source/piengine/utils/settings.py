
class Piesettings:

    def __init__(self):
        self.base_directory = ""
        self.title = ""
        self.width = 0
        self.height = 0

    def set_base_directory(self, base_dir):
        self.base_directory = base_dir

    def set_window_dimension(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

    def get_title(self):
        return self.title

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_base_directory(self):
        return self.base_directory
