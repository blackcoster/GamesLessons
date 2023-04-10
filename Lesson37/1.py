import arcade

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_ENEMY = 0.5
SPRITE_SCALING_LASER = 0.8

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'ПОСЛЕДНИЙ УРОК В МОДУЛЕ'

GAME_OVER = 1
PLAY_GAME = 0

ENEMY_SPEED = 2
BULLET_SPEED = 5

MAX_PLAYER_BULLETS = 3

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

        self.gun_sound = arcade.load_sound(':resources:sounds/hurt5.wav')
        self.hit_sound = arcade.load_sound(':resources:sounds/hit5.wav')

        arcade.set_background_color(arcade.color.AMAZON)



    def setup_level_one(self):
        self.enemy_textures = []
        texture = arcade.load_texture(':resources:images/enemies/slimeBlue.png',mirrored=True)
        self.enemy_textures.append(texture)
        texture = arcade.load_texture(':resources:images/enemies/slimeBlue.png')
        self.enemy_textures.append(texture)

        x_count = 7
        x_start = 380
        x_spacing = 60
        y_count = 5
        y_start = 420
        y_spacing = 40

        for x in range(x_start,x_count*x_spacing+x_start,x_spacing):
            for y in range(y_start,y_spacing*y_count+y_start,y_spacing):
                enemy = arcade.Sprite()
                enemy.scale = SPRITE_SCALING_ENEMY
                enemy.texture = self.enemy_textures[1]
                enemy.center_x = x
                enemy.center_y = y
                self.enemy_list.append(enemy)


    def make_shield(self,x_start):
        shield_block_width = 5
        shield_block_height = 10
        shield_width_count = 20
        shield_height_count = 5

        y_start = 150

        for x in range(x_start,x_start+shield_width_count*shield_block_width,shield_block_width):
            for y in range(y_start,y_start+shield_height_count*shield_block_height):
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
        self.shield_list = arcade.SpriteList()
        self.score = 0
        self.player_sprite = arcade.Sprite(':resources:images/animated_characters/female_person/femalePerson_idle.png',
                                           SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 40
        self.player_list.append(self.player_sprite)

        for x in range(75,800,190):
            self.make_shield(x)
        arcade.set_background_color(arcade.color.AMAZON)

        self.setup_level_one()

    def on_draw(self):
        self.enemy_list.draw()
        self.player_list.draw()
        self.shield_list.draw()
        # self.player_bullet_list.draw()
        # self.enemy_bullet_list.draw()

def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()
