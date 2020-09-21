import pygame
from abc import ABC, abstractmethod

class Color(ABC):
    def __init__(self, x, y, box_size):
        self._x = x
        self._y = y
        self._box_size = box_size

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @abstractmethod
    def draw(self, surface):
        """ Draws the box """
        pass

    @abstractmethod
    def play(self):
        """ Plays coresponding sound """
        pass

class Red(Color):
    def __init__(self, x, y, box_size):
        super().__init__()
        self.color = (255, 0, 0)

    def draw(self, surface):
        """ Draws the box """
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.box_size, self._box_size))

    def play(self):
        pass

class Green(Color):
    def __init__(self, x, y, box_size):
        super().__init__()
        self.color = (0, 255, 0)

    def draw(self, surface):
        """ Draws the box """
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.box_size, self._box_size))

    def play(self):
        pass

class Blue(Color):
    def __init__(self, x, y, box_size):
        super().__init__()
        self.color = (0, 0, 255)

    def draw(self, surface):
        """ Draws the box """
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.box_size, self._box_size))

    def play(self):
        pass

class Yellow(Color):
    def __init__(self, x, y, box_size):
        super().__init__()
        self.color = (255, 255, 0)

    def draw(self, surface):
        """ Draws the box """
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.box_size, self._box_size))

    def play(self):
        pass
