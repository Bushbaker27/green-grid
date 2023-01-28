import pygame

class Game:
    def __init__(self):
        self.dimensions = (800, 600)
        self.screen = None
        self.start_game()

    def start_game(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.dimensions)

