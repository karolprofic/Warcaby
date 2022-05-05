import pygame
from pygame import mixer
from layout.Button import *
from scenes.PlayerVersusAI import PlayerVersusAI
from scenes.PlayerVersusPlayer import PlayerVersusPlayer

clicked = False
pygame.init()
screen = pygame.display.set_mode((1220, 800))
pygame.display.set_caption('Warcaby menu')
czcionka = pygame.font.SysFont('Calibri', 30)
zegar = pygame.time.Clock()


def RysujTlo(src):
    img = pygame.image.load(src)
    img.convert()
    rect = img.get_rect()
    rect.height = 800
    rect.width = 1220
    screen.blit(img, rect)
    pygame.draw.rect(screen, PLAYER_BLACK, rect, 1)

def StartMenu():
    global clicked
    global config_music

    mixer.init()
    mixer.music.load('./assets/music/track1.mp3')

    przycisk_muzyka_komunikat = 'Włącz muzykę'

    run = True
    while run:

        RysujTlo("./assets/menu/menu_mg_1.jpg")
        przycisk_polaczenie = Button(140, 256, 'Graj przeciwko AI', screen, czcionka)
        przycisk_start = Button(140, 385, 'Gra swobodna', screen, czcionka)
        przycisk_muzyka = Button(140, 515, przycisk_muzyka_komunikat, screen, czcionka)
        przycisk_koniec = Button(140, 642, 'Zakończ', screen, czcionka)

        if przycisk_polaczenie.drawButton():
            pygame.quit()
            PlayerVersusAI(False)

        if przycisk_start.drawButton():
            pygame.quit()
            PlayerVersusPlayer(False)

        if przycisk_muzyka.drawButton():
            if config_music:
                config_music = False
                przycisk_muzyka_komunikat = 'Włącz muzykę'
                mixer.music.stop()
            else:
                config_music = True
                przycisk_muzyka_komunikat = 'Wyłącz muzykę'
                mixer.music.play()

        if przycisk_koniec.drawButton():
            print('Kliknięto koniec')
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()