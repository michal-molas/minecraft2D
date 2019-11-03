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
        terrain.terrain[y + 1][x] = "sky"

    def fall(self, terrain, x, y):
        if terrain.terrain[y + 1][x] == "sky" and self.position[1] % 32 == 0:
            self.isFalling = True

    def move(self, terrain):
        #print(self.position)

        keys = pygame.key.get_pressed()

        playerIndexY = 64 - self.position[1] // 32
        if self.position[0] < 0:
            if self.position[0] % 32 < 16:
                playerIndexX = 500 + self.position[0] // 32 + config.screenWidth // 64
            else:
                playerIndexX = 500 + self.position[0] // 32 + config.screenWidth // 64 + 1
        else:
            if self.position[0] % 32 < 16:
                playerIndexX = 500 + self.position[0] // 32 + config.screenWidth // 64
            else:
                playerIndexX = 500 + self.position[0] // 32 + config.screenWidth // 64 + 1

        # terrain.terrain[playerIndexY][playerIndexX] = "water"

        #print(self.position[0] % 32)
        if keys[pygame.K_a] and (terrain.terrain[playerIndexY][playerIndexX - 1] == "sky"
                                 or self.position[0] % 32 > 16
                                 or playerIndexX != 500 + self.position[0] // 32 + config.screenWidth // 64 + 1):
            self.position[0] -= 1
        elif keys[pygame.K_d] and (terrain.terrain[playerIndexY][playerIndexX + 1] == "sky"
                                   or (self.position[0] % 32 < 16)
                                   or (playerIndexX != 500 + self.position[0] // 32 + config.screenWidth // 64
                                       and self.position[0] % 32 >= 16)):
            print(playerIndexX != 500 + self.position[0] // 32 + config.screenWidth // 64
                  and self.position[0] % 32 > 16)
            print(self.position[0] % 32 < 16)
            print(terrain.terrain[playerIndexY][playerIndexX + 1] == "sky")
            print(self.position[0] % 32)
            self.position[0] += 1

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
