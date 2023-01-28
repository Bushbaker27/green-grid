import pygame
import json
class Plant(pygame.sprite.Sprite):
    def __init__(self, x, y, image, row, col, name):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.row = row
        self.col = col
        self.name = name

    def relations(self):
        #opens JSON file
        f = open('CropDB.json')

        #returns JSON object as dict
        data = json.load(f)

        for i in data['crops']:
            print(i)

        f.close()
