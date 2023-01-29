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

    def draw(self, screen):
        """
        Draws the space to the screen.
        :param screen:
        :return:
        """
        # The rectangle of the space.
        space_rect = pg.Rect(495 + self.location[1] * 10, 10 + self.location[0] * 10, 10, 10)
        pg.draw.rect(screen, self.color, space_rect)

    def get_item(self):
        """
        Gets the item in the space.
        :return:
        """
        return self.item

