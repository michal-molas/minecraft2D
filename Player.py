import config
import pygame
import Terrain


class Player:
    screenPosX = config.screenWidth
    screenPosY = config.screenHeight

    position = [0, 0]

    playerPng = pygame.image.load("player.png")

    canJump = True
    jumpHeight = 44
    jumpCount = jumpHeight

    def jump(self):
        if self.jumpCount > 0:
            if self.jumpCount > 3 * (self.jumpHeight//4):
                self.position[1] += 3
            elif self.jumpCount > 2 * (self.jumpHeight//4):
                self.position[1] += 1
            elif self.jumpCount > self.jumpHeight//4:
                self.position[1] -= 1
            else:
                self.position[1] -= 3
            self.jumpCount -= 1
        else:
            self.canJump = True
            self.jumpCount = self.jumpHeight

    def dig(self, terrain):
        indexY = 64 - self.position[1] // 32 + 1
        if self.position[0] < 0:
            if self.position[0] % 32 < 16:
                indexX = 500 + self.position[0] // 32 + config.screenWidth // 64
            else:
                indexX = 500 + self.position[0] // 32 + config.screenWidth // 64 + 1
        else:
            if self.position[0] % 32 < 16:
                indexX = 500 + self.position[0] // 32 + config.screenWidth // 64
            else:
                indexX = 500 + self.position[0] // 32 + config.screenWidth // 64 + 1
        terrain.terrain[indexY][indexX] = "water"

    def move(self, terrain):
        print(self.position)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.position[0] -= 1
        elif keys[pygame.K_d]:
            self.position[0] += 1

        if self.canJump:
            if keys[pygame.K_w]:
                self.canJump = False
            if keys[pygame.K_s]:
                self.dig(terrain)
        else:
            self.jump()

    def draw(self, window):
        window.blit(self.playerPng, (32*20, 32*10))
