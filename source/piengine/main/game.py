
class Game:

    def __init__(self, **window):
        self.title = window['title']
        self.width = window['width']
        self.height = window['height']

    def initialize(self, window):
        pass

    def update(self, currentime):
        pass

    def render(self):
        pass

    def close(self):
        pass

    def __str__(self):
        return self.title

    def get_title(self):
        return self.title

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height
