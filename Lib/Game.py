import pygame as pg
import os
import sys

class Game:
    def __init__(self):
        self.dimensions = (1500, 1000)
        self.screen = None
        self.grid = None
        self.background = None
        self.row_count = 0
        self.column_count = 0
        self.clock = None
        self.selected_cell = [None, '']
        self.start_game()

    def start_game(self):
        """
        Start the game
        :return:
        """
        pg.init()
        pg.display.set_caption('Green Grid')
        # A light gray color
        light_gray = (200, 200, 200)
        # A gray color
        gray = (100, 100, 100)

        color_active = pg.Color('darkslategray')
        color_passive = light_gray
        base_font = pg.font.Font(None, 32)
        black = 0, 0, 0
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode(self.dimensions)
        self.background = pg.image.load(os.path.join('./ResourcesLib/images', 'GrassBack.png'))
        sidebar = pg.Rect(0, 0, 250, 1000)

        # A list of all the input boxes, their rect is in the first element and the text is in
        # the second.
        veggie_trays = [
            [pg.Rect(45, 100, 160, 32), 'Asparagus'],
            [pg.Rect(45, 150, 160, 32), 'Basil'],
            [pg.Rect(45, 200, 160, 32), 'Bean'],
            [pg.Rect(45, 250, 160, 32), 'Beat'],
            [pg.Rect(45, 300, 160, 32), 'Broccoli'],
            [pg.Rect(45, 350, 160, 32), 'Cabbage'],
            [pg.Rect(45, 400, 160, 32), 'Carrot'],
            [pg.Rect(45, 450, 160, 32), 'Corn'],
            [pg.Rect(45, 500, 160, 32), 'Onion'],
            [pg.Rect(45, 550, 160, 32), 'Potato'],
            [pg.Rect(45, 600, 160, 32), 'Pumpkin'],
            [pg.Rect(45, 650, 160, 32), 'Radish'],
            [pg.Rect(45, 700, 160, 32), 'Squash'],
            [pg.Rect(45, 750, 160, 32), 'Strawberry'],
            [pg.Rect(45, 800, 160, 32), 'Tomato'],
            [pg.Rect(45, 850, 160, 32), 'Zucchini'],

        ]
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    for pair in veggie_trays:
                        box, text = pair
                        if box.collidepoint(event.pos):
                            # Toggle the active variable.
                            self.selected_cell = pair
                            self.selected_cell[1] = ''


                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        self.selected_cell = [None, '']
                    elif event.key == pg.K_BACKSPACE:
                        self.selected_cell[1] = self.selected_cell[1][:-1]
                    else:
                        self.selected_cell[1] += event.unicode

            self.screen.fill(black)
            self.screen.blit(self.background, (0, 0))
            # Drawing the sidebar
            pg.draw.rect(self.screen, gray, sidebar)

            # Render the current text.
            if self.selected_cell[0] is not None:
                pg.draw.rect(self.screen, color_active, self.selected_cell[0])
                # Blit the text.
                text_surface = base_font.render(self.selected_cell[1], True, (255, 255, 255))
                self.screen.blit(text_surface, (self.selected_cell[0].x + 5, self.selected_cell[0].y + 5))

            for box, text in veggie_trays:
                # Skip the selected box.
                if box is None or box is self.selected_cell[0]:
                    continue

                pg.draw.rect(self.screen, color_passive, box)
                text_surface = base_font.render(text, True, (255, 255, 255))
                self.screen.blit(text_surface, (box.x + 5, box.y + 5))
            pg.display.flip()
