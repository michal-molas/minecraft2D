import pygame
import pygame.freetype
import os, sys
import config

pygame.init()
GAME_FONT = pygame.freetype.SysFont('Arial', 24)

def draw(window, player):
    GAME_FONT.render_to(window, (config.screen_width-180, 600), f"X:{round(player.position[0]/32, 2)} Y:{round(129-player.position[1]/32, 2)}", (200, 200, 200))