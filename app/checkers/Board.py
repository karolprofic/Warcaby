from checkers.Piece import *
from commons.constants import *
from commons.functions import *


class Board:
    def __init__(self):
        self.boardArray = []
        self.numberOfRemainingBlack = 12
        self.numberOfRemainingWhite = 12
        self.numberOfBlackKing = 0
        self.numberOfWhiteKing = 0
        self.createArrayBoard()

    def createArrayBoard(self):
        for row in range(8):
            self.boardArray.append([])
            for column in range(8):
                if column % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.boardArray[row].append(Piece(row, column, PLAYER_WHITE))
                    elif row > 4:
                        self.boardArray[row].append(Piece(row, column, PLAYER_BLACK))
                    else:
                        self.boardArray[row].append(0)
                else:
                    self.boardArray[row].append(0)

    @staticmethod
    def drawBoard(gameWindow):
        for row in range(8):
            for column in range(8):
                drawImage(gameWindow, ASSETS_BOARD_WHITE, 100, 100, row * 100, column * 100, (90, 53, 9))

        for row in range(8):
            for column in range(row % 2, 8, 2):
                drawImage(gameWindow, ASSETS_BOARD_BLACK, 100, 100, row * 100, column * 100, (90, 53, 9))

    def drawPiecesOnBoard(self, gameWindow):
        self.drawBoard(gameWindow)
        for row in range(8):
            for column in range(8):
                piece = self.boardArray[row][column]
                if piece != 0:
                    piece.draw(gameWindow)

    def movePiece(self, piece, row, column):
        self.boardArray[piece.row][piece.column], self.boardArray[row][column] = self.boardArray[row][column], self.boardArray[piece.row][piece.column]

        piece.move(row, column)

        if row == 7 or row == 0:
            piece.makeKing()
            if piece.color == PLAYER_WHITE:
                self.numberOfWhiteKing += 1
            else:
                self.numberOfBlackKing += 1

    def reset(self):
        self.boardArray = []
        self.numberOfRemainingBlack = 12
        self.numberOfRemainingWhite = 12
        self.numberOfBlackKing = 0
        self.numberOfWhiteKing = 0
        self.createArrayBoard()

    def removePiece(self, pieces):
        for piece in pieces:
            self.boardArray[piece.row][piece.column] = 0

            if piece == 0:
                continue

            if piece.isKing:
                if piece.color == PLAYER_BLACK:
                    self.numberOfBlackKing -= 1
                    self.numberOfRemainingBlack -= 1
                if piece.color == PLAYER_WHITE:
                    self.numberOfWhiteKing -= 1
                    self.numberOfRemainingWhite -= 1
            else:
                if piece.color == PLAYER_BLACK:
                    self.numberOfRemainingBlack -= 1
                if piece.color == PLAYER_WHITE:
                    self.numberOfRemainingWhite -= 1

    def returnWinnerIfExists(self):
        if self.numberOfRemainingBlack <= 0:
            return PLAYER_WHITE
        elif self.numberOfRemainingWhite <= 0:
            return PLAYER_BLACK
        return None

    def findPossibleMoves(self, piece):
        possibleMoves = {}
        left = piece.column - 1
        right = piece.column + 1
        rowNumber = piece.row

        if piece.color == PLAYER_BLACK or piece.isKing:
            possibleMoves.update(self.findPossibleMovesOnDiagonal(rowNumber - 1, max(rowNumber - 3, -1), -1, piece.color, left, True))
            possibleMoves.update(self.findPossibleMovesOnDiagonal(rowNumber - 1, max(rowNumber - 3, -1), -1, piece.color, right, False))
        if piece.color == PLAYER_WHITE or piece.isKing:
            possibleMoves.update(self.findPossibleMovesOnDiagonal(rowNumber + 1, max(rowNumber + 3, 8), 1, piece.color, left, True))
            possibleMoves.update(self.findPossibleMovesOnDiagonal(rowNumber + 1, max(rowNumber + 3, 8), 1, piece.color, right, False))

        return possibleMoves

    def findPossibleMovesOnDiagonal(self, start, stop, step, color, direction, traverseLeft, skipped=None):
        if skipped is None:
            skipped = []

        moves = {}
        last = []
        for r in range(start, stop, step):
            if traverseLeft:
                if direction < 0:
                    break
            if not traverseLeft:
                if direction >= 8:
                    break

            if r > 7 or direction > 7:
                continue

            current = self.boardArray[r][direction]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, direction)] = last + skipped
                else:
                    moves[(r, direction)] = last

                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, 8)
                    moves.update(self.findPossibleMovesOnDiagonal(r + step, row, step, color, direction - 1, True, skipped=last))
                    moves.update(self.findPossibleMovesOnDiagonal(r + step, row, step, color, direction + 1, False, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            if traverseLeft:
                direction -= 1
            if not traverseLeft:
                direction += 1

        return moves

    def getPiece(self, row, col):
        return self.boardArray[row][col]