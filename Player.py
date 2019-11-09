import config
import pygame


class Player:
    screen_pos_x = config.screen_width
    screen_pos_y = config.screen_height

    block_x = None
    block_y = None

    position = None

    player_png = pygame.image.load("player.png")

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

    def clicked_block(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
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
        return None

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

    def dig(self, terrain, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clicked_block = self.clicked_block(terrain, events)
                if clicked_block is not None:
                    print(clicked_block)
                    terrain.terrain[clicked_block[1]][clicked_block[0]].change_type("sky")
                '''
                # left
                if -(self.position[0] % 32) > dif_x > -(self.position[0] % 32) - 32 \
                        and ((self.position[1] % 32 != 0 and -32 - (32 - self.position[1] % 32) < dif_y < 32 -
                              self.position[1] % 32)
                             or (self.position[1] % 32 == 0 and -32 < dif_y < 0)):
                    if terrain.terrain[self.block_y][self.block_x - 1].breakable:
                        terrain.terrain[self.block_y][self.block_x - 1].change_type("sky")
                # right
                elif (((32 - self.position[0] % 32 < dif_x < 32 - self.position[0] % 32 + 32
                        and not self.right_wall)
                       or (-self.position[0] % 32 < dif_x < 32 - self.position[0] % 32 and self.right_wall))) \
                        and ((self.position[1] % 32 != 0 and -32 - (32 - self.position[1] % 32) < dif_y < 32 -
                              self.position[1] % 32)
                             or (self.position[1] % 32 == 0 and -32 < dif_y < 0)):
                    if terrain.terrain[self.block_y][self.block_x + 1].breakable:
                        terrain.terrain[self.block_y][self.block_x + 1].change_type("sky")
                # up
                elif ((self.position[1] % 32 != 0 and -(self.position[1] % 32) > dif_y > -(self.position[1] % 32) - 32)
                      or (self.position[1] % 32 == 0 and -32 > dif_y > -64)) \
                        and ((-(self.position[0] % 32) + 32 > dif_x > -(self.position[0] % 32) and not self.right_wall)
                             or (-(self.position[0] % 32) > dif_x > -(self.position[0] % 32) - 32 and self.right_wall)):
                    if terrain.terrain[self.block_y - 1][self.block_x].breakable:
                        terrain.terrain[self.block_y - 1][self.block_x].change_type("sky")
                # down
                elif (self.position[1] % 32 == 0 and 32 > dif_y > 0) \
                        and ((-(self.position[0] % 32) + 32 > dif_x > -(self.position[0] % 32) and not self.right_wall)
                             or (-(self.position[0] % 32) > dif_x > -(self.position[0] % 32) - 32 and self.right_wall)):
                    if terrain.terrain[self.block_y + 1][self.block_x].breakable:
                        terrain.terrain[self.block_y + 1][self.block_x].change_type("sky")
                '''

    def move(self, events, terrain, eq):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.keys_pressed["a"] = True
                if event.key == pygame.K_d:
                    self.keys_pressed["d"] = True
                if event.key == pygame.K_w and self.can_jump:
                    if terrain.terrain[self.block_y - 1][self.block_x].transparent:
                        self.can_jump = False
                if event.key == pygame.K_e:
                    if self.keys_pressed["e"]:
                        self.keys_pressed["e"] = False
                        eq.eq_opened = False
                    else:
                        self.keys_pressed["e"] = True
                        eq.eq_opened = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.keys_pressed["a"] = False
                if event.key == pygame.K_d:
                    self.keys_pressed["d"] = False
        if self.keys_pressed["a"]:
            if self.position[0] % 32 != 0 or terrain.terrain[self.block_y][self.block_x - 1].transparent \
                    or self.right_wall:
                self.position[0] -= 1
            else:
                self.left_wall = True
        if self.keys_pressed["d"]:
            if self.position[0] % 32 != 0 or terrain.terrain[self.block_y][self.block_x + 1].transparent \
                    or self.left_wall:
                self.position[0] += 1
            else:
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
        self.dig(terrain, events)

    def draw(self, window):
        window.blit(self.player_png, (self.POS_ON_SCREEN_X, self.POS_ON_SCREEN_Y))

    '''
    def dig_down(self, terrain, x, y, eq):
        if self.right_wall and terrain.terrain[y + 1][x - 1].breakable:
            if terrain.terrain[y + 1][x].type == "tree":
                self.cut_tree(terrain, x, y + 1, eq)
            if terrain.terrain[y + 1][x].collectable:
                eq.set_slot(terrain.terrain[y + 1][x - 1].type)
            terrain.terrain[y + 1][x - 1].change_type("sky")
        elif terrain.terrain[y + 1][x].breakable:
            if terrain.terrain[y + 1][x].type == "tree":
                self.cut_tree(terrain, x, y + 1, eq)
            if terrain.terrain[y + 1][x].collectable:
                eq.set_slot(terrain.terrain[y + 1][x].type)
            terrain.terrain[y + 1][x].change_type("sky")

    def move_left(self, terrain, x, y):
        if not self.left_wall:
            if terrain.terrain[y][x].transparent or self.right_wall:
                self.position[0] -= 1
            self.can_dig_left = False
            self.can_dig_right = False
        elif terrain.terrain[y][x - 1].breakable:
            self.can_dig_left = True

    def move_right(self, terrain, x, y):
        if not self.right_wall:
            if terrain.terrain[y][x].transparent:
                self.position[0] += 1
            self.can_dig_left = False
            self.can_dig_right = False
        elif terrain.terrain[y][x].breakable:
            self.can_dig_right = True

    def check_walls(self, terrain, x, y):
        if self.position[0] % 32 == 16:
            if not terrain.terrain[y][x - 1].transparent:
                self.left_wall = True
            else:
                self.left_wall = False
            if not terrain.terrain[y][x].transparent:
                self.right_wall = True
            else:
                self.right_wall = False
        else:
            self.left_wall = False
            self.right_wall = False

    def dig(self, terrain, x, y, eq, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                dif_x = mouse_pos[0] - 32 * config.screen_width // 64 - 16
                player_right_dist = 32 * config.screen_width // 64 - 1 - self.position[0] % 32 - 16 - 32 * config.screen_width // 64 - 16
                dif_y = 32 * config.screen_height // 64 + 16 - mouse_pos[1]
                print(player_right_dist)
                if player_right_dist < dif_x < player_right_dist - 32 and -16 < dif_y < 16:
                    terrain.terrain[y][x - 1].change_type("sky")
                elif 32 * config.screen_width // 64 + 32 < mouse_pos[0] < 32 * config.screen_width // 64 + 64 \
                        and 32 * config.screen_height // 64 < mouse_pos[1] < 32 * config.screen_height // 64 + 32:
                    # dig right
                    pass
                elif 32 * config.screen_width // 64 < mouse_pos[0] < 32 * config.screen_width // 64 + 32\
                        and 32 * config.screen_height // 64 - 32 < mouse_pos[1] < 32 * config.screen_height // 64:
                    # dig up
                    pass
                elif 32 * config.screen_width // 64 < mouse_pos[0] < 32 * config.screen_width // 64 + 32\
                        and 32 * config.screen_height // 64 + 32 < mouse_pos[1] < 32 * config.screen_height // 64 + 64:
                    # dig down
                    pass

    def dig_left_right(self, terrain, x, y, eq):
        if self.can_dig_left:
            if terrain.terrain[y][x - 1].type == "tree":
                self.cut_tree(terrain, x - 1, y, eq)
            if terrain.terrain[y][x - 1].collectable:
                eq.set_slot(terrain.terrain[y][x - 1].type)
            terrain.terrain[y][x - 1].change_type("sky")
            self.can_dig_left = False
        if self.can_dig_right:
            if terrain.terrain[y][x].type == "tree":
                self.cut_tree(terrain, x, y, eq)
            if terrain.terrain[y][x].collectable:
                eq.set_slot(terrain.terrain[y][x].type)
            terrain.terrain[y][x].change_type("sky")
            self.can_dig_right = False

    def dig_up_or_start_jump(self, terrain, x, y, eq):
        if (terrain.terrain[y - 1][x].transparent or (terrain.terrain[y - 1][x - 1].transparent and self.right_wall)) \
                and not (self.right_wall and not terrain.terrain[y - 1][x - 1].transparent
                         and terrain.terrain[y - 1][x].transparent):
            self.can_jump = False
        elif terrain.terrain[y - 1][x].breakable:
            if not self.right_wall:
                if terrain.terrain[y - 1][x].type == "tree":
                    self.cut_tree(terrain, x, y - 1, eq)
                if terrain.terrain[y - 1][x].collectable:
                    eq.set_slot(terrain.terrain[y - 1][x].type)
                terrain.terrain[y - 1][x].change_type("sky")
            else:
                if terrain.terrain[y - 1][x - 1].type == "tree":
                    self.cut_tree(terrain, x - 1, y - 1, eq)
                if terrain.terrain[y - 1][x - 1].collectable:
                    eq.set_slot(terrain.terrain[y - 1][x - 1].type)
                terrain.terrain[y - 1][x - 1].change_type("sky")

    @staticmethod
    def cut_tree(terrain, x, y, eq):
        i = 1
        while terrain.terrain[y - i][x].type == "tree":
            eq.set_slot(terrain.terrain[y - i][x].type)
            terrain.terrain[y - i][x].change_type("sky")
            i += 1
        for n in range(3):
            for m in range(3):
                terrain.terrain[y - i - n][x - 1 + m].change_type("sky")

    def move(self, terrain, eq, ev):

        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()

        player_index_y = self.position[1] // 32
        if self.position[0] % 32 < 16:
            player_index_x = self.position[0] // 32 + config.screen_width // 64
        else:
            player_index_x = self.position[0] // 32 + config.screen_width // 64 + 1

        self.check_walls(terrain, player_index_x, player_index_y)

        self.dig(terrain, player_index_x, player_index_y, eq, ev)

        if keys[pygame.K_a]:
            self.move_left(terrain, player_index_x, player_index_y)

        if keys[pygame.K_d]:
            self.move_right(terrain, player_index_x, player_index_y)

        if mouse[0]:
            self.dig_left_right(terrain, player_index_x, player_index_y, eq)

        if self.can_jump:
            self.start_fall(terrain, player_index_x, player_index_y)
            if keys[pygame.K_w] and not self.is_falling:
                self.dig_up_or_start_jump(terrain, player_index_x, player_index_y, eq)
            if keys[pygame.K_s] and not self.already_digged and not self.is_falling:
                self.dig_down(terrain, player_index_x, player_index_y, eq)
                self.already_digged = True
        else:
            self.jump()

        if not keys[pygame.K_s]:
            self.already_digged = False

        if keys[pygame.K_e]:
            if not self.e_pressed:
                if not eq.eq_opened:
                    eq.eq_opened = True
                else:
                    eq.eq_opened = False
            self.e_pressed = True

        if not keys[pygame.K_e]:
            self.e_pressed = False

        self.fall(terrain, player_index_x, player_index_y)
    '''
