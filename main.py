import pygame
import config
import Player
import Terrain
import Equipment
import showcoords

pygame.init()
window = pygame.display.set_mode((config.screen_width, config.screen_height))
pygame.display.set_caption("Minecraft2D")

terrain = Terrain.Terrain()
player = Player.Player(terrain)
equipment = Equipment.Equipment()

def update(ev):
    player.update(ev, terrain, equipment)
    equipment.update(ev)


def draw():
    window.fill((0, 0, 0))
    terrain.draw(window, player)
    player.draw(window)
    equipment.draw(window)
    showcoords.draw(window, player)

terrain.create_terrain()

run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False

    update(events)

    draw()

    pygame.display.update()

pygame.quit()