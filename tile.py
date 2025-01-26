import pygame
from sprite import Sprite
from constants import *


class Tile(Sprite):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.width = TILE_SIZE
        self.height = TILE_SIZE


    def draw(self, screen, color=RED):
        pygame.draw.rect(screen, color, (self.x * TILE_SIZE, self.y * TILE_SIZE, self.width, self.height))


class Wall(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = DARK_GREY

    def draw(self, screen):
        super().draw(screen, self.color)

class Floor(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = GREY

    def draw(self, screen):
        return super().draw(screen, self.color)