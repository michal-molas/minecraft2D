import config
import pygame
import Textures


class Player:
    screen_pos_x = config.screen_width
    screen_pos_y = config.screen_height

    block_x = None
    block_y = None

    position = None

    player_png = Textures.loadTxt("player", "player")

    can_jump = True
    jump_count = 44

    already_digged = False

    can_dig_left = False
    can_dig_right = False

    clicked_mouse = False

    is_falling = False

    left_wall = False
    right_wall = False

    e_pressed = False

    POS_ON_SCREEN_X = 32 * config.screen_width // 64 - 16
    POS_ON_SCREEN_Y = 32 * config.screen_height // 64

    keys_pressed = {
        "e": False,
        "a": False,
        "d": False,
        "c": False
    }

    def __init__(self, terrain):
        self.position = [terrain.world_size_x * 32 // 2 + 16, 64 * 32 + 32]
        self.block_x = self.position[0] // 32
        self.block_y = self.position[1] // 32 - 1

    def update_current_block(self):
        if self.position[0] % 32 != 0:
            self.block_x = self.position[0] // 32
        if self.position[1] % 32 != 0:
            self.block_y = self.position[1] // 32

    def clicked_block(self):
        mouse_pos = pygame.mouse.get_pos()
        dif_x = mouse_pos[0] - (self.POS_ON_SCREEN_X + 16)
        dif_y = mouse_pos[1] - (self.POS_ON_SCREEN_Y + 32)

        if not self.right_wall:
            clicked_block_x = self.block_x + (dif_x + self.position[0] % 32) // 32
        else:
            clicked_block_x = self.block_x + dif_x // 32 + 1

        if self.position[1] % 32 != 0:
            clicked_block_y = self.block_y + (dif_y + self.position[1] % 32) // 32
        else:
            clicked_block_y = self.block_y + dif_y // 32 + 1

        return clicked_block_x, clicked_block_y

    def jump(self):
        if self.jump_count > 0:
            self.jump_count -= 2
            self.position[1] -= 2

        else:
            self.is_falling = True
            self.can_jump = True
            self.jump_count = 44

    def start_fall(self, terrain):
        if self.position[1] % 32 == 0 and terrain.terrain[self.block_y + 1][self.block_x].transparent:
            self.is_falling = True

    def fall(self, terrain):
        if self.is_falling:
            self.position[1] += 2
            if self.position[1] % 32 == 0:
                self.is_falling = False
                self.start_fall(terrain)

    def dig(self, terrain, events, eq):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clicked_block = self.clicked_block()
                if clicked_block is not None:
                    rel_blocks_x = clicked_block[0] - self.block_x
                    rel_blocks_y = clicked_block[1] - self.block_y

                    if terrain.terrain[clicked_block[1]][clicked_block[0]].breakable:
                        if (rel_blocks_x == 0 and (rel_blocks_y == 1 or rel_blocks_y == -1)) \
                                or (rel_blocks_y == 0 and (rel_blocks_x == 1 or rel_blocks_x == -1)) \
                                or (rel_blocks_y == -1 and rel_blocks_x == -1
                                    and (terrain.terrain[clicked_block[1] + 1][clicked_block[0]].transparent
                                         or terrain.terrain[clicked_block[1]][clicked_block[0] + 1].transparent)) \
                                or (rel_blocks_y == -1 and rel_blocks_x == 1
                                    and (terrain.terrain[clicked_block[1] + 1][clicked_block[0]].transparent
                                         or terrain.terrain[clicked_block[1]][clicked_block[0] - 1].transparent)) \
                                or (rel_blocks_y == 1 and rel_blocks_x == -1
                                    and (terrain.terrain[clicked_block[1] - 1][clicked_block[0]].transparent
                                         or terrain.terrain[clicked_block[1]][clicked_block[0] + 1].transparent)) \
                                or (rel_blocks_y == 1 and rel_blocks_x == 1
                                    and (terrain.terrain[clicked_block[1] - 1][clicked_block[0]].transparent
                                         or terrain.terrain[clicked_block[1]][clicked_block[0] - 1].transparent)):
                            if terrain.terrain[clicked_block[1]][clicked_block[0]].collectable:
                                eq.set_slot(terrain.terrain[clicked_block[1]][clicked_block[0]].type)
                            terrain.terrain[clicked_block[1]][clicked_block[0]].change_type("sky")

    def place_block(self, terrain, events, eq):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and eq.slots[eq.picked_slot].item != "empty":
                clicked_block = self.clicked_block()
                if clicked_block is not None:

                    rel_blocks_x = clicked_block[0] - self.block_x
                    rel_blocks_y = clicked_block[1] - self.block_y

                    if terrain.terrain[clicked_block[1]][clicked_block[0]].transparent:
                        if (rel_blocks_x == 0 and (rel_blocks_y == 1 or rel_blocks_y == -1)) \
                                or (rel_blocks_y == 0 and (rel_blocks_x == 1 or rel_blocks_x == -1)) \
                                or (rel_blocks_y == -1 and rel_blocks_x == -1
                                    and (terrain.terrain[clicked_block[1] + 1][clicked_block[0]].transparent
                                         or terrain.terrain[clicked_block[1]][clicked_block[0] + 1].transparent)) \
                                or (rel_blocks_y == -1 and rel_blocks_x == 1
                                    and (terrain.terrain[clicked_block[1] + 1][clicked_block[0]].transparent
                                         or terrain.terrain[clicked_block[1]][clicked_block[0] - 1].transparent)) \
                                or (rel_blocks_y == 1 and rel_blocks_x == -1
                                    and (terrain.terrain[clicked_block[1] - 1][clicked_block[0]].transparent
                                         or terrain.terrain[clicked_block[1]][clicked_block[0] + 1].transparent)) \
                                or (rel_blocks_y == 1 and rel_blocks_x == 1
                                    and (terrain.terrain[clicked_block[1] - 1][clicked_block[0]].transparent
                                         or terrain.terrain[clicked_block[1]][clicked_block[0] - 1].transparent)):
                            terrain.terrain[clicked_block[1]][clicked_block[0]]\
                                .change_type(eq.slots[eq.picked_slot].item)
                            eq.remove_items(eq.picked_slot, 1)

    def move(self, events, terrain, eq):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.keys_pressed["a"] = True
                if event.key == pygame.K_d:
                    self.keys_pressed["d"] = True
                
                if event.key == pygame.K_w and self.can_jump and not self.is_falling:
                    if terrain.terrain[self.block_y - 1][self.block_x].transparent:
                        self.can_jump = False
                if event.key == pygame.K_e:
                    if self.keys_pressed["e"]:
                        self.keys_pressed["e"] = False
                        eq.eq_opened = False
                    else:
                        self.keys_pressed["e"] = True
                        eq.eq_opened = True
                if event.key == pygame.K_c:
                    if self.keys_pressed["c"]:
                        self.keys_pressed["c"] = False
                        eq.crafting_opened = False
                    else:
                        self.keys_pressed["c"] = True
                        eq.crafting_opened = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.keys_pressed["a"] = False
                if event.key == pygame.K_d:
                    self.keys_pressed["d"] = False
            
        if self.keys_pressed["a"]:
            if (self.position[0] % 32 != 0 or terrain.terrain[self.block_y][self.block_x - 1].transparent
                    or self.right_wall and terrain.terrain[self.block_y][self.block_x].transparent
                    and not (self.left_wall and self.keys_pressed["d"])):
                self.position[0] -= 1
            elif not self.right_wall:
                self.left_wall = True
        if self.keys_pressed["d"]:
            if (self.position[0] % 32 != 0 or terrain.terrain[self.block_y][self.block_x + 1].transparent
                    or (self.left_wall and not self.keys_pressed["a"])) \
                    and terrain.terrain[self.block_y][self.block_x].transparent:
                self.position[0] += 1
            elif not self.left_wall:
                self.right_wall = True

        if not self.can_jump:
            self.jump()

        if self.position[0] % 32 != 0:
            self.left_wall = False
            self.right_wall = False

        self.start_fall(terrain)
        self.fall(terrain)

    def update(self, events, terrain, eq):
        self.move(events, terrain, eq)
        self.update_current_block()
        self.dig(terrain, events, eq)
        self.place_block(terrain, events, eq)

    def draw(self, window):
        window.blit(self.player_png, (self.POS_ON_SCREEN_X, self.POS_ON_SCREEN_Y))
