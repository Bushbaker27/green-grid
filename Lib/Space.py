import pygame as pg
from Lib import Grid, Game
class Space:
    """
    A space is a single cell in the grid.
    It can contain a plant or nothing.
    """
    def __init__(self, location, game):
        self.game = game
        self.item = None
        self.color = pg.Color('gray')
        self.location = location
        self.scale = 10
        info = pg.display.Info()
        self.gridWidth = info.current_w/2
        self.gridHeight = info.current_h/2

    def draw(self, screen):
        pg.init()
        """
        Draws the space to the screen.
        :param screen:
        :return:
        """
        # The rectangle of the space.
        #info = pg.display.Info()
        #print(info.center_w)
        #widthCenter = info.center_w/2
        #widthHeight = info.center_h/2
        space_rect = pg.Rect((self.gridWidth + 5 + (((int(self.game.veggie_trays[17][1]) / 2)*-self.scale))) + self.location[1] * self.scale, (self.gridHeight + 5 + ((int(self.game.veggie_trays[16][1]) / 2)*-self.scale)) + self.location[0] * self.scale, 10, 10)

        pg.draw.rect(screen, self.color, space_rect)
        pg.draw.rect(screen, pg.Color('black'), space_rect, 1)

    def get_item(self):
        """
        Gets the item in the space.
        :return:
        """
        return self.item

    def set_item(self, item):
        """
        Sets the item in the space. Will also change the color of the space depending
        on what crop is being planted.
        :param item: The item to be placed in the space.
        :return:
        """
        self.item = item
        self.color = item.color
