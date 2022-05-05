import pygame
from checkers.Piece import *
from commons.constants import *

class Board:
    def __init__(self):
        self.boardArray = []
        self.numberOfRemainingBlack = 12
        self.numberOfRemainingWhite = 12
        self.numberOfBlackKing = 0
        self.numberOfWhiteKing = 0
        self.createBoardWithPieces()

    def drawnBoard(self, win):
        for row in range(8):
            # TODO: Duplikacja kodu
            for column in range(8):
                img = pygame.image.load(ASSETS_BOARD_WHITE)
                img.convert()
                el = img.get_rect()
                el.height = 100
                el.width = 100
                el.left = row * 100
                el.top = column * 100
                win.blit(img, el)
                pygame.draw.rect(win, (90, 53, 9), el, 1)

        for row in range(8):
            for column in range(row % 2, 8, 2):
                img = pygame.image.load(ASSETS_BOARD_BLACK)
                img.convert()
                el = img.get_rect()
                el.height = 100
                el.width = 100
                el.left = row * 100
                el.top = column * 100
                win.blit(img, el)
                pygame.draw.rect(win, (90, 53, 9), el, 1)

    def movePiece(self, piece, row, column):
        self.boardArray[piece.row][piece.column], self.boardArray[row][column] = self.boardArray[row][column], self.boardArray[piece.row][piece.column]
        piece.move(row, column)

        if row == 8 - 1 or row == 0:
            piece.makeKing()
            if piece.color == PLAYER_WHITE:
                self.numberOfWhiteKing += 1
            else:
                self.numberOfBlackKing += 1

    def createBoardWithPieces(self):
        for row in range(8):
            self.boardArray.append([])
            for column in range(8):
                if column % 2 == ((row +  1) % 2):
                    if row < 3:
                        self.boardArray[row].append(Piece(row, column, PLAYER_WHITE))
                    elif row > 4:
                        self.boardArray[row].append(Piece(row, column, PLAYER_BLACK))
                    else:
                        self.boardArray[row].append(0)
                else:
                    self.boardArray[row].append(0)

    def reset(self):
        self.boardArray = []
        self.numberOfRemainingBlack = 12
        self.numberOfRemainingWhite = 12
        self.numberOfBlackKing = 0
        self.numberOfWhiteKing = 0
        self.createBoardWithPieces()

    def drawPiecesOnBoard(self, win):
        self.drawnBoard(win)
        for row in range(8):
            for column in range(8):
                piece = self.boardArray[row][column]
                if piece != 0:
                    piece.draw(win)

    def usun_pionka(self, pionki):
        for pionek in pionki:
            self.boardArray[pionek.row][pionek.column] = 0
            if pionek != 0:
                if pionek.color == PLAYER_BLACK:
                    self.numberOfRemainingBlack -= 1
                else:
                    self.numberOfRemainingWhite -= 1

    def kto_wygral(self):
        if self.numberOfRemainingBlack <= 0:
            return PLAYER_WHITE
        elif self.numberOfRemainingWhite <= 0:
            return PLAYER_BLACK
        return None

    def findPossibleMoves(self, pionek):
        possibleMoves = {}
        left = pionek.column - 1
        right = pionek.column + 1
        rowNumber = pionek.row

        if pionek.color == PLAYER_BLACK or pionek.isKing:
            possibleMoves.update(self.lewa_diagonala(rowNumber - 1, max(rowNumber - 3, -1), -1, pionek.color, left))
            possibleMoves.update(self.prawa_diagonala(rowNumber - 1, max(rowNumber - 3, -1), -1, pionek.color, right))
        if pionek.color == PLAYER_WHITE or pionek.isKing:
            possibleMoves.update(self.lewa_diagonala(rowNumber + 1, max(rowNumber + 3, 8), 1, pionek.color, left))
            possibleMoves.update(self.prawa_diagonala(rowNumber + 1, max(rowNumber + 3, 8), 1, pionek.color, right))

        return possibleMoves

    def lewa_diagonala(self, start, stop, step, kolor, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            if(r > 7 or left > 7):
                continue

            current = self.boardArray[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r,left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        rzad = max(r-3, 0)
                    else:
                        rzad = min(r+3, 8)
                    moves.update(self.lewa_diagonala(r + step, rzad, step, kolor, left - 1, skipped=last))
                    moves.update(self.prawa_diagonala(r + step, rzad, step, kolor, left + 1, skipped=last))
                break
            elif current.color == kolor:
                break
            else:
                last = [current]

            left -= 1
        return moves

    def prawa_diagonala(self, start, stop, step, kolor, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= 8:
                break

            if(r > 7 or right > 7):
                continue

            current = self.boardArray[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        rzad = max(r - 3, 0)
                    else:
                        rzad = min(r + 3, 8)
                    moves.update(self.lewa_diagonala(r + step, rzad, step, kolor, right - 1, skipped=last))
                    moves.update(self.prawa_diagonala(r + step, rzad, step, kolor, right + 1, skipped=last))
                break
            elif current.color == kolor:
                break
            else:
                last = [current]

            right += 1
        return moves

