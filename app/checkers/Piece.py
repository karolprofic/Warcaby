import pygame
from commons.constants import *

class Piece:

    def __init__(self, row, column, color):
        self.x = 0
        self.y = 0
        self.row = row
        self.column = column
        self.color = color
        self.isKing = False
        self.calculateCoordinates()

    def calculateCoordinates(self):
        self.x = 100 * self.column + 100 // 2
        self.y = 100 * self.row + 100 // 2

    def makeKing(self):
        self.isKing = True

    def draw(self, win):
        if self.color == PLAYER_WHITE:
            if self.isKing:
                img = pygame.image.load(ASSETS_PIECE_WHITE_KING)
            else:
                img = pygame.image.load(ASSETS_PIECE_WHITE)
        else:
            if self.isKing:
                img = pygame.image.load(ASSETS_PIECE_BLACK_KING)
            else:
                img = pygame.image.load(ASSETS_PIECE_BLACK)
        img.convert()
        el = img.get_rect()
        el.height = 100
        el.width = 100
        el.left = self.x - 50
        el.top = self.y - 50
        win.blit(img, el)
        pygame.draw.rect(win, (90, 53, 9), el, 1)

    def move(self, rzad, col):
        self.row = rzad
        self.column = col
        self.calculateCoordinates()

    def __repr__(self):
        return str(self.color)
