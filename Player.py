import config
import pygame


class Player:
    screenPosX = config.screenWidth
    screenPosY = config.screenHeight

    position = [0, 0]

    playerPng = pygame.image.load("player.png")

    canJump = True
    jumpCount = 44

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
        if self.rightWall and terrain.terrain[y + 1][x - 1] != "bedrock":
            terrain.terrain[y + 1][x - 1] = "sky"
        elif terrain.terrain[y + 1][x] != "bedrock":
            terrain.terrain[y + 1][x] = "sky"

    def startFall(self, terrain, x, y):
        if (self.position[1] % 32 == 0 and
                (terrain.terrain[y + 1][x] == "sky"
                 or (terrain.terrain[y + 1][x - 1] == "sky" and self.rightWall))):
            self.isFalling = True

    def fall(self, terrain, x, y):
        if self.isFalling:
            self.position[1] -= 2
            if self.position[1] % 32 == 0:
                self.isFalling = False
                self.startFall(terrain, x, y)

    def moveLeft(self, terrain, x, y):
        if not self.leftWall:
            if terrain.terrain[y][x] == "sky" or self.rightWall:
                self.position[0] -= 1
            self.canDigLeft = False
            self.canDigRight = False
        elif terrain.terrain[y][x - 1] != "bedrock":
            self.canDigLeft = True

    def moveRight(self, terrain, x, y):
        if not self.rightWall:
            if terrain.terrain[y][x] == "sky":
                self.position[0] += 1
            self.canDigLeft = False
            self.canDigRight = False
        elif terrain.terrain[y][x] != "bedrock":
            self.canDigRight = True

    def checkWalls(self, terrain, x, y):
        if self.position[0] % 32 == 16:
            if terrain.terrain[y][x - 1] != "sky":
                self.leftWall = True
            else:
                self.leftWall = False
            if terrain.terrain[y][x] != "sky":
                self.rightWall = True
            else:
                self.rightWall = False
        else:
            self.leftWall = False
            self.rightWall = False

    def digLeftRight(self, terrain, x, y):
        if self.canDigLeft:
            terrain.terrain[y][x - 1] = "sky"
            self.canDigLeft = False
        if self.canDigRight:
            terrain.terrain[y][x] = "sky"
            self.canDigRight = False

    def move(self, terrain):

        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()

        playerIndexY = 64 - self.position[1] // 32
        if self.position[0] % 32 < 16:
            playerIndexX = 500 + self.position[0] // 32 + config.screenWidth // 64
        else:
            playerIndexX = 500 + self.position[0] // 32 + config.screenWidth // 64 + 1

        self.checkWalls(terrain, playerIndexX, playerIndexY)

        if keys[pygame.K_a]:
            self.moveLeft(terrain, playerIndexX, playerIndexY)

        if keys[pygame.K_d]:
            self.moveRight(terrain, playerIndexX, playerIndexY)

        if mouse[0]:
            self.digLeftRight(terrain, playerIndexX, playerIndexY)

        if self.canJump:
            self.startFall(terrain, playerIndexX, playerIndexY)
            if keys[pygame.K_w] and not self.isFalling:
                if terrain.terrain[playerIndexY - 1][playerIndexX] == "sky"\
                        or (terrain.terrain[playerIndexY - 1][playerIndexX - 1] == "sky" and self.rightWall):
                    self.canJump = False
                elif terrain.terrain[playerIndexY - 1][playerIndexX] != "bedrock":
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

        self.fall(terrain, playerIndexX, playerIndexY)

    def draw(self, window):
        window.blit(self.playerPng, (32*20, 32*10))
