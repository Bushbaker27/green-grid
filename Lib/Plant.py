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
