from Lib import Plant
from Lib import Space
import pygame as pg

class Grid:

    def __init__(self, rows, cols, chosen_plants):
        self.rows = rows
        self.cols = cols
        self.chosen_plants = chosen_plants
        self.plant_list = []
        self.grid = []
        self.set_spaces()

    def make_plants(self):
        #Creates plant object from strings given
        for plant in self.chosen_plants:
            new_plant = Plant.Plant(plant)
            self.plant_list.append(new_plant)
        # Creates relationships for the plants given
        for plant in self.plant_list:
            plant.relations()

    def set_spaces(self):
        """
        Sets the spaces in the grid.
        :return:
        """
        for row in range(self.rows):
            self.grid.append([])
            for col in range(self.cols):
                self.grid[row].append(Space.Space((row, col)))

    def get_space(self, location):
        """
        Gets the space at the given location.
        :param location:
        :return:
        """
        if not self.check_bound(location):
            return None
        return self.grid[location[0]][location[1]]

    def get_neighbors(self, location):
        """
        Gets the neighbors of the given location.
        :param location: The location to test.
        :return: a list of neighbors that are adjacent to the given location.
        """
        neighbors = []
        bounds = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for bound in bounds:
            neighbor = (location[0] + bound[0], location[1] + bound[1])
            if not self.check_bound(neighbor):
                continue
            neighbors.append(self.get_space(neighbor))

        return neighbors

    def check_bound(self, location):
        """
        Checks if the given location is within the bounds of the grid.
        :param location:
        :return: True if the sl
        """
        return location[0] < 0 or location[0] >= self.rows or location[1] < 0 or location[1] >= self.cols


    def draw(self, screen):
        """
        Draws the grid to the screen.
        :param screen: The main screen that is currently active on the application.
        :return: None
        """
        # Make a rectangle as the grid.
        grid_rect = pg.Rect(490, 10, self.cols * 10 + 10, self.rows * 10 + 10)
        pg.draw.rect(screen, pg.Color('brown'), grid_rect)
        for row in self.grid:
            for space in row:
                space.draw(screen)