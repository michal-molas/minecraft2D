import pygame


class Terrain:

    terrain = []
    terrainLayer = []

    dirtPng = pygame.image.load("dirt.png")

    def createTerrain(self):
        for i in range(64):
            for j in range(1000):
                self.terrainLayer.append("dirt")
            self.terrain.append(self.terrainLayer)

    def draw(self, window):
        for i in range(64):
            for j in range(1000):
                if self.terrain[i][j] == "dirt":
                    window.blit(self.dirtPng, (j*32, i*32))