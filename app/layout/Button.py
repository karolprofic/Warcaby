import pygame
from pygame.locals import *
from scenes.Game import *

clicked = False

class Button:

    def __init__(self, x, y, text, screen, font):
        self.x = x
        self.y = y
        self.text = text
        self.screen = screen
        self.font = font

    def drawButton(self):
        global clicked
        action = False

        mousePosition = pygame.mouse.get_pos()
        buttonRect = Rect(self.x, self.y, 390, 70)
        buttonFont = self.font.render(self.text, True, (252, 245, 235))

        if buttonRect.collidepoint(mousePosition):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                buttonFont = self.font.render(self.text, True, (30, 30, 30))

        self.screen.blit(buttonFont, (self.x + int(390 / 2) - int(buttonFont.get_width() / 2), self.y + 25))
        return action
