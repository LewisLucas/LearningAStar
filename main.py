from constants import *
import pygame


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = TILE_SIZE
        self.height = TILE_SIZE


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.tiles = [Tile(0, 0), Tile(1, 0), Tile(2, 0), Tile(3, 0), Tile(4, 0)]

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            self.screen.fill(WHITE)
            for tile in self.tiles:
                pygame.draw.rect(self.screen, RED, (tile.x * TILE_SIZE, tile.y * TILE_SIZE, tile.width, tile.height))
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    app = Game()
    app.run()