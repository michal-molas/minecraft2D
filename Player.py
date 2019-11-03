import config
import pygame


class Player:
    screenPosX = config.screenWidth
    screenPosY = config.screenHeight

    position = [0, 0]

    playerPng = pygame.image.load("player.png")

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.position[0] -= 1
        elif keys[pygame.K_d]:
            self.position[0] += 1
        elif keys[pygame.K_w]:
            self.position[1] += 1
        elif keys[pygame.K_s]:
            self.position[1] -= 1

        print(self.position)

    def draw(self, window):
        window.blit(self.playerPng, (32*20, 32*10))
