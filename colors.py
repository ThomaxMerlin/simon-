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
    def play(self, surface):
        """ Plays coresponding sound """
        pass
