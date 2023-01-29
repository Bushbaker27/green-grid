import pygame as pg
from Lib import Plant

class Legend:
    def __init__(self, legend):
        self.legend = legend
        self.position = (280, 10)

    def draw(self, screen):
        """
        Draw the legend on the screen.
        :param screen: The screen context to draw on.
        :return:
        """
        pg.draw.rect(screen, (0, 0, 0), (self.position[0], self.position[1], 200, 400))
        pg.draw.rect(screen, (255, 255, 255), (self.position[0] + 2, self.position[1] + 2, 196,
                                               396), 1)
        font = pg.font.SysFont('Arial', 20)
        for i, (plant, num) in enumerate(self.legend.items()):
            plant = Plant.Plant(plant)
            # Draw a border around the plant color.
            pg.draw.rect(screen, (255, 255, 255), (self.position[0] + 10, self.position[1] + 10 +
                                                   i * 22, 22, 22), 1)
            pg.draw.rect(screen, plant.color, (self.position[0] + 11, self.position[1] + 11 + i *
                                               22, 20, 20))
            # Draw the text.
            text = font.render(plant.name.capitalize(), True, (255, 255, 255))
            screen.blit(text, (self.position[0] + 40, self.position[1] + 11 + i * 22))