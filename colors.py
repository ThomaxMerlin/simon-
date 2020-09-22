from pygame.draw import rect
from pygame.mixer import Sound

class Color():
    def __init__(self, x, y, box_size):
        self._x = x
        self._y = y
        self.box_size = box_size

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def draw(self, surface):
        """ Draws the box """
        self.surface = rect(surface, self.color, (self.x, self.y, self.box_size, self.box_size))

    def play(self):
        """ Plays coresponding sound """
        self.sound.play()

class Red(Color):
    def __init__(self, x, y, box_size):
        super().__init__(x, y, box_size)
        self.color = (255, 0, 0)
        self.sound = Sound('sound/red.wav')

class Green(Color):
    def __init__(self, x, y, box_size):
        super().__init__(x, y, box_size)
        self.color = (0, 255, 0)
        self.sound = Sound('sound/green.wav')

class Blue(Color):
    def __init__(self, x, y, box_size):
        super().__init__(x, y, box_size)
        self.color = (0, 0, 255)
        self.sound = Sound('sound/blue.wav')

class Yellow(Color):
    def __init__(self, x, y, box_size):
        super().__init__(x, y, box_size)
        self.color = (255, 255, 0)
        self.sound = Sound('sound/yellow.wav')
