import Textures
import pygame
import config
import Slot
from gui import Gui
import gui.Bar
import gui.Equipment

slot_keys = {pygame.K_1: 0, pygame.K_2: 1, pygame.K_3: 2, pygame.K_4: 3, pygame.K_5: 4, pygame.K_6: 5, pygame.K_7: 6, pygame.K_8: 7, pygame.K_9: 8, pygame.K_0: 9}


class Inventory:
    gui_handler = Gui.Gui()
    bar = gui.Bar.Bar()
    eq = gui.Equipment.Equipment()

    picked_slot = 0
    clicked_slot = None
    item_in_hand = Slot.Slot("empty")

    eq_opened = False
    crafting_opened = False

    def draw_bar(self, window):
        self.bar.draw(window, self.gui_handler)

    def draw_eq(self, window):
        self.eq.draw(window, self.gui_handler)

    # crafting nie dziala bo i tak nikt go nie zrobil to nie chce mi sie na razie naprawiac
    def draw_crafting(self, window):
        self.gui_handler.drawGrid(window, [], 40, (-14, -4, 3, 3))

    def draw_picked_slot(self, window):
        self.gui_handler.pickSlot(window, (self.bar.bb[0] // 32 + self.picked_slot, self.bar.bb[1] // 32))

    def draw_item_in_hand(self, window):
        if self.item_in_hand.item != "empty":
            pos = pygame.mouse.get_pos()
            self.gui_handler.drawTexture(window, self.item_in_hand, pos)

    def change_picked_slot(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 5:
                    self.picked_slot += 1
                    self.picked_slot %= 10
                if event.button == 4:
                    self.picked_slot -= 1
                    self.picked_slot %= 10
            elif event.type == pygame.KEYDOWN:
                if slot_keys.get(event.key, 2137) != 2137:  # basically check if event.key in dictionary
                    self.picked_slot = slot_keys[event.key]  # set slot

    def onClicked(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # creation of an array that stores all possible inventories
                    cases = [[gui.Gui.getPositionCoords(self.eq.bb), self.eq],
                             [gui.Gui.getPositionCoords(self.bar.bb), self.bar]]
                    # get the non-None value from the array (get the coords of the mouse that's inside a bounding box
                    # of an container)
                    val = next((case for case in cases if case[0] is not None), None)
                    if val is not None:
                        # get the relative coordinates in the container
                        slot = (val[0][0] - val[1].bb[0]//32, val[0][1] - val[1].bb[1]//32)
                        item = val[1].container.getItemInSlot(slot).__copy__()
                        hand = self.item_in_hand.__copy__()
                        if item.item != hand.item:
                            val[1].container.takeItem(item.quantity, slot)
                            self.item_in_hand = item
                            val[1].container.addItem(hand.item, hand.quantity, slot)
                        else:
                            val[1].container.addItem(hand.item, hand.quantity, slot)
                            self.item_in_hand = Slot.Slot("empty")

    def update(self, events):
        self.change_picked_slot(events)
        if self.eq_opened:
            self.onClicked(events)

    def draw(self, window):
        self.draw_bar(window)
        if self.eq_opened:
            self.draw_eq(window)
            self.draw_item_in_hand(window)
            self.gui_handler.drawHighlighted(window, self.eq.bb)
            self.gui_handler.drawHighlighted(window, self.bar.bb)
        # if self.crafting_opened:
        #     self.draw_crafting(window)
        self.draw_picked_slot(window)
