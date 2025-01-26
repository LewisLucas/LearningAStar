from constants import *
import pygame
from tile import Tile, Wall, Floor
from player import Player
import sys


class Game:
    def __init__(self):
        # Initialize Pygame
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.dt = 0
        
        # Create Sprite groups
        self.updateable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group() 
        self.walls = pygame.sprite.Group()
        self.collidables = pygame.sprite.Group()

        # Assign sprite groups to Tile class 
        Tile.containers = (self.drawable)
        Wall.containers = (self.walls, self.drawable, self.collidables)   
        Player.containers = (self.updateable, self.drawable, self.collidables)

        # 2d array of the map
        self.map = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]

        # Create the map
        for y, row in enumerate(self.map):
            for x, tile in enumerate(row):
                if tile == 1:
                    Wall(x, y)
                else:
                    Floor(x, y)

        # Create the player
        self.player = Player(1, 1)

    def run(self):
        while True:
            # Limit the frame rate and get delta time
            self.dt = self.clock.tick(60) / 1000.0

            # Pygame events
            self.events()

            # Update all the updateable objects
            self.update()

            # Draw all the drawable objects
            self.draw()

    def events(self):
        # Handle the pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    def update(self):
        # Update all the updateable objects
        for updateable in self.updateable:
            updateable.update(self.dt, self.collidables)

    def draw(self):
        # Clear the screen
        self.screen.fill(WHITE)

        # Draw all the drawable objects
        for drawable in self.drawable:
            drawable.draw(self.screen)

        # Update the display
        pygame.display.flip()

if __name__ == '__main__':
    app = Game()
    app.run()