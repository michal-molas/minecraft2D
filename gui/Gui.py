import pygame
import Textures
import config


def getRegionBoundingBox(corners):
    x_pos = corners[0]
    y_pos = corners[1]
    x_len = corners[2]
    y_len = corners[3]
    x1 = (config.screen_width + x_pos * 32) % config.screen_width
    y1 = (config.screen_height + y_pos * 32) % config.screen_height
    x2 = (config.screen_width + x_pos * 32) % config.screen_width + x_len * 32
    y2 = (config.screen_height + y_pos * 32) % config.screen_height + y_len * 32
    return x1, y1, x2, y2


def getPositionCoords(bb):
    pos = pygame.mouse.get_pos()
    # idk why but the Y-axis bounding box is translated one block up so I just translated it down manually
    if bb[0] < pos[0] < bb[2] and bb[1] < pos[1] < bb[3]:
        return pos[0] // 32, pos[1] // 32


class Gui:
    pygame.font.init()
    quantity_font = pygame.font.SysFont("arial", 32 // 2)
    dev_font = pygame.font.SysFont("Comic Sans MS", 32 // 4)
    slot_png = Textures.loadTxt("gui", "slot")
    picked_slot_png = Textures.loadTxt("gui", "pickedSlot")

    def drawGrid(self, window, slots, slot_off, corners):
        x_pos = corners[0]
        y_pos = corners[1]
        x_num = corners[2]
        y_num = corners[3]
        for y in range(y_num):
            for x in range(x_num):
                coords = ((config.screen_width + x_pos * 32) % config.screen_width + x * 32,
                          (config.screen_height + y_pos * 32) % config.screen_height + 32 * y)
                slot_nr = x_num * y + x + slot_off
                window.blit(self.slot_png, coords)
                testText = self.dev_font.render(f"{x}, {y}", True, (255, 255, 255))
                window.blit(testText, (coords[0] + 4, coords[1] + 4))
                if slots[slot_nr].item != "empty":
                    txt = pygame.transform.scale(Textures.Textures.textures[slots[slot_nr].item], (16, 16))
                    window.blit(txt, (coords[0] + 8, coords[1] + 8))
                if slots[slot_nr].item != "empty" and slots[slot_nr].quantity != 1:
                    quantityText = self.quantity_font.render(str(slots[slot_nr].quantity), True, (255, 255, 255))
                    window.blit(quantityText, (coords[0] + 5, coords[1] + 12))

    def pickSlot(self, window, slot):
        window.blit(self.picked_slot_png, (slot[0] * 32, slot[1] * 32))

    def drawHighlighted(self, window, bb):
        coords = getPositionCoords(bb)
        if coords is not None:
            self.pickSlot(window, coords)

    def drawTexture(self, window, item, pos):
        txt = pygame.transform.scale(Textures.Textures.textures[item.item], (16, 16))
        window.blit(txt, pos)
        if item.quantity > 1:
            quantityText = self.quantity_font.render(str(item.quantity), True, (255, 255, 255))
            window.blit(quantityText, (pos[0] - 3, pos[1] + 4))
