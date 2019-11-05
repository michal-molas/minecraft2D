import pygame
import config
import Block
import random


class Terrain:

    terrain = []

    dirtPng = pygame.image.load("dirt.png")
    waterPng = pygame.image.load("water.png")
    stonePng = pygame.image.load("stone.png")
    grassPng = pygame.image.load("grass.png")
    skyPng = pygame.image.load("sky.png")
    bedrockPng = pygame.image.load("bedrock.png")
    treePng = pygame.image.load("tree.png")
    leavesPng = pygame.image.load("leaves.png")

    def createTerrain(self):
        for i in range(140):
            terrainLayer = []
            for j in range(1000):
                if i > 128:
                    terrainLayer.append(Block.Block("bedrock"))
                elif i > 80:
                    terrainLayer.append(Block.Block("stone"))
                elif i > 69:
                    rand = random.randint(0, 10)
                    if rand > 79 - i:
                        terrainLayer.append(Block.Block("stone"))
                    else:
                        terrainLayer.append(Block.Block("dirt"))
                elif i > 64:
                    terrainLayer.append(Block.Block("dirt"))
                else:
                    terrainLayer.append(Block.Block("sky"))
            self.terrain.append(terrainLayer)

        self.createForestBiome(300, 600)

    def createForestBiome(self, a, b):
        for i in range((b-a)//4):
            self.createTree(a, b)

    def createTree(self, a, b):
        x = random.randint(a, b)
        y = -1
        i = 139
        treeSize = random.randint(3, 5)
        freeSpace = True
        while i >= 0:
            if self.terrain[i][x].type == "sky" and self.terrain[i+1][x].type == "dirt" and x != 520:
                for n in range(5):
                    for m in (-1, 1):
                        if self.terrain[i-n][x+m].type != "sky":
                            freeSpace = False

                if freeSpace:
                    y = i
                    for n in range(treeSize):
                        self.terrain[y - n][x] = Block.Block("tree")
                    for n in range(3):
                        for m in range(3):
                            self.terrain[y - 2 - treeSize + n][x - 1 + m] = Block.Block("leaves")
                else:
                    self.createTree(a, b)
                break
            i -= 1

    def draw(self, window, player):
        for i in range(config.screenHeight // 32 + 2):
            for j in range(config.screenWidth // 32 + 2):
                indexY = i + 64 - (config.screenHeight//32) // 2 - player.position[1]//32 - 1
                indexX = j + 500 + player.position[0] // 32
                if player.position[0] >= 0:
                    posX = j * 32 - player.position[0] % 32
                else:
                    posX = j * 32 + (32 - player.position[0] % 32) - 32
                if player.position[1] >= 0:
                    posY = i * 32 + player.position[1] % 32 - 32
                else:
                    posY = i * 32 - (32 - player.position[1] % 32)

                if self.terrain[indexY][indexX].type == "dirt":
                    window.blit(self.dirtPng, (posX, posY))
                elif self.terrain[indexY][indexX].type == "water":
                    window.blit(self.waterPng, (posX, posY))
                elif self.terrain[indexY][indexX].type == "stone":
                    window.blit(self.stonePng, (posX, posY))
                elif self.terrain[indexY][indexX].type == "sky":
                    window.blit(self.skyPng, (posX, posY))
                elif self.terrain[indexY][indexX].type == "bedrock":
                    window.blit(self.bedrockPng, (posX, posY))
                elif self.terrain[indexY][indexX].type == "grass":
                    window.blit(self.grassPng, (posX, posY))
                elif self.terrain[indexY][indexX].type == "tree":
                    window.blit(self.treePng, (posX, posY))
                elif self.terrain[indexY][indexX].type == "leaves":
                    window.blit(self.leavesPng, (posX, posY))
