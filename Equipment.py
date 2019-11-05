import pygame
import Slot


class Equipment:
    slotPng = pygame.image.load("slot.png")
    slotDirtPng = pygame.image.load("slotDirt.png")
    slotStonePng = pygame.image.load("slotStone.png")
    slotTreePng = pygame.image.load("slotTree.png")
    slotIronPng = pygame.image.load("slotIron.png")
    slotGoldPng = pygame.image.load("slotGold.png")
    slotDiamondPng = pygame.image.load("slotDiamond.png")

    pygame.font.init()

    quantityFont = pygame.font.SysFont("arial", 16)

    barSlots = []

    def __init__(self):
        for i in range(10):
            self.barSlots.append(Slot.Slot("empty"))

    def drawBar(self, window):
        for i in range(10):
            if self.barSlots[i].item == "empty":
                window.blit(self.slotPng, (480 + i * 32, 576))
            elif self.barSlots[i].item == "dirt":
                window.blit(self.slotDirtPng, (480 + i * 32, 576))
            elif self.barSlots[i].item == "tree":
                window.blit(self.slotTreePng, (480 + i * 32, 576))
            elif self.barSlots[i].item == "stone":
                window.blit(self.slotStonePng, (480 + i * 32, 576))
            elif self.barSlots[i].item == "iron":
                window.blit(self.slotIronPng, (480 + i * 32, 576))
            elif self.barSlots[i].item == "gold":
                window.blit(self.slotGoldPng, (480 + i * 32, 576))
            elif self.barSlots[i].item == "diamond":
                window.blit(self.slotDiamondPng, (480 + i * 32, 576))
            if self.barSlots[i].item != "empty":
                quantityText = self.quantityFont.render(str(self.barSlots[i].quantity), True, (255, 255, 255))
                window.blit(quantityText, (484 + i * 32, 588))

    def setSlot(self, item):
        for i in range(10):
            if self.barSlots[i].item == item and self.barSlots[i].quantity != 64:
                self.barSlots[i].quantity += 1
                break
            elif self.barSlots[i].item == "empty":
                self.barSlots[i] = Slot.Slot(item)
                self.barSlots[i].quantity += 1
                break
