import pygame
from checkers.Board import *

BIALY = (255, 255, 255)
CZARNY = (0, 0, 0)

class Warcaby:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.drawPiecesOnBoard(self.win)
        self.rysuj_podpowiedzi(self.mozliwe_ruchy)
        pygame.display.update()

    def _init(self):
        self.aktywny_pionek = None
        self.board = Plansza()
        self.czyja_kolej = BLACK_COLOR
        self.mozliwe_ruchy = {}

    def kto_wygral(self):
        return self.board.kto_wygral()

    def zresetuj_gre(self):
        self._init()

    def wybierz_pionka(self, rzad, kolumna):
        if self.aktywny_pionek:
            if not self.przesun(rzad, kolumna):
                self.aktywny_pionek = None
                self.wybierz_pionka(rzad, kolumna)

        pionek = self.board.boardArray[rzad][kolumna]
        if pionek != 0 and pionek.color == self.czyja_kolej:
            self.aktywny_pionek = pionek
            self.mozliwe_ruchy = self.board.findPossibleMoves(pionek)
            return True

        return False

    def przesun(self, rzad, kolumna):
        pionek = self.board.boardArray[rzad][kolumna]
        if self.aktywny_pionek and pionek == 0 and (rzad, kolumna) in self.mozliwe_ruchy:
            self.board.movePiece(self.aktywny_pionek, rzad, kolumna)
            przeskok = self.mozliwe_ruchy[(rzad, kolumna)]
            if przeskok:
                self.board.usun_pionka(przeskok)
            self.zmien_gracza()
        else:
            return False

        return True

    def rysuj_podpowiedzi(self, mozliwe_ruchy):
        for ruch in mozliwe_ruchy:
            row, col = ruch
            img = pygame.image.load("./assets/Pionki/move.png")
            img.convert()
            el = img.get_rect()#
            el.height = 100#
            el.width = 100#
            el.left = col * 100
            el.top = row * 100
            self.win.blit(img, el)
            pygame.draw.rect(self.win, (90, 53, 9), el, 1)

    def zmien_gracza(self):
        self.mozliwe_ruchy = {}
        if self.czyja_kolej == BLACK_COLOR:
            self.czyja_kolej = WHITE_COLOR
        else:
            self.czyja_kolej = BLACK_COLOR