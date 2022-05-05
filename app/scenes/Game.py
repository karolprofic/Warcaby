import pygame
from pygame import mixer
from layout.Button import *
from checkers.Controller import *
from commons.constants import *

class Game:

    def __init__(self, music):
        self.config_music = music
        self.isRunning = True
        self.WIN = pygame.display.set_mode((1220, 800))

        if self.config_music:
            mixer.init()
            mixer.music.load(ASSETS_MUSIC_1)
            mixer.music.play()

        pygame.display.set_caption(GAME_TITLE)

    def drawMenu(self, pozostalo_czarnych, pozostalo_bialych, krolowe_czarne, krolowe_biale, czyja_kolejka):
        bigfont = pygame.font.SysFont(FONT_NAME, 36)
        smallfont = pygame.font.SysFont(FONT_NAME, 22)

        self.WIN.blit(bigfont.render(TEXT_TITLE, True, (50, 50, 50)), (820, 20))
        self.WIN.blit(smallfont.render(str(TEXT_WHITE_REMAINING + str(pozostalo_bialych)), True, (50, 50, 50)), (820, 70))
        self.WIN.blit(smallfont.render(str(TEXT_BLACK_REMAINING + str(pozostalo_czarnych)), True, (50, 50, 50)), (820, 110))
        self.WIN.blit(smallfont.render(str(TEXT_BLACK_KINGS + str(krolowe_czarne)), True, (50, 50, 50)), (820, 150))
        self.WIN.blit(smallfont.render(str(TEXT_WHITE_KINGS + str(krolowe_biale)), True, (50, 50, 50)), (820, 190))

        # Rysowanie czyj ruch i kto wygrał
        if pozostalo_czarnych == 0 or pozostalo_bialych == 0:
            self.WIN.blit(smallfont.render(TEXT_WIN, True, (50, 50, 50)), (820, 255))
            if pozostalo_bialych == 0:
                self.drawImage(ASSETS_PIECE_BLACK, 100, 100, 980, 220)
            else:
                self.drawImage(ASSETS_PIECE_WHITE, 100, 100, 980, 220)

        else:
            self.WIN.blit(smallfont.render(TEXT_WHOSE_MOVE, True, (50, 50, 50)), (820, 255))
            if czyja_kolejka == (0, 0, 0):
                self.drawImage(ASSETS_PIECE_BLACK, 100, 100, 980, 220)
            else:
                self.drawImage(ASSETS_PIECE_WHITE, 100, 100, 980, 220)

        # Rysowanie przycisków
        self.drawImage(ASSETS_MENU_RESET, 66, 350, 840, 600)
        self.drawImage(ASSETS_MENU_EXIT, 66, 350, 840, 700)

    def oblicz_rzad_i_kolumne(self, mousePosition, gra):
        x, y = mousePosition
        if x > 100*8 or y > 100*8:
            # Reset
            if (x > 840 and x < 1190 and y > 600 and y < 670):
                gra.zresetuj_gre()
                gra.czyja_kolej = PLAYER_BLACK
            # Exit
            if x > 840 and x < 1190 and y > 700 and y < 760:
                self.isRunning = False
            return -1, -1
        else:
            row = y // 100
            column = x // 100
            return row, column

    def drawImage(self, src, height, width, left, top):
        img = pygame.image.load(src)
        img.convert()
        el = img.get_rect()
        el.height = height
        el.width = width
        el.left = left
        el.top = top
        self.WIN.blit(img, el)
        pygame.draw.rect(self.WIN, (255, 255, 255), el, 1)
