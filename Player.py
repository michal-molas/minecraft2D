import config
import pygame


class Player:
    screenPosX = config.screenWidth
    screenPosY = config.screenHeight

    playerPng = pygame.image.load("player.png")

    def draw(self, window):
        window.blit(self.playerPng, (self.screenPosX / 2, self.screenPosY / 2))
