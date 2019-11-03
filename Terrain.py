import pygame
import config


class Terrain:

    terrain = []

    dirtPng = pygame.image.load("dirt.png")
    waterPng = pygame.image.load("water.png")
    stonePng = pygame.image.load("stone.png")
    skyPng = pygame.image.load("sky.png")

    def createTerrain(self):
        for i in range(128):
            terrainLayer = []
            for j in range(1000):
                if i > 64:
                    if j % 2 == 0:
                        terrainLayer.append("dirt")
                    else:
                        terrainLayer.append("stone")
                else:
                    terrainLayer.append("sky")
            self.terrain.append(terrainLayer)

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

                if self.terrain[indexY][indexX] == "dirt":
                    window.blit(self.dirtPng, (posX, posY))
                elif self.terrain[indexY][indexX] == "water":
                    window.blit(self.waterPng, (posX, posY))
                elif self.terrain[indexY][indexX] == "stone":
                    window.blit(self.stonePng, (posX, posY))
                elif self.terrain[indexY][indexX] == "sky":
                    window.blit(self.skyPng, (posX, posY))
