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

    quantity_font = pygame.font.SysFont("arial", 32 // 2)

    slots = []
    picked_slot = 0

    clicked_slot = None
    already_clicked = False

    eq_opened = False
    crafting_opened = False

    def __init__(self):
        for i in range(49):
            self.slots.append(Slot.Slot("empty"))

    def draw_bar(self, window):
        for i in range(10):
            if self.slots[i].item == "empty":
                window.blit(self.slot_png, (config.screen_width // 2 - 5 * 32 + i * 32,
                                            config.screen_height - 2 * 32))
            elif self.slots[i].item == "dirt":
                window.blit(self.slot_dirt_png,
                            (config.screen_width // 2 - 5 * 32 + i * 32,
                             config.screen_height - 2 * 32))
            elif self.slots[i].item == "tree":
                window.blit(self.slot_tree_png,
                            (config.screen_width // 2 - 5 * 32 + i * 32,
                             config.screen_height - 2 * 32))
            elif self.slots[i].item == "stone":
                window.blit(self.slot_stone_png,
                            (config.screen_width // 2 - 5 * 32 + i * 32,
                             config.screen_height - 2 * 32))
            elif self.slots[i].item == "iron":
                window.blit(self.slot_iron_png,
                            (config.screen_width // 2 - 5 * 32 + i * 32,
                             config.screen_height - 2 * 32))
            elif self.slots[i].item == "gold":
                window.blit(self.slot_gold_png,
                            (config.screen_width // 2 - 5 * 32 + i * 32,
                             config.screen_height - 2 * 32))
            elif self.slots[i].item == "diamond":
                window.blit(self.slot_diamond_png,
                            (config.screen_width // 2 - 5 * 32 + i * 32,
                             config.screen_height - 2 * 32))
            if self.slots[i].item != "empty" and self.slots[i].quantity != 1:
                quantityText = self.quantity_font.render(str(self.slots[i].quantity), True, (255, 255, 255))
                window.blit(quantityText, (config.screen_width // 2 - 5 * 32 + 32 // 5 + i * 32,
                                           config.screen_height - 2 * 32 + 32 * 2 // 5))

    def draw_eq(self, window):
        for i in range(3):
            for j in range(10):
                if self.slots[10 * (i + 1) + j].item == "empty":
                    window.blit(self.slot_png, (config.screen_width // 2 - 5 * 32 + j * 32,
                                                config.screen_height - 7 * 32 + 32 * i))
                elif self.slots[10 * (i + 1) + j].item == "dirt":
                    window.blit(self.slot_dirt_png, (config.screen_width // 2 - 5 * 32 + j * 32,
                                                     config.screen_height - 7 * 32 + 32 * i))
                elif self.slots[10 * (i + 1) + j].item == "tree":
                    window.blit(self.slot_tree_png, (config.screen_width // 2 - 5 * 32 + j * 32,
                                                     config.screen_height - 7 * 32 + 32 * i))
                elif self.slots[10 * (i + 1) + j].item == "stone":
                    window.blit(self.slot_stone_png, (config.screen_width // 2 - 5 * 32 + j * 32,
                                                      config.screen_height - 7 * 32 + 32 * i))
                elif self.slots[10 * (i + 1) + j].item == "iron":
                    window.blit(self.slot_iron_png, (config.screen_width // 2 - 5 * 32 + j * 32,
                                                     config.screen_height - 7 * 32 + 32 * i))
                elif self.slots[10 * (i + 1) + j].item == "gold":
                    window.blit(self.slot_gold_png, (config.screen_width // 2 - 5 * 32 + j * 32,
                                                     config.screen_height - 7 * 32 + 32 * i))
                elif self.slots[10 * (i + 1) + j].item == "diamond":
                    window.blit(self.slot_diamond_png, (config.screen_width // 2 - 5 * 32 + j * 32,
                                                        config.screen_height - 7 * 32 + 32 * i))
                if self.slots[10 * (i + 1) + j].item != "empty" and self.slots[10 * (i + 1) + j].quantity != 1:
                    quantityText = self.quantity_font.render(str(self.slots[10 * (i + 1) + j].quantity),
                                                             True, (255, 255, 255))
                    window.blit(quantityText, (config.screen_width // 2 - 5 * 32 + 32 // 5 + j * 32,
                                               config.screen_height - 7 * 32 + 32 * i + 32 * 2 // 5))

    def draw_crafting(self, window):
        for i in range(40, 49):
            if self.slots[i].item == "empty":
                window.blit(self.slot_png, (config.screen_width // 2 + 7 * 32 + ((i - 40) % 3) * 32,
                                            config.screen_height - 7 * 32 + ((i - 40) // 3) * 32))
            elif self.slots[i].item == "dirt":
                window.blit(self.slot_dirt_png, (config.screen_width // 2 + 7 * 32 + ((i - 40) % 3) * 32,
                                                 config.screen_height - 7 * 32 + ((i - 40) // 3) * 32))
            elif self.slots[i].item == "tree":
                window.blit(self.slot_tree_png, (config.screen_width // 2 + 7 * 32 + ((i - 40) % 3) * 32,
                                                 config.screen_height - 7 * 32 + ((i - 40) // 3) * 32))
            elif self.slots[i].item == "stone":
                window.blit(self.slot_stone_png, (config.screen_width // 2 + 7 * 32 + ((i - 40) % 3) * 32,
                                                  config.screen_height - 7 * 32 + ((i - 40) // 3) * 32))
            elif self.slots[i].item == "iron":
                window.blit(self.slot_iron_png, (config.screen_width // 2 + 7 * 32 + ((i - 40) % 3) * 32,
                                                 config.screen_height - 7 * 32 + ((i - 40) // 3) * 32))
            elif self.slots[i].item == "gold":
                window.blit(self.slot_gold_png, (config.screen_width // 2 + 7 * 32 + ((i - 40) % 3) * 32,
                                                 config.screen_height - 7 * 32 + ((i - 40) // 3) * 32))
            elif self.slots[i].item == "diamond":
                window.blit(self.slot_diamond_png, (config.screen_width // 2 + 7 * 32 + ((i - 40) % 3) * 32,
                                                    config.screen_height - 7 * 32 + ((i - 40) // 3) * 32))
            if self.slots[i].item != "empty" and self.slots[i].quantity != 1:
                quantityText = self.quantity_font.render(str(self.slots[i].quantity),
                                                         True, (255, 255, 255))
                window.blit(quantityText, (config.screen_width // 2 + 7 * 32 + ((i - 40) % 3) * 32 + 32 // 5,
                                           config.screen_height - 7 * 32 + ((i - 40) // 3) * 32 + 32 * 2 // 5))

    def draw_picked_slot(self, window):
        window.blit(self.picked_slot_png, (config.screen_width // 2 - 5 * 32
                                           + self.picked_slot * 32,
                                           config.screen_height - 2 * 32))

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
            if self.slots[i].item == item and self.slots[i].quantity < 64:
                self.slots[i].quantity += 1
                return
        for i in range(40):
            if self.slots[i].item == "empty":
                self.slots[i] = Slot.Slot(item)
                self.slots[i].quantity += 1
                return

    def remove_items(self, slot_index, qu):
        self.slots[slot_index].quantity -= qu
        if self.slots[slot_index].quantity <= 0:
            self.slots[slot_index].item = "empty"
            self.slots[slot_index].quantity = 0

    def draw_clicked_slot(self, window):
        if self.clicked_slot is not None:
            if 0 <= self.clicked_slot < 10:
                window.blit(self.picked_slot_png, (config.screen_width // 2 - 5 * 32 + self.clicked_slot % 10 * 32,
                                                   config.screen_height - 2 * 32))
            elif 10 <= self.clicked_slot < 40 and self.eq_opened:
                window.blit(self.picked_slot_png, (config.screen_width // 2 - 5 * 32 + self.clicked_slot % 10 * 32,
                                                   config.screen_height - 8 * 32 + self.clicked_slot // 10 * 32))
            elif 40 <= self.clicked_slot < 49 and self.crafting_opened:
                window.blit(self.picked_slot_png, (config.screen_width // 2 + 7 * 32
                                                   + ((self.clicked_slot - 40) % 3) * 32,
                                                   config.screen_height - 7 * 32
                                                   + ((self.clicked_slot - 40) // 3) * 32))

    # 0 - 9 - bar
    # 10 - 39 - eq
    # 40 - 48 - crafting

    def click_slot(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    last_clicked = self.clicked_slot
                    for i in range(49):
                        if i < 10:
                            if config.screen_width // 2 - 5 * 32 + i * 32 < mouse_pos[0] < \
                                    config.screen_width // 2 - 4 * 32 + i * 32 \
                                    and config.screen_height - 2 * 32 < mouse_pos[1] < config.screen_height - 32:
                                self.clicked_slot = i
                        elif i < 40 and self.eq_opened:
                            if config.screen_width // 2 - 5 * 32 + (i % 10) * 32 < mouse_pos[0] < \
                                    config.screen_width // 2 - 4 * 32 + (i % 10) * 32 \
                                    and config.screen_height - 8 * 32 + (i // 10) * 32 < mouse_pos[1] < \
                                    config.screen_height - 7 * 32 + (i // 10) * 32:
                                self.clicked_slot = i
                        elif i < 49 and self.crafting_opened:
                            if config.screen_width // 2 + 7 * 32 + ((i - 40) % 3) * 32 < mouse_pos[0] < \
                                    config.screen_width // 2 + 8 * 32 + ((i - 40) % 3) * 32 \
                                    and config.screen_height - 7 * 32 + ((i - 40) // 3) * 32 < mouse_pos[1] < \
                                    config.screen_height - 6 * 32 + ((i - 40) // 3) * 32:
                                self.clicked_slot = i
                    if last_clicked is not None:
                        if self.slots[last_clicked].item != "empty":
                            if last_clicked != self.clicked_slot:
                                if self.slots[last_clicked].item != self.slots[self.clicked_slot].item:
                                    temp = self.slots[last_clicked]
                                    self.slots[last_clicked] = self.slots[self.clicked_slot]
                                    self.slots[self.clicked_slot] = temp
                                    self.clicked_slot = None
                                else:
                                    self.slots[self.clicked_slot].quantity = self.slots[self.clicked_slot].quantity \
                                                                             + self.slots[last_clicked].quantity
                                    self.slots[last_clicked] = Slot.Slot("empty")
                                    if self.slots[self.clicked_slot].quantity > 64:
                                        for i in range(self.slots[self.clicked_slot].quantity - 64):
                                            self.set_slot(self.slots[self.clicked_slot].item)
                                        self.slots[self.clicked_slot].quantity = 64
                                    self.clicked_slot = None
                            else:
                                self.clicked_slot = None
                        else:
                            self.clicked_slot = None

    def update(self, events):
        self.change_picked_slot(events)
        self.click_slot(events)

    def draw(self, window):
        self.draw_bar(window)
        if self.eq_opened:
            self.draw_eq(window)
        if self.crafting_opened:
            self.draw_crafting(window)
        self.draw_picked_slot(window)
        self.draw_clicked_slot(window)
