import pygame
import json
import os


class Plant(pygame.sprite.Sprite):
    def __init__(self, name, row=1, col=-1):
        pygame.sprite.Sprite.__init__(self)
        #self.image = image
        #self.rect = self.image.get_rect()
        #self.rect.x = x
        #self.rect.y = y

        self.row = row
        self.col = col
        self.name = name
        self.relation = []

    def relations(self):

        #opens JSON file
        f = open(os.path.join('./ResourcesLib', 'CropDB.JSON'))

        #returns JSON object as dict
        data = json.load(f)

        #for i in data[self.name]:


        f.close()
