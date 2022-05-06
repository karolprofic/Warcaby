import pygame
from pygame import mixer
from layout.Button import *
from scenes.PlayerVersusAI import PlayerVersusAI
from scenes.PlayerVersusPlayer import PlayerVersusPlayer

class Menu:

    def __init__(self):
        self.isRunning = True
        pygame.init()
        pygame.display.set_caption('Warcaby menu')
        self.gameWindow = pygame.display.set_mode((1220, 800))
        self.font = pygame.font.SysFont('Calibri', 30)
        self.music = False
        self.start()

    def start(self):
        mixer.init()
        mixer.music.load(ASSETS_MUSIC_1)
        musicButtonText = TEXT_MUSIC_ON

        while self.isRunning:
            drawImage(self.gameWindow, ASSETS_MENU_BACKGROUND, 800, 1220, 0, 0, (0, 0, 0))
            buttonPlayerVsAI = Button(140, 256, TEXT_PvAI, self.gameWindow, self.font)
            buttonPlayerVsPlayer = Button(140, 385, TEXT_PvP, self.gameWindow, self.font)
            ButtonMusic = Button(140, 515, musicButtonText, self.gameWindow, self.font)
            buttonExit = Button(140, 642, TEXT_END, self.gameWindow, self.font)

            if buttonPlayerVsAI.drawButton():
                pygame.quit()
                PlayerVersusAI(self.music)

            if buttonPlayerVsPlayer.drawButton():
                pygame.quit()
                PlayerVersusPlayer(self.music)

            if ButtonMusic.drawButton():
                if self.music:
                    self.music = False
                    musicButtonText = TEXT_MUSIC_ON
                    mixer.music.stop()
                else:
                    self.music = True
                    musicButtonText = TEXT_MUSIC_OFF
                    mixer.music.play()

            if buttonExit.drawButton():
                self.isRunning = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isRunning = False

            pygame.display.update()

        pygame.quit()