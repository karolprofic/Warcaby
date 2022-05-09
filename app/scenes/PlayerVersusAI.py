from scenes.Game import Game
from checkers.Controller import *
from commons.constants import *
from checkers.AI import *

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
                moveValue, newBoard = AI(self.gameController.getBoard(), self.difficulty, PLAYER_WHITE).valueAndBoard
                self.gameController.setBoard(newBoard)
                self.gameController.changePlayer()

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

