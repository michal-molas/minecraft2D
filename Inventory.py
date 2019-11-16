import Textures
import pygame
import config
import Slot
from gui import Gui
import gui.Bar
import gui.Equipment


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

    def change_picked_slot(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    self.picked_slot -= 1
                    self.picked_slot %= 10
                if event.button == 5:
                    self.picked_slot += 1
                    self.picked_slot %= 10

    def onClicked(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    eq_coords = gui.Gui.getPositionCoords(self.eq.bb)
                    bar_coords = gui.Gui.getPositionCoords(self.bar.bb)
                    if eq_coords is not None:
                        slot = (eq_coords[0] - self.eq.bb[0] // 32, eq_coords[1] - self.eq.bb[3] // 32 - 1)
                        print(slot)
                        item = self.eq.container.getItemInSlot(slot).__copy__()
                        self.eq.container.takeItem(item.quantity, slot)
                        hand = self.item_in_hand.__copy__()
                        self.item_in_hand = item
                        self.eq.container.addItem(hand.item, hand.quantity, slot)
                    if bar_coords is not None:
                        # that code is not perfect I know it has to be written in better way
                        # TODO: CHANGE THIS TO SOMETHING MORE READABLE
                        slot = (bar_coords[0] - self.bar.bb[0] // 32, bar_coords[1] - self.bar.bb[3] // 32 - 1)
                        print(slot)
                        item = self.bar.container.getItemInSlot(slot).__copy__()
                        self.bar.container.takeItem(item.quantity, slot)
                        hand = self.item_in_hand.__copy__()
                        self.item_in_hand = item
                        self.bar.container.addItem(hand.item, hand.quantity, slot)

    def update(self, events):
        self.change_picked_slot(events)
        if self.eq_opened:
            self.onClicked(events)

    def draw(self, window):
        self.draw_bar(window)
        if self.eq_opened:
            self.draw_eq(window)
            self.gui_handler.drawHighlighted(window, self.eq.bb)
            self.gui_handler.drawHighlighted(window, self.bar.bb)
        # if self.crafting_opened:
        #     self.draw_crafting(window)
        self.draw_picked_slot(window)
