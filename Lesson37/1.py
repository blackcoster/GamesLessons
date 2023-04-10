import random
import arcade

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_enemy = 0.5
SPRITE_SCALING_LASER = 0.8

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Slime Invaders"

BULLET_SPEED = 5
ENEMY_SPEED = 2

MAX_PLAYER_BULLETS = 3
ENEMY_VERTICAL_MARGIN = 15
RIGHT_ENEMY_BORDER = SCREEN_WIDTH - ENEMY_VERTICAL_MARGIN
LEFT_ENEMY_BORDER = ENEMY_VERTICAL_MARGIN
ENEMY_MOVE_DOWN_AMOUNT = 30

GAME_OVER = 1
PLAY_GAME = 0


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.player_list = None
        self.enemy_list = None
        self.player_bullet_list = None
        self.enemy_bullet_list = None
        self.shield_list = None
        self.enemy_textures = None
        self.game_state = PLAY_GAME
        self.player_sprite = None
        self.score = 0

        self.enemy_change_x = -ENEMY_SPEED

        self.set_mouse_visible(False)

        self.gun_sound = arcade.load_sound(":resources:sounds/hurt5.wav")
        self.hit_sound = arcade.load_sound(":resources:sounds/hit5.wav")

        arcade.set_background_color(arcade.color.AMAZON)

    def setup_level_one(self):
        self.enemy_textures = []
        texture = arcade.load_texture(":resources:images/enemies/slimeBlue.png", mirrored=True)
        self.enemy_textures.append(texture)
        texture = arcade.load_texture(":resources:images/enemies/slimeBlue.png")
        self.enemy_textures.append(texture)

        x_count = 7
        x_start = 380
        x_spacing = 60
        y_count = 5
        y_start = 420
        y_spacing = 40

        for x in range(x_start, x_spacing * x_count + x_start, x_spacing):
            for y in range(y_start, y_spacing * y_count + y_start, y_spacing):
                enemy = arcade.Sprite()
                enemy.scale = SPRITE_SCALING_enemy
                enemy.texture = self.enemy_textures[1]
                enemy.center_x = x
                enemy.center_y = y
                self.enemy_list.append(enemy)

    def make_shield(self, x_start):
        shield_block_width = 5
        shield_block_height = 10
        shield_width_count = 20
        shield_height_count = 5
        y_start = 150
        for x in range(x_start,
                       x_start + shield_width_count * shield_block_width,
                       shield_block_width):
            for y in range(y_start,
                           y_start + shield_height_count * shield_block_height,
                           shield_block_height):
                shield_sprite = arcade.SpriteSolidColor(shield_block_width,
                                                        shield_block_height,
                                                        arcade.color.WHITE)
                shield_sprite.center_x = x
                shield_sprite.center_y = y
                self.shield_list.append(shield_sprite)
    def setup(self):
        self.game_state = PLAY_GAME
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.player_bullet_list = arcade.SpriteList()
        self.enemy_bullet_list = arcade.SpriteList()
        self.shield_list = arcade.SpriteList(is_static=True)
        self.score = 0
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/"
                                           "femalePerson_idle.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 40
        self.player_list.append(self.player_sprite)
        for x in range(75, 800, 190):
            self.make_shield(x)
        arcade.set_background_color(arcade.color.AMAZON)

        self.setup_level_one()

    def on_draw(self):
        self.clear()

        self.enemy_list.draw()
        self.player_bullet_list.draw()
        self.enemy_bullet_list.draw()
        self.shield_list.draw()
        self.player_list.draw()

        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14)

        if self.game_state == GAME_OVER:
            arcade.draw_text("GAME OVER", 250, 300, arcade.color.WHITE, 55)
            self.set_mouse_visible(True)

    def on_mouse_motion(self, x, y, dx, dy):
        if self.game_state == GAME_OVER:
            return

        self.player_sprite.center_x = x

    def on_mouse_press(self, x, y, button, modifiers):
        if len(self.player_bullet_list) < MAX_PLAYER_BULLETS:
            arcade.play_sound(self.gun_sound)
            bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png", SPRITE_SCALING_LASER)
            bullet.angle = 90
            bullet.change_y = BULLET_SPEED
            bullet.center_x = self.player_sprite.center_x
            bullet.bottom = self.player_sprite.top
            self.player_bullet_list.append(bullet)

    def update_enemies(self):
        for enemy in self.enemy_list:
            enemy.center_x += self.enemy_change_x

        move_down = False
        for enemy in self.enemy_list:
            if enemy.right > RIGHT_ENEMY_BORDER and self.enemy_change_x > 0:
                self.enemy_change_x *= -1
                move_down = True
            if enemy.left < LEFT_ENEMY_BORDER and self.enemy_change_x < 0:
                self.enemy_change_x *= -1
                move_down = True

        if move_down:
            for enemy in self.enemy_list:
                enemy.center_y -= ENEMY_MOVE_DOWN_AMOUNT
                if self.enemy_change_x > 0:
                    enemy.texture = self.enemy_textures[0]
                else:
                    enemy.texture = self.enemy_textures[1]

    def allow_enemies_to_fire(self):
        x_spawn = []
        for enemy in self.enemy_list:
            chance = 4 + len(self.enemy_list) * 4
            if random.randrange(chance) == 0 and enemy.center_x not in x_spawn:
                bullet = arcade.Sprite(":resources:images/space_shooter/laserRed01.png", SPRITE_SCALING_LASER)
                bullet.angle = 180
                bullet.change_y = -BULLET_SPEED
                bullet.center_x = enemy.center_x
                bullet.top = enemy.bottom
                self.enemy_bullet_list.append(bullet)
            x_spawn.append(enemy.center_x)

    def process_enemy_bullets(self):
        self.enemy_bullet_list.update()

        for bullet in self.enemy_bullet_list:
            hit_list = arcade.check_for_collision_with_list(bullet, self.shield_list)

            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
                for shield in hit_list:
                    shield.remove_from_sprite_lists()
                continue
            if arcade.check_for_collision_with_list(self.player_sprite, self.enemy_bullet_list):
                self.game_state = GAME_OVER
            if bullet.top < 0:
                bullet.remove_from_sprite_lists()

    def process_player_bullets(self):
        self.player_bullet_list.update()
        for bullet in self.player_bullet_list:

            hit_list = arcade.check_for_collision_with_list(bullet, self.shield_list)
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
                for shield in hit_list:
                    shield.remove_from_sprite_lists()
                continue

            hit_list = arcade.check_for_collision_with_list(bullet, self.enemy_list)

            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()

            for enemy in hit_list:
                enemy.remove_from_sprite_lists()
                self.score += 1

                arcade.play_sound(self.hit_sound)
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()

    def on_update(self, delta_time):
        if self.game_state == GAME_OVER:
            return

        self.update_enemies()
        self.allow_enemies_to_fire()
        self.process_enemy_bullets()
        self.process_player_bullets()

        if len(self.enemy_list) == 0:
            self.setup_level_one()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
