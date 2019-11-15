import pygame
import Textures
import config


class Gui:
    pygame.font.init()
    quantity_font = pygame.font.SysFont("arial", 32 // 2)
    slot_png = Textures.loadTxt("gui", "slot")
    picked_slot_png = Textures.loadTxt("gui", "pickedSlot")

    def drawGrid(self, window, slots, slot_off, x_num, y_num, x_pos, y_pos):
        for x in range(x_num):
            for y in range(y_num):
                coords = (config.screen_width // 2 + x_pos * 32 + y * 32, config.screen_height - y_pos * 32 - 32 * x)
                slot_nr = y_num * x + y + slot_off
                window.blit(self.slot_png, coords)
                if slots[slot_nr].item != "empty":
                    txt = pygame.transform.scale(Textures.Textures.textures[slots[slot_nr].item], (16, 16))
                    window.blit(txt, (coords[0] + 8, coords[1] + 8))
                if slots[slot_nr].item != "empty" and slots[slot_nr].quantity != 1:
                    quantityText = self.quantity_font.render(str(slots[slot_nr].quantity), True, (255, 255, 255))
                    window.blit(quantityText, (coords[0] + 5, coords[1] + 12))

    #def drawHighlighted(self, window):