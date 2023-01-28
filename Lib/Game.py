import pygame
import sys
from Lib import Grid


class Game:
    def __init__(self):
        self.dimensions = (800, 600)
        self.screen = None
        self.start_game()

    def start_game(self):
        """
        Start the game
        :return:
        """
        pygame.init()

        grid = Grid.Grids(10, 10, ["asparagus", "potatoes", "basil"])
        grid.make_plants()

        black = 0, 0, 0
        self.screen = pygame.display.set_mode(self.dimensions)
        while True:
            self.screen.fill(black)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    break
            pygame.display.flip()
