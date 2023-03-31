
class Settings:

    BASE_DIRECTORY = ""
    TITLE = ""
    WIDTH = 0 
    HEIGHT = 0
    
    def set_base_directory(path):
        Settings.BASE_DIRECTORY = path

    def set_window_dimension(title, width, height):
        Settings.TITLE = title 
        Settings.WIDTH = width 
        Settings.HEIGHT = height

    def get_title():
        return Settings.TITLE

    def get_width():
        return Settings.WIDTH 
    
    def get_height():
        return Settings.HEIGHT

    def get_base_directory():
        return Settings.BASE_DIRECTORY

    def print_something():
        print(Settings.BASE_DIRECTORY)







