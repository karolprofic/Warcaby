import pygame
from pygame import mixer
from layout.Button import *
from checkers.Controller import *


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Game:

    def __init__(self, music):
        self.config_music = music
        self.WIN = pygame.display.set_mode((1220, 800))

        if (self.config_music):
            mixer.init()
            mixer.music.load('./assets/Muzyka/track1.mp3')
            mixer.music.play()

        pygame.display.set_caption('Warcaby')

        self.start()

    def drawMenu(self, pozostalo_czarnych, pozostalo_bialych, krolowe_czarne, krolowe_biale, czyja_kolejka):
        bigfont = pygame.font.SysFont('Calibri', 36)
        smallfont = pygame.font.SysFont('Calibri', 22)

        self.WIN.blit(bigfont.render('Warcaby:', True, (50, 50, 50)), (820, 20))
        self.WIN.blit(smallfont.render(str('Pozostało białych pinków: ' + str(pozostalo_bialych)), True, (50, 50, 50)), (820, 70))
        self.WIN.blit(smallfont.render(str('Pozostało czarnych pinków: ' + str(pozostalo_czarnych)), True, (50, 50, 50)), (820, 110))
        self.WIN.blit(smallfont.render(str('Liczba czarnych króli: ' + str(krolowe_czarne)), True, (50, 50, 50)), (820, 150))
        self.WIN.blit(smallfont.render(str('Liczba białych króli: ' + str(krolowe_biale)), True, (50, 50, 50)), (820, 190))

        # Rysowanie czyj ruch i kto wygrał
        if(pozostalo_czarnych == 0 or pozostalo_bialych == 0):
            self.WIN.blit(smallfont.render('Wygrali: ', True, (50, 50, 50)), (820, 255))
            if pozostalo_bialych == 0:
                img = pygame.image.load("./assets/Pionki/black.png")
            else:
                img = pygame.image.load("./assets/Pionki/white.png")
            img.convert()
            el = img.get_rect()  #
            el.height = 100  #
            el.width = 100  #
            el.left = 980
            el.top = 220
            self.WIN.blit(img, el)
            pygame.draw.rect(self.WIN, (255, 255, 255), el, 1)
        else:
            self.WIN.blit(smallfont.render('Ruch należy do: ', True, (50, 50, 50)), (820, 255))
            if czyja_kolejka == (0, 0, 0):
                img = pygame.image.load("./assets/Pionki/black.png")
            else:
                img = pygame.image.load("./assets/Pionki/white.png")
            img.convert()
            el = img.get_rect()  #
            el.height = 100  #
            el.width = 100  #
            el.left = 980
            el.top = 220
            self.WIN.blit(img, el)
            pygame.draw.rect(self.WIN, (255, 255, 255), el, 1)

        # Rysowanie przycisku
        img = pygame.image.load("./assets/Menu/reset.png")
        img.convert()
        el = img.get_rect()
        el.height = 66
        el.width = 350
        el.left = 840
        el.top = 700
        self.WIN.blit(img, el)
        pygame.draw.rect(self.WIN, (255, 255, 255), el, 1)

    def oblicz_rzad_i_kolumne(self, pos, gra):
        x, y = pos
        if(x > 100*8 or y > 100*8):
            # Reset
            if(x > 840 and x < 1190 and y > 700 and y < 760):
                gra.zresetuj_gre()
                gra.czyja_kolej = BLACK_COLOR
            return -1, -1
        else:
            rzad = y // 100
            kolumna = x // 100
            return rzad, kolumna
