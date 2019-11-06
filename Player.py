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

    eqOpened = False
    ePressed = False

    def jump(self):
        if self.jumpCount > 0:
            self.jumpCount -= 2
            self.position[1] += 2
        else:
            self.isFalling = True
            self.canJump = True
            self.jumpCount = 44

    def digDown(self, terrain, x, y, eq):
        if self.rightWall and terrain.terrain[y + 1][x - 1].breakable:
            if terrain.terrain[y + 1][x].type == "tree":
                self.cutTree(terrain, x, y + 1, eq)
            if terrain.terrain[y + 1][x].collectable:
                eq.setSlot(terrain.terrain[y + 1][x - 1].type)
            terrain.terrain[y + 1][x - 1].changeType("sky")
        elif terrain.terrain[y + 1][x].breakable:
            if terrain.terrain[y + 1][x].type == "tree":
                self.cutTree(terrain, x, y + 1, eq)
            if terrain.terrain[y + 1][x].collectable:
                eq.setSlot(terrain.terrain[y + 1][x].type)
            terrain.terrain[y + 1][x].changeType("sky")

    def startFall(self, terrain, x, y):
        if (self.position[1] % 32 == 0 and
                (terrain.terrain[y + 1][x].transparent
                 or (terrain.terrain[y + 1][x - 1].transparent and self.rightWall))):
            self.isFalling = True

    def fall(self, terrain, x, y):
        if self.isFalling:
            self.position[1] -= 2
            if self.position[1] % 32 == 0:
                self.isFalling = False
                self.startFall(terrain, x, y)

    def moveLeft(self, terrain, x, y):
        if not self.leftWall:
            if terrain.terrain[y][x].transparent or self.rightWall:
                self.position[0] -= 1
            self.canDigLeft = False
            self.canDigRight = False
        elif terrain.terrain[y][x - 1].breakable:
            self.canDigLeft = True

    def moveRight(self, terrain, x, y):
        if not self.rightWall:
            if terrain.terrain[y][x].transparent:
                self.position[0] += 1
            self.canDigLeft = False
            self.canDigRight = False
        elif terrain.terrain[y][x].breakable:
            self.canDigRight = True

    def checkWalls(self, terrain, x, y):
        if self.position[0] % 32 == 16:
            if not terrain.terrain[y][x - 1].transparent:
                self.leftWall = True
            else:
                self.leftWall = False
            if not terrain.terrain[y][x].transparent:
                self.rightWall = True
            else:
                self.rightWall = False
        else:
            self.leftWall = False
            self.rightWall = False

    def digLeftRight(self, terrain, x, y, eq):
        if self.canDigLeft:
            if terrain.terrain[y][x - 1].type == "tree":
                self.cutTree(terrain, x - 1, y, eq)
            if terrain.terrain[y][x - 1].collectable:
                eq.setSlot(terrain.terrain[y][x - 1].type)
            terrain.terrain[y][x - 1].changeType("sky")
            self.canDigLeft = False
        if self.canDigRight:
            if terrain.terrain[y][x].type == "tree":
                self.cutTree(terrain, x, y, eq)
            if terrain.terrain[y][x].collectable:
                eq.setSlot(terrain.terrain[y][x].type)
            terrain.terrain[y][x].changeType("sky")
            self.canDigRight = False

    def digUpOrStartJump(self, terrain, x, y, eq):
        if terrain.terrain[y - 1][x].transparent or (terrain.terrain[y - 1][x - 1].transparent and self.rightWall):
            self.canJump = False
        elif terrain.terrain[y - 1][x].breakable:
            if not self.rightWall:
                if terrain.terrain[y - 1][x].type == "tree":
                    self.cutTree(terrain, x, y - 1, eq)
                if terrain.terrain[y - 1][x].collectable:
                    eq.setSlot(terrain.terrain[y - 1][x].type)
                terrain.terrain[y - 1][x].changeType("sky")
            else:
                if terrain.terrain[y - 1][x - 1].type == "tree":
                    self.cutTree(terrain, x - 1, y - 1, eq)
                if terrain.terrain[y - 1][x - 1].collectable:
                    eq.setSlot(terrain.terrain[y - 1][x - 1].type)
                terrain.terrain[y - 1][x - 1].changeType("sky")

    def cutTree(self, terrain, x, y, eq):
        i = 1
        while terrain.terrain[y - i][x].type == "tree":
            eq.setSlot(terrain.terrain[y - i][x].type)
            terrain.terrain[y - i][x].changeType("sky")
            i += 1
        for n in range(3):
            for m in range(3):
                terrain.terrain[y - i - n][x - 1 + m].changeType("sky")

    def move(self, terrain, eq):

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
            self.digLeftRight(terrain, playerIndexX, playerIndexY, eq)

        if self.canJump:
            self.startFall(terrain, playerIndexX, playerIndexY)
            if keys[pygame.K_w] and not self.isFalling:
                self.digUpOrStartJump(terrain, playerIndexX, playerIndexY, eq)
            if keys[pygame.K_s] and not self.alreadyDigged and not self.isFalling:
                self.digDown(terrain, playerIndexX, playerIndexY, eq)
                self.alreadyDigged = True
        else:
            self.jump()

        if not keys[pygame.K_s]:
            self.alreadyDigged = False

        if keys[pygame.K_e]:
            if not self.ePressed:
                if not self.eqOpened:
                    self.eqOpened = True
                else:
                    self.eqOpened = False
            self.ePressed = True

        if not keys[pygame.K_e]:
            self.ePressed = False

        self.fall(terrain, playerIndexX, playerIndexY)

    def draw(self, window):
        window.blit(self.playerPng, (32*20, 32*10))
