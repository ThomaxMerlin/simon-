import pygame
from abc import ABC, abstractmethod

class Color(ABC):
    def __init__(self, x, y, box_size):
        self.color = None
        self.sound = None

    @abstractmethod
    def draw(surface):
        pass

    @abstractmethod
    def play(surface):
        pass