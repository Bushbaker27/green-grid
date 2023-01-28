from Lib import Plant


class Grids:

    def __init__(self, rows, cols, chosen_plants):
        self.rows = rows
        self.cols = cols
        self.chosen_plants = chosen_plants
        self.plant_list = []

    def make_plants(self):
        #Creates plant object from strings given
        for plant in self.chosen_plants:
            new_plant = Plant.Plant(plant)
            self.plant_list.append(new_plant)
        # Creates relationships for the plants given
        for plant in self.plant_list:
            plant.relations()
