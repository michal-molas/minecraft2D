import config
import pygame
import Slot


class Equipment:
    slot_png = pygame.image.load("slot.png")
    slot_dirt_png = pygame.image.load("slotDirt.png")
    slot_stone_png = pygame.image.load("slotStone.png")
    slot_tree_png = pygame.image.load("slotTree.png")
    slot_iron_png = pygame.image.load("slotIron.png")
    slot_gold_png = pygame.image.load("slotGold.png")
    slot_diamond_png = pygame.image.load("slotDiamond.png")
    picked_slot_png = pygame.image.load("pickedSlot.png")

    pygame.font.init()

    quantity_font = pygame.font.SysFont("arial", config.block_height // 2)

    slots = []
    picked_slot = 0

    def __init__(self):
        for i in range(40):
            self.slots.append(Slot.Slot("empty"))

    def draw_bar(self, window):
        for i in range(10):
            if self.slots[i].item == "empty":
                window.blit(self.slot_png, (config.screen_width // 2 - 5 * config.block_width + i * config.block_width,
                                            config.screen_height - 2 * config.block_height))
            elif self.slots[i].item == "dirt":
                window.blit(self.slot_dirt_png,
                            (config.screen_width // 2 - 5 * config.block_width + i * config.block_width,
                             config.screen_height - 2 * config.block_height))
            elif self.slots[i].item == "tree":
                window.blit(self.slot_tree_png,
                            (config.screen_width // 2 - 5 * config.block_width + i * config.block_width,
                             config.screen_height - 2 * config.block_height))
            elif self.slots[i].item == "stone":
                window.blit(self.slot_stone_png,
                            (config.screen_width // 2 - 5 * config.block_width + i * config.block_width,
                             config.screen_height - 2 * config.block_height))
            elif self.slots[i].item == "iron":
                window.blit(self.slot_iron_png,
                            (config.screen_width // 2 - 5 * config.block_width + i * config.block_width,
                             config.screen_height - 2 * config.block_height))
            elif self.slots[i].item == "gold":
                window.blit(self.slot_gold_png,
                            (config.screen_width // 2 - 5 * config.block_width + i * config.block_width,
                             config.screen_height - 2 * config.block_height))
            elif self.slots[i].item == "diamond":
                window.blit(self.slot_diamond_png,
                            (config.screen_width // 2 - 5 * config.block_width + i * config.block_width,
                             config.screen_height - 2 * config.block_height))
            if self.slots[i].item != "empty":
                quantityText = self.quantity_font.render(str(self.slots[i].quantity), True, (255, 255, 255))
                x = config.screen_width // 2 - 5 * config.block_width + config.block_width // 5 + i * config.block_width
                y = config.screen_height - 2 * config.block_height + config.block_height * 2 // 5
                window.blit(quantityText, (x, y))

    def draw_eq(self, window):
        for i in range(3):
            for j in range(10):
                if self.slots[10 * (i + 1) + j].item == "empty":
                    window.blit(self.slot_png, (config.screen_width // 2 - 5 * config.block_width
                                                + j * config.block_width,
                                                config.screen_height - 7 * config.block_height
                                                + config.block_height * i))
                elif self.slots[10 * (i + 1) + j].item == "dirt":
                    window.blit(self.slot_dirt_png, (config.screen_width // 2 - 5 * config.block_width
                                                     + j * config.block_width,
                                                     config.screen_height - 7 * config.block_height
                                                     + config.block_height * i))
                elif self.slots[10 * (i + 1) + j].item == "tree":
                    window.blit(self.slot_tree_png, (config.screen_width // 2 - 5 * config.block_width
                                                     + j * config.block_width,
                                                     config.screen_height - 7 * config.block_height
                                                     + config.block_height * i))
                elif self.slots[10 * (i + 1) + j].item == "stone":
                    window.blit(self.slot_stone_png, (config.screen_width // 2 - 5 * config.block_width
                                                      + j * config.block_width,
                                                      config.screen_height - 7 * config.block_height
                                                      + config.block_height * i))
                elif self.slots[10 * (i + 1) + j].item == "iron":
                    window.blit(self.slot_iron_png, (config.screen_width // 2 - 5 * config.block_width
                                                     + j * config.block_width,
                                                     config.screen_height - 7 * config.block_height
                                                     + config.block_height * i))
                elif self.slots[10 * (i + 1) + j].item == "gold":
                    window.blit(self.slot_gold_png, (config.screen_width // 2 - 5 * config.block_width
                                                     + j * config.block_width,
                                                     config.screen_height - 7 * config.block_height
                                                     + config.block_height * i))
                elif self.slots[10 * (i + 1) + j].item == "diamond":
                    window.blit(self.slot_diamond_png, (config.screen_width // 2 - 5 * config.block_width
                                                        + j * config.block_width,
                                                        config.screen_height - 7 * config.block_height
                                                        + config.block_height * i))
                if self.slots[10 * (i + 1) + j].item != "empty":
                    quantityText = self.quantity_font.render(str(self.slots[10 * (i + 1) + j].quantity),
                                                             True, (255, 255, 255))
                    window.blit(quantityText,
                                (config.screen_width // 2 - 5 * config.block_width + config.block_width // 5
                                 + j * config.block_width, config.screen_height - 7 * config.block_height
                                 + config.block_height * i + config.block_height * 2 // 5))

    def draw_picked_slot(self, window):
        window.blit(self.picked_slot_png, (config.screen_width // 2 - 5 * config.block_width
                                           + self.picked_slot * config.block_width,
                                           config.screen_height - 2 * config.block_height))

    def change_picked_slot(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    self.picked_slot += 1
                    self.picked_slot %= 10
                if event.button == 5:
                    self.picked_slot -= 1
                    self.picked_slot %= 10

    def set_slot(self, item):
        for i in range(40):
            if self.slots[i].item == item and self.slots[i].quantity != 64:
                self.slots[i].quantity += 1
                break
            elif self.slots[i].item == "empty":
                self.slots[i] = Slot.Slot(item)
                self.slots[i].quantity += 1
                break
