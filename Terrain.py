import pygame
import config
import Block
import random


class Terrain:

    terrain = []

    world_size_x = 1280

    dirt_png = pygame.image.load("dirt.png")
    water_png = pygame.image.load("water.png")
    stone_png = pygame.image.load("stone.png")
    grass_png = pygame.image.load("grass.png")
    sky_png = pygame.image.load("sky.png")
    bedrock_png = pygame.image.load("bedrock.png")
    tree_png = pygame.image.load("tree.png")
    leaves_png = pygame.image.load("leaves.png")
    iron_png = pygame.image.load("iron.png")
    gold_png = pygame.image.load("gold.png")
    diamond_png = pygame.image.load("diamond.png")

    def create_terrain(self):
        for i in range(140):
            terrain_layer = []
            for j in range(self.world_size_x):
                if i > 128:
                    terrain_layer.append(Block.Block("bedrock", j, i))
                elif i > 80:
                    terrain_layer.append(Block.Block("stone", j, i))
                elif i > 69:
                    rand = random.randint(0, 10)
                    if rand > 79 - i:
                        terrain_layer.append(Block.Block("stone", j, i))
                    else:
                        terrain_layer.append(Block.Block("dirt", j, i))
                elif i > 64:
                    if j % 2 == 0:
                        terrain_layer.append(Block.Block("dirt", j, i))
                    else:
                        terrain_layer.append(Block.Block("stone", j, i))
                else:
                    terrain_layer.append(Block.Block("sky", j, i))
            self.terrain.append(terrain_layer)

        self.create_resources()
        self.create_forest_biome(600, 900)

    def create_forest_biome(self, a, b):
        for i in range((b-a)//4):
            self.create_tree(a, b)

    def create_resources(self):
        for i in range(80, 129):
            for j in range(self.world_size_x):
                self.create_iron(j, i)
                if i > 90:
                    self.create_gold(j, i)
                if i > 110:
                    self.create_diamonds(j, i)

    def create_iron(self, x, y):
        rand = random.randint(0, 50)
        if rand == 0:
            self.terrain[y][x].change_type("iron")

    def create_gold(self, x, y):
        rand = random.randint(0, 200)
        if rand == 0:
            self.terrain[y][x].change_type("gold")

    def create_diamonds(self, x, y):
        rand = random.randint(0, 1000)
        if rand == 0:
            self.terrain[y][x].change_type("diamond")

    def create_tree(self, a, b):
        x = random.randint(a, b)
        i = 139
        tree_size = random.randint(3, 5)
        free_space = True
        while i >= 0:
            if self.terrain[i][x].type == "sky" and self.terrain[i+1][x].type == "dirt" and x != self.world_size_x // 2:
                for n in range(5):
                    for m in (-1, 1):
                        if self.terrain[i-n][x+m].type != "sky":
                            free_space = False

                if free_space:
                    for n in range(tree_size):
                        self.terrain[i - n][x].change_type("tree")
                    for n in range(3):
                        for m in range(3):
                            self.terrain[i - 2 - tree_size + n][x - 1 + m].change_type("leaves")
                else:
                    self.create_tree(a, b)
                break
            i -= 1

    def draw(self, window, player):
        for i in range(config.screen_height // 32 + 2):
            for j in range(config.screen_width // 32 + 2):
                index_y = i + player.position[1] // 32 - config.screen_height // 64 - 1
                index_x = j + player.position[0] // 32 - config.screen_width // 64

                pos_x = j * 32 - player.position[0] % 32
                pos_y = i * 32 - player.position[1] % 32

                if self.terrain[index_y][index_x].type == "dirt":
                    window.blit(self.dirt_png, (pos_x, pos_y))
                elif self.terrain[index_y][index_x].type == "water":
                    window.blit(self.water_png, (pos_x, pos_y))
                elif self.terrain[index_y][index_x].type == "stone":
                    window.blit(self.stone_png, (pos_x, pos_y))
                elif self.terrain[index_y][index_x].type == "sky":
                    window.blit(self.sky_png, (pos_x, pos_y))
                elif self.terrain[index_y][index_x].type == "bedrock":
                    window.blit(self.bedrock_png, (pos_x, pos_y))
                elif self.terrain[index_y][index_x].type == "grass":
                    window.blit(self.grass_png, (pos_x, pos_y))
                elif self.terrain[index_y][index_x].type == "tree":
                    window.blit(self.tree_png, (pos_x, pos_y))
                elif self.terrain[index_y][index_x].type == "leaves":
                    window.blit(self.leaves_png, (pos_x, pos_y))
                elif self.terrain[index_y][index_x].type == "iron":
                    window.blit(self.iron_png, (pos_x, pos_y))
                elif self.terrain[index_y][index_x].type == "gold":
                    window.blit(self.gold_png, (pos_x, pos_y))
                elif self.terrain[index_y][index_x].type == "diamond":
                    window.blit(self.diamond_png, (pos_x, pos_y))
