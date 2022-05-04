import pygame

WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)


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
        if self.color == WHITE_COLOR:
            if self.isKing:
                img = pygame.image.load("./assets/Pionki/whiteQueen.png")
            else:
                img = pygame.image.load("./assets/Pionki/white.png")
        else:
            if self.isKing:
                img = pygame.image.load("./assets/Pionki/blackQueen.png")
            else:
                img = pygame.image.load("./assets/Pionki/black.png")
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
