from pygame.draw import rect
from pygame.mixer import music

class Color():
    def __init__(self, x, y, box_size):
        self._x = x
        self._y = y
        self._box_size = box_size
        self.color = None
        self.sound = 0

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def draw(self, surface):
        """ Draws the box """
        rect(surface, self.color, (self.x, self.y, self.box_size, self._box_size))

    def play(self):
        """ Plays coresponding sound """
        self.sound.play(0)

class Red(Color):
    def __init__(self, x, y, box_size):
        super().__init__()
        self.color = (255, 0, 0)
        self.sound = music.load('sound/red.wav')

class Green(Color):
    def __init__(self, x, y, box_size):
        super().__init__()
        self.color = (0, 255, 0)
        self.sound = music.load('sound/green.wav')

class Blue(Color):
    def __init__(self, x, y, box_size):
        super().__init__()
        self.color = (0, 0, 255)
        self.sound = music.load('sound/blue.wav')

class Yellow(Color):
    def __init__(self, x, y, box_size):
        super().__init__()
        self.color = (255, 255, 0)
        self.sound = music.load('sound/yellow.wav')
