import pygame as pg
import os
import sys
import re
import json

from Lib.SendSMS import SendSMS
from Lib import Grid


class Game:
    def __init__(self):
        self.dimensions = (1500, 1000)
        self.grid = None
        self.screen = None
        self.grid = None
        self.background = None
        self.row_count = 0
        self.column_count = 0
        self.clock = None
        self.splash_dimensions = (700, 500)
        self.selected_cell = [None, '']
        self.veggie_trays = [
            [pg.Rect(45, 100, 160, 32), 'Asparagus', 'Asparagus'],
            [pg.Rect(45, 150, 160, 32), 'Basil', 'Basil'],
            [pg.Rect(45, 200, 160, 32), 'Bean', 'Bean'],
            [pg.Rect(45, 250, 160, 32), 'Beet', 'Beet'],
            [pg.Rect(45, 300, 160, 32), 'Broccoli', 'Broccoli'],
            [pg.Rect(45, 350, 160, 32), 'Cabbage', 'Cabbage'],
            [pg.Rect(45, 400, 160, 32), 'Carrot', 'Carrot'],
            [pg.Rect(45, 450, 160, 32), 'Corn', 'Corn'],
            [pg.Rect(45, 500, 160, 32), 'Onion', 'Onion'],
            [pg.Rect(45, 550, 160, 32), 'Potato', 'Potato'],
            [pg.Rect(45, 600, 160, 32), 'Pumpkin', 'Pumpkin'],
            [pg.Rect(45, 650, 160, 32), 'Radish', 'Radish'],
            [pg.Rect(45, 700, 160, 32), 'Squash', 'Squash'],
            [pg.Rect(45, 750, 160, 32), 'Strawberry', 'Strawberry'],
            [pg.Rect(45, 800, 160, 32), 'Tomato', 'Tomato'],
            [pg.Rect(45, 850, 160, 32), 'Zucchini', 'Zucchini'],
            [pg.Rect(15, 40, 100, 32), 'Length', 'Length'],
            [pg.Rect(145, 40, 100, 32), 'Width', 'Width'],
        ]
        self.sendSMS = SendSMS()

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
        base_font = pg.font.Font(None, 30)
        black = 0, 0, 0

        self.screen = pg.display.set_mode(self.splash_dimensions)
        self.background = pg.image.load(os.path.join('./ResourcesLib/images', 'GGLogo.png'))
        self.screen.blit(self.background, (0, 0))
        pg.display.flip()
        pg.time.wait(2000)

        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode(self.dimensions)
        self.background = pg.image.load(os.path.join('./ResourcesLib/images', 'GrassBack.png'))

        # The sidebar
        sidebar = pg.Rect(0, 0, 250, 1000)
        # The start button.
        start_button = pg.Rect(30, 900, 200, 50)
        start_button_color = pg.Color('palegreen')
        start_text = 'Start'

        while True:
            self.CheckForTextMessages()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    for pair in self.veggie_trays:
                        box, text, _ = pair
                        if box.collidepoint(event.pos):
                            # Toggle the active variable.
                            self.selected_cell = pair
                            self.selected_cell[1] = ''
                    if start_button.collidepoint(event.pos):
                        # Bring up the grid.
                        self.row_count = int(self.veggie_trays[16][1])
                        self.column_count = int(self.veggie_trays[17][1])
                        plant_filter = [(pair[2], pair[1]) for pair in self.veggie_trays[:16] if
                                        re.match(r'^[1-9]{0,1}[0-9]+$', pair[1])]
                        plant_selected = dict()
                        for plant, num in plant_filter:
                            plant_selected[plant] = int(num)

                        self.grid = Grid.Grid(self.row_count, self.column_count, plant_selected)


                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_BACKSPACE:
                        self.selected_cell[1] = self.selected_cell[1][:-1]
                    else:
                        # Only accept numbers that are smaller than 1000000000.
                        text = event.unicode
                        if (10 >= len(self.selected_cell[1]) >= 1 and re.match(r'^[0-9]$', text)) or \
                                re.match(r'^[1-9]$', text):
                            self.selected_cell[1] += event.unicode

            self.screen.fill(black)
            self.screen.blit(self.background, (0, 0))
            # Drawing the sidebar
            pg.draw.rect(self.screen, gray, sidebar)

            # Render the current text.
            if self.selected_cell[0] is not None and self.selected_cell[0] is not start_button:
                pg.draw.rect(self.screen, color_active, self.selected_cell[0])
                # Blit the text.
                text_surface = base_font.render(self.selected_cell[1], True, (255, 255, 255))
                self.screen.blit(text_surface, (self.selected_cell[0].x + 5, self.selected_cell[0].y + 5))

            for box, text, _ in self.veggie_trays:
                # Skip the selected box.
                if box is None or box is self.selected_cell[0]:
                    continue

                pg.draw.rect(self.screen, color_passive, box)
                text_surface = base_font.render(text, True, (0, 0, 0))
                self.screen.blit(text_surface, (box.x + 5, box.y + 5))

            # Green start button
            pg.draw.rect(self.screen, start_button_color, start_button)
            start_text_surface = base_font.render(start_text, True, (0, 0, 0))
            self.screen.blit(start_text_surface, (start_button.x + 75, start_button.y + 15))

            if self.grid is not None:
                self.grid.draw(self.screen)

            pg.display.flip()

    def CheckForTextMessages(self):
        textRequestFile = open(os.path.dirname(__file__) + "/../ResourcesLib/TextRequest.JSON")
        textRequestData = json.load(textRequestFile)

        if textRequestData["entry"] == "pause":
            print("User request a pause")
            self.sendSMS.SendTractorPause("Harvesting", "1,1")
        elif textRequestData["entry"] == "begin":
            print("User request a begin")
            self.sendSMS.SendTractorBegin("Harvesting", "1,1")

        resetTextRequestData = {
            "entry": "no response"
        }

        replaceTextRequestFile = json.dumps(resetTextRequestData, indent=4)

        with open(os.path.dirname(__file__) + "/../ResourcesLib/TextRequest.JSON", "w") as outfile:
            outfile.write(replaceTextRequestFile)
