import pygame as pg
import os
import sys

class Game:
    def __init__(self):
        self.dimensions = (1200, 800)
        self.screen = None
        self.grid = None
        self.background = None
        self.start_game()

    def start_game(self):
        """
        Start the game
        :return:
        """
        pg.init()
        black = 0, 0, 0
        self.screen = pg.display.set_mode(self.dimensions)
        self.background = pg.image.load(os.path.join('./ResourcesLib/images', 'background.jpg'))
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
            self.screen.fill(black)
            self.screen.blit(self.background, (0, 0))
            pg.display.flip()
