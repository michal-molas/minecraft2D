import pygame
import config
import Player
import Terrain

pygame.init()
window = pygame.display.set_mode((config.screenWidth, config.screenHeight))
pygame.display.set_caption("Minecraft2D")

player = Player.Player()
terrain = Terrain.Terrain()


def update():
    player.move()


def draw():
    window.fill((0, 0, 0))
    terrain.draw(window, player)
    player.draw(window)


terrain.createTerrain()

run = True
while run:
    #pygame.time.delay(200)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    update()

    draw()

    pygame.display.update()

pygame.quit()
