import config
import pygame


class Player:
    screenPosX = config.screenWidth
    screenPosY = config.screenHeight

    position = [0, 0]

    playerPng = pygame.image.load("player.png")

    canJump = True
    jumpCount = 44

    canDig = True
    alreadyDigged = False

    canDigLeft = False
    canDigRight = False

    clickedMouse = False

    isFalling = False

    leftWall = False
    rightWall = False

    def jump(self):
        if self.jumpCount > 0:
            self.jumpCount -= 2
            self.position[1] += 2
        else:
            self.isFalling = True
            self.canJump = True
            self.jumpCount = 44

    def digDown(self, terrain, x, y):
        if self.rightWall:
            terrain.terrain[y + 1][x - 1] = "sky"
        else:
            terrain.terrain[y + 1][x] = "sky"

    def fall(self, terrain, x, y):
        if (self.position[1] % 32 == 0 and
                (terrain.terrain[y + 1][x] == "sky"
                 or (terrain.terrain[y + 1][x - 1] == "sky" and self.rightWall))):
            self.isFalling = True

    def move(self, terrain):

        print(self.rightWall)

        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()

        playerIndexY = 64 - self.position[1] // 32
        if self.position[0] % 32 < 16:
            playerIndexX = 500 + self.position[0] // 32 + config.screenWidth // 64
        else:
            playerIndexX = 500 + self.position[0] // 32 + config.screenWidth // 64 + 1

        if keys[pygame.K_a]:
            if not self.leftWall:
                if terrain.terrain[playerIndexY][playerIndexX] == "sky" or self.rightWall:
                    self.position[0] -= 1
                    if self.position[0] % 32 == 16 and terrain.terrain[playerIndexY][playerIndexX - 1] != "sky":
                        self.leftWall = True
                    else:
                        self.leftWall = False
                        self.rightWall = False
                self.canDigLeft = False
                self.canDigRight = False
            else:
                self.canDigLeft = True

        if keys[pygame.K_d]:
            if not self.rightWall:
                if terrain.terrain[playerIndexY][playerIndexX] == "sky":
                    self.position[0] += 1
                    if self.position[0] % 32 == 16 and terrain.terrain[playerIndexY][playerIndexX + 1] != "sky":
                        self.rightWall = True
                    else:
                        self.leftWall = False
                        self.rightWall = False
                self.canDigLeft = False
                self.canDigRight = False
            else:
                self.canDigRight = True

        if mouse[0]:
            if self.canDigLeft:
                terrain.terrain[playerIndexY][playerIndexX - 1] = "sky"
                self.leftWall = False
                self.canDigLeft = False
            if self.canDigRight:
                terrain.terrain[playerIndexY][playerIndexX] = "sky"
                self.rightWall = False
                self.canDigRight = False

        if self.canJump:
            self.fall(terrain, playerIndexX, playerIndexY)
            if keys[pygame.K_w] and not self.isFalling:
                if terrain.terrain[playerIndexY - 1][playerIndexX] == "sky"\
                        or (terrain.terrain[playerIndexY - 1][playerIndexX - 1] == "sky" and self.rightWall):
                    self.canJump = False
                else:
                    if not self.rightWall:
                        terrain.terrain[playerIndexY - 1][playerIndexX] = "sky"
                    else:
                        terrain.terrain[playerIndexY - 1][playerIndexX - 1] = "sky"
            if keys[pygame.K_s] and not self.alreadyDigged and not self.isFalling:
                self.digDown(terrain, playerIndexX, playerIndexY)
                self.alreadyDigged = True
        else:
            self.jump()

        if not keys[pygame.K_s]:
            self.alreadyDigged = False

        # falling
        if self.isFalling:
            self.position[1] -= 2
            if self.position[1] % 32 == 0:
                self.isFalling = False
                self.fall(terrain, playerIndexX, playerIndexY)
        # falling end

        if terrain.terrain[playerIndexY][playerIndexX - 1] == "sky":
            self.leftWall = False
        if terrain.terrain[playerIndexY][playerIndexX + 1] == "sky":
            self.rightWall = False

    def draw(self, window):
        window.blit(self.playerPng, (32*20, 32*10))
