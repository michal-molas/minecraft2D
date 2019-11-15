import Textures
import pygame
import config
import Slot
from gui import Gui
import gui.Bar
import gui.Equipment

class Equipment:
    slot_png = Textures.loadTxt("gui", "slot")
    picked_slot_png = Textures.loadTxt("gui", "pickedSlot")

    pygame.font.init()

    quantity_font = pygame.font.SysFont("arial", 32 // 2)

    gui_handler = Gui.Gui()
    bar = gui.Bar.Bar()
    eq = gui.Equipment.Equipment()

    slots = []

    picked_slot = 0
    clicked_slot = None

    already_clicked = False

    eq_opened = False
    crafting_opened = False

    def __init__(self):
        self.slots = [Slot.Slot("empty")] * 49

    def draw_bar(self, window):
        self.bar.draw(window, self.gui_handler)

    def draw_eq(self, window):
        self.eq.draw(window, self.gui_handler)

    def draw_crafting(self, window):
        self.gui_handler.drawGrid(window, self.slots, 40, 3, 3, 6, 5)

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
                    # print(last_clicked, self.clicked_slot)
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
