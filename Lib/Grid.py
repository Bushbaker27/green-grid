from Lib import Plant
from Lib import Space
from Lib import Legend
import pygame as pg


class Grid:

    def __init__(self, rows, cols, chosen_plants):
        self.rows = rows
        self.cols = cols
        self.chosen_plants = chosen_plants
        self.legend = Legend.Legend(chosen_plants)
        self.grid = []
        self.set_spaces()
        self.make_plants()

    def make_plants(self):
        """
        Make plants that are appropriate for this grid.
        :return:
        """
        # The first plant will be selected by which plant has the most rows being planted.
        plant = self.select_plant(True)
        self.plant_row(0, plant)

        rows_to_plant = sum(self.chosen_plants.values())
        while rows_to_plant > 0:
            # Select a plant to be planted.
            plant, row = self.select_plant()
            # Plant the plant in the row.
            self.plant_row(row, plant)
            # Decrement the number of rows to plant.
            rows_to_plant -= 1

    def calculate_score(self, plant, neighbors):
        """
        Calculates the score of the given plant in the given location.
        :param plant: The plant to be tested.
        :param neighbors: The neighbors of the plant.
        :return: The score of the plant.
        """
        score = 0
        for neighbor in neighbors:
            if neighbor is not None:
                score += plant.get_score(neighbor.item)
        return score

    def select_plant(self, simple=False):
        """
        Selects a plant to be placed in the grid.
        :param simple: If true, the plant will be a simple plant.
        :return: The plant to be placed in the grid.
        """
        best_plant = ''
        best_score = 0
        # Grab the plant with the highest value.
        for plant, num in self.chosen_plants.items():
            if num > best_score:
                best_score = num
                best_plant = plant
        plant = Plant.Plant(best_plant)
        if simple:
            return plant

        # If this was not a simple planting, then we must do some investigation.
        best_row = 0
        best_score = -2
        for row in range(1, self.rows):
            # If the row is already used, then skip it.
            if self.grid[row][0].item:
                continue
            score = self.calculate_score(plant, self.get_neighbors((row, 0)))
            if score > best_score:
                best_score = score
                best_row = row
        return plant, best_row

    def plant_row(self, row, plant):
        """
        Plants a row of plants.
        :param row: The row to plant
        :param plant: The plant that will be in this row.
        :return: None
        """
        for space in self.grid[row]:
            space.set_item(plant)
        self.chosen_plants[plant.name.capitalize()] -= 1

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
        if self.check_bound(location):
            return None
        return self.grid[location[0]][location[1]]

    def get_neighbors(self, location):
        """
        Gets the neighbors of the given location.
        :param location: The location to test.
        :return: a list of neighbors that are adjacent to the given location.
        """
        neighbors = []
        bounds = [1, -1]
        for bound in bounds:
            neighbor = (location[0] + bound, location[1])
            if self.check_bound(neighbor):
                continue
            neighbors.append(self.get_space(neighbor))

        return neighbors

    def check_bound(self, location):
        """
        Checks if the given location is within the bounds of the grid.
        :param location:
        :return: True if the location is outside the bounds of the grid.
        """
        return location[0] < 0 or location[0] >= self.rows or location[1] < 0 or location[1] >= \
               self.cols

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
