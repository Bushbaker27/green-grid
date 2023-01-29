import pygame as pg

class Space:
    """
    A space is a single cell in the grid.
    It can contain a plant or nothing.
    """
    def __init__(self, location):
        self.item = None
        self.color = pg.Color('brown')
        self.location = location

