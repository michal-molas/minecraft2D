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

    canDig = True
    alreadyDigged = False

    isFalling = False
    fallCount = 0

    lastGround = ""
    leftWall = False
    rightWall = False

    def jump(self):
        if self.jumpCount > 0:
            if self.jumpCount > 3 * self.jumpHeight // 4:
                self.position[1] += 3
            elif self.jumpCount > 2 * self.jumpHeight // 4:
                self.position[1] += 1
            elif self.jumpCount > self.jumpHeight // 4:
                self.position[1] -= 1
            else:
                self.position[1] -= 3
            self.jumpCount -= 1
        else:
            self.canJump = True
            self.jumpCount = self.jumpHeight

    def dig(self, terrain, x, y):
        if self.rightWall:
            terrain.terrain[y + 1][x - 1] = "sky"
        else:
            terrain.terrain[y + 1][x] = "sky"

    def fall(self, terrain, x, y):
        if (self.position[1] % 32 == 0 and
                (terrain.terrain[y + 1][x] == "sky"
                 or (terrain.terrain[y + 1][x - 1] == "sky" and self.position[0] % 32 == 16))):
            self.isFalling = True

    def move(self, terrain):

        keys = pygame.key.get_pressed()

        playerIndexY = 64 - self.position[1] // 32
        if self.position[0] % 32 < 16:
            playerIndexX = 500 + self.position[0] // 32 + config.screenWidth // 64
        else:
            playerIndexX = 500 + self.position[0] // 32 + config.screenWidth // 64 + 1

        if keys[pygame.K_a] and ((terrain.terrain[playerIndexY][playerIndexX] == "sky" and self.position[0] % 32 != 16)
                                 or (terrain.terrain[playerIndexY][playerIndexX - 1] == "sky"
                                     and terrain.terrain[playerIndexY][playerIndexX] != "sky"
                                     and self.position[0] % 32 == 16)):
            self.position[0] -= 1
            if self.position[0] % 32 == 16:
                self.leftWall = True
            else:
                self.leftWall = False
                self.rightWall = False
        elif keys[pygame.K_d] and (terrain.terrain[playerIndexY][playerIndexX] == "sky"):
            self.position[0] += 1
            if self.position[0] % 32 == 16:
                self.rightWall = True
            else:
                self.leftWall = False
                self.rightWall = False

        if self.canJump:
            self.fall(terrain, playerIndexX, playerIndexY)
            if keys[pygame.K_w] and not self.isFalling:
                self.canJump = False
            if keys[pygame.K_s] and not self.alreadyDigged and not self.isFalling:
                self.dig(terrain, playerIndexX, playerIndexY)
                self.alreadyDigged = True
        else:
            self.jump()

        if not keys[pygame.K_s]:
            self.alreadyDigged = False

        # falling
        if self.isFalling:
            self.position[1] -= 2
            self.fallCount += 2

        if self.fallCount == 32:
            self.fallCount = 0
            self.isFalling = False
        # falling end

    def draw(self, window):
        window.blit(self.playerPng, (32*20, 32*10))
