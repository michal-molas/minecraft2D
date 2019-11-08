import config
import pygame


class Player:
    screen_pos_x = config.screen_width
    screen_pos_y = config.screen_height

    position = [0, 0]

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

    def jump(self):
        if self.jump_count > 0:
            self.jump_count -= 2
            self.position[1] += 2
        else:
            self.is_falling = True
            self.can_jump = True
            self.jump_count = 44

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

    def start_fall(self, terrain, x, y):
        if (self.position[1] % 32 == 0 and
                (terrain.terrain[y + 1][x].transparent
                 or (terrain.terrain[y + 1][x - 1].transparent and self.right_wall))):
            self.is_falling = True

    def fall(self, terrain, x, y):
        if self.is_falling:
            self.position[1] -= 2
            if self.position[1] % 32 == 0:
                self.is_falling = False
                self.start_fall(terrain, x, y)

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

    def move(self, terrain, eq):

        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()

        player_index_y = 64 - self.position[1] // 32
        if self.position[0] % 32 < 16:
            player_index_x = terrain.world_size_x // 2 + self.position[0] // 32 + config.screen_width // 64
        else:
            player_index_x = terrain.world_size_x // 2 + self.position[0] // 32 + config.screen_width // 64 + 1

        self.check_walls(terrain, player_index_x, player_index_y)

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

    def draw(self, window):
        window.blit(self.player_png, (32 * config.screen_width // 64, 32 * config.screen_height // 64))
