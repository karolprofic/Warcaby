from commons.constants import *
from commons.functions import *


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
            self.drawPiece(win, ASSETS_PIECE_WHITE, ASSETS_PIECE_WHITE_KING)
        else:
            self.drawPiece(win, ASSETS_PIECE_BLACK, ASSETS_PIECE_BLACK_KING)

    def drawPiece(self, win, pieceIcon, kingIcon):
        if self.isKing:
            drawImage(win, kingIcon, 100, 100, self.x - 50, self.y - 50, (90, 53, 9))
        else:
            drawImage(win, pieceIcon, 100, 100, self.x - 50, self.y - 50, (90, 53, 9))

    def move(self, row, col):
        self.row = row
        self.column = col
        self.calculateCoordinates()

    def __repr__(self):
        return str(self.color)
