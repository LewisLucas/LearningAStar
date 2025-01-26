from constants import *
from sprite import Sprite
import pygame


class Player(Sprite):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.width = PLAYER_SIZE
        self.height = PLAYER_SIZE
        self.color = BLUE
        self.move_delay = 0

    def draw(self, screen):
        # Draw the player in the center of the tile 
        pygame.draw.rect(screen, self.color, (self.x * TILE_SIZE + (TILE_SIZE - self.width) // 2,
                                              self.y * TILE_SIZE + (TILE_SIZE - self.height) // 2, self.width, self.height))

    def update(self, dt, collidables):
        self.move(self, dt, collidables)

    def move(self, dt, collidables):
        if self.move_delay > 0:
            self.move_delay -= dt
            return
        