from copy import deepcopy

from scenes.Game import Game
from checkers.Controller import *
from commons.constants import *

class PlayerVersusAI(Game):
    def __init__(self, music):
        super().__init__(music)
        self.gameController = Controller(self.gameWindow)
        self.clock = pygame.time.Clock()
        self.difficulty = 1
        self.start()

    def start(self):
        pygame.init()

        while self.isRunning:
            self.gameWindow.fill(DEFAULT_BACKGROUND)
            self.clock.tick(60)

            # AI move
            if self.gameController.whoseTurn == PLAYER_WHITE:
                value, new_board = minimax(self.gameController.get_board(), self.difficulty, PLAYER_WHITE)
                print("ZMIANA : " + str(value) )
                self.gameController.ai_move(new_board)




            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isRunning = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.changeDifficultyClicked(pygame.mouse.get_pos())
                    row, col = self.mouseClickEvent(pygame.mouse.get_pos(), self.gameController)
                    if row != -1 and col != -1:
                        self.gameController.selectPiece(row, col)

            self.drawMenu(self.gameController.board.numberOfRemainingBlack,
                          self.gameController.board.numberOfRemainingWhite,
                          self.gameController.board.numberOfBlackKing,
                          self.gameController.board.numberOfWhiteKing,
                          self.gameController.whoseTurn)
            self.drawChangDifficulty()
            self.gameController.update()

        pygame.quit()

    def changeDifficultyClicked(self, mousePosition):
        x, y = mousePosition
        if x > 800 or y > 800:
            if 840 < x < 1015 and 500 < y < 570:
                self.difficulty = 1
            if 1016 < x < 1190 and 500 < y < 560:
                self.difficulty = 4

    def drawChangDifficulty(self):
        font = pygame.font.SysFont(FONT_NAME, 28)

        if self.difficulty == 1:
            self.gameWindow.blit(font.render(TEXT_EASY, True, (50, 50, 50)), (840, 450))
            drawImage(self.gameWindow, ASSETS_DIFFICULTY_EASY, 66, 350, 840, 500)
        else:
            self.gameWindow.blit(font.render(TEXT_HARD, True, (50, 50, 50)), (820, 450))
            drawImage(self.gameWindow, ASSETS_DIFFICULTY_HARD, 66, 350, 840, 500)





# TODO: refaktor
def minimax(board, depth, playerColor):
    if depth == 0 or board.returnWinnerIfExists() is not None:
        moveValue = board.numberOfRemainingWhite - board.numberOfRemainingBlack + (board.numberOfWhiteKing * 0.5 - board.numberOfBlackKing * 0.5)
        return moveValue, board

    if playerColor == PLAYER_WHITE:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(board, PLAYER_WHITE):
            evaluation = minimax(move, depth - 1, PLAYER_BLACK)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move

        return maxEval, best_move

    if playerColor == PLAYER_BLACK:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(board, PLAYER_BLACK):
            evaluation = minimax(move, depth - 1, PLAYER_WHITE)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move

        return minEval, best_move


def simulate_move(piece, move, board, skip):
    board.movePiece(piece, move[0], move[1])
    if skip:
        board.removePiece(skip)

    return board


def get_all_moves(board, color):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.findPossibleMoves(piece)
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.column)
            new_board = simulate_move(temp_piece, move, temp_board, skip)
            moves.append(new_board)

    return moves

