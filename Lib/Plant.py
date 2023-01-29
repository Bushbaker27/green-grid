import pygame as pg
import json
import os


class Plant(pg.sprite.Sprite):
    def __init__(self, name):
        pg.sprite.Sprite.__init__(self)
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
        """
        Decide the color of the plant.
        :return: The color of the plant.
        """
        if self.name == 'asparagus':
            # Blue
            return pg.Color((27, 45, 204))
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
            return pg.Color((47, 0, 122))
        elif self.name == 'strawberry':
            return pg.Color('pink')
        elif self.name == 'zucchini':
            return pg.Color((117, 74, 0))
        elif self.name == 'corn':
            return pg.Color('yellow')
        elif self.name == 'pumpkin':
            return pg.Color('orange')
        elif self.name == 'basil':
            # magenta
            return pg.Color((204, 27, 204))
        elif self.name == 'carrot':
            # Burnt orange
            return pg.Color((79, 9, 30))
        elif self.name == 'onion':
            # tan
            return pg.Color((232, 193, 162))
        elif self.name == 'potato':
            # light brown
            return pg.Color((181, 101, 29))
        elif self.name == 'tomato':
            # lime
            return pg.Color((27, 204, 89))

    def get_score(self, other):
        """
        Get the score of the plant with the given plant.
        :param other: The other plant.
        :return: The score of the plant.
        """
        if other is None:
            return 1
        if other.name == self.name:
            return 0
        return self.relation[other.name]
