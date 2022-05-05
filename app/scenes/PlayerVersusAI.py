from scenes.Game import Game
from checkers.Controller import *


class PlayerVersusAI(Game):
    def __init__(self, music):
        super().__init__(music)

    def start(self):
    # TODO: AI implementation
        run = True
        zegar = pygame.time.Clock()
        gra = Warcaby(self.WIN)
        pygame.init()

        while run:
            self.WIN.fill(WHITE_COLOR)
            zegar.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()

                    row, col = self.oblicz_rzad_i_kolumne(pos, gra)

                    if row != -1 and col != -1:
                        gra.wybierz_pionka(row, col)

            self.drawMenu(gra.board.numberOfRemainingBlack, gra.board.numberOfRemainingWhite, gra.board.numberOfBlackKing, gra.board.numberOfWhiteKing, gra.czyja_kolej)
            gra.update()

        pygame.quit()