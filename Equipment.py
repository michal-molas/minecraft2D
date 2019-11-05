import pygame


class Equipment:
    slotPng = pygame.image.load("slot.png")
    slotDirtPng = pygame.image.load("slotDirt.png")
    slotStonePng = pygame.image.load("slotStone.png")
    slotTreePng = pygame.image.load("slotTree.png")
    slotIronPng = pygame.image.load("slotIron.png")
    slotGoldPng = pygame.image.load("slotGold.png")
    slotDiamondPng = pygame.image.load("slotDiamond.png")

    barSlots = []

    def __init__(self):
        for i in range(10):
            self.barSlots.append("empty")

    def drawBar(self, window):
        for i in range(10):
            if self.barSlots[i] == "empty":
                window.blit(self.slotPng, (480 + i * 32, 576))
            elif self.barSlots[i] == "dirt":
                window.blit(self.slotDirtPng, (480 + i * 32, 576))
            elif self.barSlots[i] == "tree":
                window.blit(self.slotTreePng, (480 + i * 32, 576))
            elif self.barSlots[i] == "stone":
                window.blit(self.slotStonePng, (480 + i * 32, 576))
            elif self.barSlots[i] == "iron":
                window.blit(self.slotIronPng, (480 + i * 32, 576))
            elif self.barSlots[i] == "gold":
                window.blit(self.slotGoldPng, (480 + i * 32, 576))
            elif self.barSlots[i] == "diamond":
                window.blit(self.slotDiamondPng, (480 + i * 32, 576))

    def setSlot(self, item):
        for i in range(10):
            if self.barSlots[i] == "empty":
                self.barSlots[i] = item
                break
