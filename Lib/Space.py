import pygame as pg

class Space:
    """
    A space is a single cell in the grid.
    It can contain a plant or nothing.
    """
    def __init__(self, location):
        self.item = None
        self.color = pg.Color('green')
        self.location = location
        self.scale = 10

    def draw(self, screen):
        """
        Draws the space to the screen.
        :param screen:
        :return:
        """
        # The rectangle of the space.
        space_rect = pg.Rect(495 + self.location[1] * self.scale, 15 + self.location[0] * self.scale, 10, 10)
        pg.draw.rect(screen, self.color, space_rect)
        pg.draw.rect(screen, pg.Color('black'), space_rect, 1)

    def get_item(self):
        """
        Gets the item in the space.
        :return:
        """
        return self.item

