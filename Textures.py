import pygame
import os
from Blocks import *


def loadTxt(kind, name):
    txt = os.path.join("assets", kind, name + ".png")
    print(f"Adding texture: {txt}")
    return pygame.image.load(txt)


class Textures:
    textures = {}

    def addTexture(self, id, kind, name):
        self.textures.update({id: loadTxt(kind, name)})


# add block textures

for el in Blocks.blocks:
    Textures().addTexture(el, "blocks", el)
