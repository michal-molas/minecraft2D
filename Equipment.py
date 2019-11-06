import config
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
    pickedSlotPng = pygame.image.load("pickedSlot.png")

    pygame.font.init()

    quantityFont = pygame.font.SysFont("arial", config.blockHeight // 2)

    barSlots = []
    pickedSlot = 0

    def __init__(self):
        for i in range(40):
            self.barSlots.append(Slot.Slot("empty"))

    def drawBar(self, window):
        for i in range(10):
            if self.barSlots[i].item == "empty":
                window.blit(self.slotPng, (config.screenWidth // 2 - 5 * config.blockWidth + i * config.blockWidth
                                           , config.screenHeight - 2 * config.blockHeight))
            elif self.barSlots[i].item == "dirt":
                window.blit(self.slotDirtPng, (config.screenWidth // 2 - 5 * config.blockWidth + i * config.blockWidth
                                               , config.screenHeight - 2 * config.blockHeight))
            elif self.barSlots[i].item == "tree":
                window.blit(self.slotTreePng, (config.screenWidth // 2 - 5 * config.blockWidth + i * config.blockWidth
                                               , config.screenHeight - 2 * config.blockHeight))
            elif self.barSlots[i].item == "stone":
                window.blit(self.slotStonePng, (config.screenWidth // 2 - 5 * config.blockWidth + i * config.blockWidth
                                                , config.screenHeight - 2 * config.blockHeight))
            elif self.barSlots[i].item == "iron":
                window.blit(self.slotIronPng, (config.screenWidth // 2 - 5 * config.blockWidth + i * config.blockWidth
                                               , config.screenHeight - 2 * config.blockHeight))
            elif self.barSlots[i].item == "gold":
                window.blit(self.slotGoldPng, (config.screenWidth // 2 - 5 * config.blockWidth + i * config.blockWidth
                                               , config.screenHeight - 2 * config.blockHeight))
            elif self.barSlots[i].item == "diamond":
                window.blit(self.slotDiamondPng,
                            (config.screenWidth // 2 - 5 * config.blockWidth + i * config.blockWidth
                             , config.screenHeight - 2 * config.blockHeight))
            if self.barSlots[i].item != "empty":
                quantityText = self.quantityFont.render(str(self.barSlots[i].quantity), True, (255, 255, 255))
                x = config.screenWidth // 2 - 5 * config.blockWidth + config.blockWidth // 5 + i * config.blockWidth
                y = config.screenHeight - 2 * config.blockHeight + config.blockHeight * 2 // 5
                window.blit(quantityText, (x, y))

    def drawEq(self, window):
        for i in range(3):
            for j in range(10):
                if self.barSlots[10 * (i + 1) + j].item == "empty":
                    window.blit(self.slotPng, (config.screenWidth // 2 - 5 * config.blockWidth + j * config.blockWidth,
                                               config.screenHeight - 7 * config.blockHeight + config.blockHeight * i))
                elif self.barSlots[10 * (i + 1) + j].item == "dirt":
                    window.blit(self.slotDirtPng, (config.screenWidth // 2 - 5 * config.blockWidth
                                                   + j * config.blockWidth,
                                                   config.screenHeight - 7 * config.blockHeight
                                                   + config.blockHeight * i))
                elif self.barSlots[10 * (i + 1) + j].item == "tree":
                    window.blit(self.slotTreePng, (config.screenWidth // 2 - 5 * config.blockWidth
                                                   + j * config.blockWidth,
                                                   config.screenHeight - 7 * config.blockHeight
                                                   + config.blockHeight * i))
                elif self.barSlots[10 * (i + 1) + j].item == "stone":
                    window.blit(self.slotStonePng, (config.screenWidth // 2 - 5 * config.blockWidth
                                                    + j * config.blockWidth,
                                                    config.screenHeight - 7 * config.blockHeight
                                                    + config.blockHeight * i))
                elif self.barSlots[10 * (i + 1) + j].item == "iron":
                    window.blit(self.slotIronPng, (config.screenWidth // 2 - 5 * config.blockWidth
                                                   + j * config.blockWidth,
                                                   config.screenHeight - 7 * config.blockHeight
                                                   + config.blockHeight * i))
                elif self.barSlots[10 * (i + 1) + j].item == "gold":
                    window.blit(self.slotGoldPng, (config.screenWidth // 2 - 5 * config.blockWidth
                                                   + j * config.blockWidth,
                                                   config.screenHeight - 7 * config.blockHeight
                                                   + config.blockHeight * i))
                elif self.barSlots[10 * (i + 1) + j].item == "diamond":
                    window.blit(self.slotDiamondPng, (config.screenWidth // 2 - 5 * config.blockWidth
                                                      + j * config.blockWidth,
                                                      config.screenHeight - 7 * config.blockHeight
                                                      + config.blockHeight * i))
                if self.barSlots[10 * (i + 1) + j].item != "empty":
                    quantityText = self.quantityFont.render(str(self.barSlots[10 * (i + 1) + j].quantity)
                                                            , True, (255, 255, 255))
                    window.blit(quantityText,
                                (config.screenWidth // 2 - 5 * config.blockWidth + config.blockWidth // 5
                                 + j * config.blockWidth, config.screenHeight - 7 * config.blockHeight
                                 + config.blockHeight * i + config.blockHeight * 2 // 5))

    def drawPickedSlot(self, window):
        window.blit(self.pickedSlotPng, (config.screenWidth // 2 - 5 * config.blockWidth
                                         + self.pickedSlot * config.blockWidth
                                         , config.screenHeight - 2 * config.blockHeight))

    def changePickedSlot(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    self.pickedSlot += 1
                    self.pickedSlot %= 10
                if event.button == 5:
                    self.pickedSlot -= 1
                    self.pickedSlot %= 10

    def setSlot(self, item):
        for i in range(40):
            if self.barSlots[i].item == item and self.barSlots[i].quantity != 64:
                self.barSlots[i].quantity += 1
                break
            elif self.barSlots[i].item == "empty":
                self.barSlots[i] = Slot.Slot(item)
                self.barSlots[i].quantity += 1
                break
