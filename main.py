import pygame
import config
import Player
import Terrain
import Equipment

pygame.init()
window = pygame.display.set_mode((config.screenWidth, config.screenHeight))
pygame.display.set_caption("Minecraft2D")

player = Player.Player()
terrain = Terrain.Terrain()
equipment = Equipment.Equipment()


def update(events):
    player.move(terrain, equipment)
    equipment.changePickedSlot(events)


def draw():
    window.fill((0, 0, 0))
    terrain.draw(window, player)
    player.draw(window)
    equipment.drawBar(window)
    if player.eqOpened:
        equipment.drawEq(window)
    equipment.drawPickedSlot(window)


terrain.createTerrain()

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
