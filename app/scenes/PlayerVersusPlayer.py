from scenes.Game import Game
from checkers.Controller import *


class PlayerVersusPlayer(Game):
    def __init__(self, music):
        super().__init__(music)
        self.gameController = Controller(self.gameWindow)
        self.clock = pygame.time.Clock()
        self.start()

    def start(self):

        try:
            pygame.init()

            while self.isRunning:
                self.gameWindow.fill(DEFAULT_BACKGROUND)
                self.clock.tick(60)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.isRunning = False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        row, col = self.mouseClickEvent(pygame.mouse.get_pos(), self.gameController)
                        if row != -1 and col != -1:
                            self.gameController.selectPiece(row, col)

                self.drawMenu(self.gameController.board.numberOfRemainingBlack,
                              self.gameController.board.numberOfRemainingWhite,
                              self.gameController.board.numberOfBlackKing,
                              self.gameController.board.numberOfWhiteKing,
                              self.gameController.whoseTurn)
                self.gameController.update()

            pygame.quit()

        except:
            print("3")
            return

