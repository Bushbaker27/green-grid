import pygame as pg
import json
import os


class Plant(pg.sprite.Sprite):
    def __init__(self, name, row=-1, col=-1):
        pg.sprite.Sprite.__init__(self)

        self.row = row
        self.col = col
        self.name = name.lower()
        self.relation = dict()
        self.color = self.decide_color()
        self.relations()

    def relations(self):
        """
        Initialize the relations of the plant with other plants.
        :return:
        """
        with open(os.path.join('./ResourcesLib', 'CropDB.JSON')) as file:
            data = json.load(file)
            for name, value in sorted(data[self.name].items(), key=lambda x: x[1], reverse=True):
                self.relation[name] = value

    def decide_color(self):
        if self.name == 'asparagus':
            return pg.Color('lightgreen')
        elif self.name == 'bean':
            return pg.Color((204, 86, 39))
        elif self.name == 'beet':
            return pg.Color('purple')
        elif self.name == 'broccoli':
            return pg.Color('darkgreen')
        elif self.name == 'cabbage':
            return pg.Color('white')
        elif self.name == 'radish':
            return pg.Color('red')
        elif self.name == 'squash':
            return pg.Color('yellow')
        elif self.name == 'strawberry':
            return pg.Color('pink')
        elif self.name == 'zucchini':
            return pg.Color('green')
        elif self.name == 'corn':
            return pg.Color('yellow')
        elif self.name == 'pumpkin':
            return pg.Color('orange')
        elif self.name == 'basil':
            # brackish green
            return pg.Color((19, 28, 9))
        elif self.name == 'carrot':
            # Burnt orange
            return pg.Color((128, 68, 0))
        elif self.name == 'onion':
            # tan
            return pg.Color((232, 193, 162))
        elif self.name == 'potato':
            return pg.Color('lightbrown')
        elif self.name == 'tomato':
            # tomato red
            return pg.Color((255, 99, 71))
