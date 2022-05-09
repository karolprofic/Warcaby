from checkers.Board import *
from commons.constants import *


class Controller:
    def __init__(self, gameWindow):
        self.gameWindow = gameWindow
        self.selectedPiece = None
        self.board = Board()
        self.whoseTurn = PLAYER_BLACK
        self.possibleMoves = {}

    def update(self):
        self.board.drawPiecesOnBoard(self.gameWindow)
        self.drawPossibleMoves(self.possibleMoves)
        pygame.display.update()

    def reset(self):
        self.board.reset()

    def returnWinnerIfExists(self):
        return self.board.returnWinnerIfExists()

    def getBoard(self):
        return self.board

    def setBoard(self, newBoard):
        self.board = newBoard

    def selectPiece(self, row, column):
        if self.selectedPiece:
            if not self.movePiece(row, column):
                self.selectedPiece = None
                self.selectPiece(row, column)

        piece = self.board.boardArray[row][column]
        if piece != 0 and piece.color == self.whoseTurn:
            self.selectedPiece = piece
            self.possibleMoves = self.board.findPossibleMoves(piece)
            return True

        return False

    def movePiece(self, row, column):
        piece = self.board.boardArray[row][column]
        if self.selectedPiece and piece == 0 and (row, column) in self.possibleMoves:
            self.board.movePiece(self.selectedPiece, row, column)
            piecesJumpedOver = self.possibleMoves[(row, column)]
            if piecesJumpedOver:
                self.board.removePiece(piecesJumpedOver)
            self.changePlayer()
        else:
            return False

        return True

    def drawPossibleMoves(self, possibleMoves):
        for move in possibleMoves:
            row, column = move
            drawImage(self.gameWindow, ASSETS_PIECE_MOVE, 100, 100, column * 100, row * 100, (90, 53, 9))

    def changePlayer(self):
        self.possibleMoves = {}
        if self.whoseTurn == PLAYER_BLACK:
            self.whoseTurn = PLAYER_WHITE
        else:
            self.whoseTurn = PLAYER_BLACK
