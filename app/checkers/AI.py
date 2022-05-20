from copy import deepcopy
from scenes.Game import Game
from checkers.Controller import *
from commons.constants import *


class AI:
    def __init__(self, board, depth, playerColor):
        self.valueAndBoard = self.minimax(board, depth, playerColor)

    def minimax(self, board, depth, playerColor):
        if depth == 0 or board.returnWinnerIfExists() is not None:
            return self.rateMove(board), board

        if playerColor == PLAYER_WHITE:
            return self.findWhiteMoves(board, depth)

        if playerColor == PLAYER_BLACK:
            return self.findBlackMoves(board, depth)

    @staticmethod
    def rateMove(board):
        return board.numberOfRemainingWhite - board.numberOfRemainingBlack + (board.numberOfWhiteKing * 0.5 - board.numberOfBlackKing * 0.5)

    def findWhiteMoves(self, board, depth):
        maxEval = float('-inf')
        bestMove = None
        for move in self.getAllMoves(board, PLAYER_WHITE):
            evaluation = AI(move, depth - 1, PLAYER_BLACK).valueAndBoard[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                bestMove = move

        return maxEval, bestMove

    def findBlackMoves(self, board, depth):
        minEval = float('inf')
        bestMove = None
        for move in self.getAllMoves(board, PLAYER_BLACK):
            evaluation = AI(move, depth - 1, PLAYER_WHITE).valueAndBoard[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                bestMove = move

        return minEval, bestMove

    def getAllMoves(self, board, color):
        moves = []
        for piece in self.findAllPiecesOfColor(board, color):
            possibleMoves = board.findPossibleMoves(piece)
            for move, skip in possibleMoves.items():
                newBoard = deepcopy(board)
                chosenPiece = newBoard.getPiece(piece.row, piece.column)
                newBoard.movePiece(chosenPiece, move[0], move[1])
                if skip:
                    newBoard.removePiece(skip)
                moves.append(newBoard)
        return moves

    @staticmethod
    def findAllPiecesOfColor(board, color):
        pieces = []
        for row in board.boardArray:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces
