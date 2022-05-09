from pygame import mixer
from layout.Button import *
from commons.constants import *
from commons.functions import *

class Game:

    def __init__(self, music):
        self.config_music = music
        self.isRunning = True
        self.gameWindow = pygame.display.set_mode((1220, 800))

        if self.config_music:
            mixer.init()
            mixer.music.load(ASSETS_MUSIC_1)
            mixer.music.play()

        pygame.display.set_caption(GAME_TITLE)

    def drawMenu(self, blackRemaining, whiteRemaining, blackKings, whiteKings, whoseTurn):
        biggerFont = pygame.font.SysFont(FONT_NAME, 36)
        smallerFont = pygame.font.SysFont(FONT_NAME, 22)

        self.gameWindow.blit(biggerFont.render(TEXT_TITLE, True, (50, 50, 50)), (820, 20))
        self.gameWindow.blit(smallerFont.render(str(TEXT_WHITE_REMAINING + str(whiteRemaining)), True, (50, 50, 50)), (820, 70))
        self.gameWindow.blit(smallerFont.render(str(TEXT_BLACK_REMAINING + str(blackRemaining)), True, (50, 50, 50)), (820, 110))
        self.gameWindow.blit(smallerFont.render(str(TEXT_BLACK_KINGS + str(blackKings)), True, (50, 50, 50)), (820, 150))
        self.gameWindow.blit(smallerFont.render(str(TEXT_WHITE_KINGS + str(whiteKings)), True, (50, 50, 50)), (820, 190))

        if blackRemaining == 0 or whiteRemaining == 0:
            self.gameWindow.blit(smallerFont.render(TEXT_WIN, True, (50, 50, 50)), (820, 255))
            if whiteRemaining == 0:
                drawImage(self.gameWindow, ASSETS_PIECE_BLACK, 100, 100, 980, 220)
            else:
                drawImage(self.gameWindow, ASSETS_PIECE_WHITE, 100, 100, 980, 220)

        else:
            self.gameWindow.blit(smallerFont.render(TEXT_WHOSE_MOVE, True, (50, 50, 50)), (820, 255))
            if whoseTurn == (0, 0, 0):
                drawImage(self.gameWindow, ASSETS_PIECE_BLACK, 100, 100, 980, 220)
            else:
                drawImage(self.gameWindow, ASSETS_PIECE_WHITE, 100, 100, 980, 220)

        # Draw buttons
        drawImage(self.gameWindow, ASSETS_MENU_RESET, 66, 350, 840, 600)
        drawImage(self.gameWindow, ASSETS_MENU_EXIT, 66, 350, 840, 700)

    def mouseClickEvent(self, mousePosition, gameController):
        x, y = mousePosition
        if x > 800 or y > 800:
            # Reset
            if 840 < x < 1190 and 600 < y < 670:
                gameController.reset()
                gameController.whoseTurn = PLAYER_BLACK
            # Exit
            if 840 < x < 1190 and 700 < y < 760:
                self.isRunning = False
            return -1, -1
        else:
            row = y // 100
            column = x // 100
            return row, column
