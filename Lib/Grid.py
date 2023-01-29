from Lib import Plant
from Lib import Space
import pygame as pg


class Grid:

    def __init__(self, rows, cols, chosen_plants):
        self.rows = rows
        self.cols = cols
        self.chosen_plants = chosen_plants
        self.grid = []
        self.set_spaces()
        self.make_plants()

    def make_plants(self):
        """
        Make plants that are appropriate for this grid.
        :return:
        """
        # The first plant will be selected by which plant has the most rows being planted.
        plant = self.select_plant(0, True)
        curr_row = self.grid[0]
        self.plant_row(curr_row, plant)

        start_row = 1
        while start_row < self.rows:
            neighbors = self.get_neighbors((start_row, 0))



    def select_plant(self, row, simple=False):
        """
        Selects a plant to be placed in the grid.
        :param row: The row of the grid that the plant will be placed in.
        :param simple: If true, the plant will be a simple plant.
        :return: The plant to be placed in the grid.
        """
        best_plant = ''
        best_score = 0
        if simple:
            # Grab the plant with the highest value.
            for plant, num in self.chosen_plants.items():
                if num > best_score:
                    best_score = num
                    best_plant = plant
            if best_plant:
                return Plant.Plant(best_plant)

    def plant_row(self, row, plant):
        """
        Plants a row of plants.
        :param row: The row to plant
        :param plant: The plant that will be in this row.
        :return: None
        """
        for space in row:
            space.item = plant

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
        bounds = [(1, 0), (-1, 0)]
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
