import pygame
from constants import *


class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.width = TILE_SIZE
        self.height = TILE_SIZE


    def draw(self, screen):
        pass  # Override this method in the child class to draw the sprite

    def update(self, dt):
        pass # Override this method in the child class to update the sprite