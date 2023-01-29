import pygame as pg

class Space:
    """
    A space is a single cell in the grid.
    It can contain a plant or nothing.
    """
    def __init__(self, location, scale_row=10, scale_col=10):
        self.item = None
        self.color = pg.Color('gray')
        self.location = location
        self.scale_row = scale_row
        self.scale_col = scale_col

    def draw(self, screen):
        """
        Draws the space to the screen.
        :param screen:
        :return:
        """
        # The rectangle of the space.
        space_rect = pg.Rect(495 + self.location[1] * self.scale_row, 15 + self.location[0] *
                             self.scale_col, self.scale_row, self.scale_col)
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

    def show_tractor(self, screen):
        space_rect = pg.Rect(495 + self.location[1] * self.scale_row, 15 + self.location[0] *
                             self.scale_col, self.scale_row, self.scale_col)
        pg.draw.rect(screen, pg.Color('black'), space_rect)
