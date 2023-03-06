import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CHARACTER_SCALE = 1
TILE_SCALING = 0.5
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 2
PLAYER_JUMP_SPEED = 20

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__(
            ':resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png',
            CHARACTER_SCALE,
        )
        self.center_x = 64
        self.center_y = 128
    def update(self):
        self.center_x+=self.change_x
        self.center_y += self.change_y
        self.center_y-=GRAVITY
        if self.center_y<=128:
            self.center_y=128
            game.isGround = True


class Box(arcade.Sprite):
    def __init__(self):
        super().__init__(
            ":resources:images/tiles/boxCrate_double.png",
            TILE_SCALING,
        )
        self.position = [512, 96]
        self.change_y = 2

    def update(self):
        self.center_y+=self.change_y
        if self.top>=500:
            self.change_y = -self.change_y
        elif self.bottom<=64:
            self.change_y = -self.change_y

class Game(arcade.Window):
    def __init__(self):
        super().__init__(
            width=SCREEN_WIDTH,
            height=SCREEN_HEIGHT,
            title='Работа со спрайтами',
        )
        self.player_sprite = None
        self.scene = None
        self.isGround = True

    def setup(self):

        self.scene = arcade.Scene()
        self.scene.add_sprite_list('Player')
        self.scene.add_sprite_list('Wall')


        self.player_sprite = Player()
        self.scene.add_sprite('Player',self.player_sprite)


        for x in range(0, 800, 64):
            self.ground = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
            self.ground.center_x = x
            self.ground.center_y = 32
            self.scene.add_sprite('Wall',self.ground)

        self.box = Box()

        self.scene.add_sprite('Wall',self.box)

    def on_draw(self):
        self.clear()
        self.scene.draw()

    def update(self, delta_time: float):
        self.player_sprite.update()
        self.box.update()

    def on_key_press(self, key: int, modifiers: int):
        if self.isGround==1:
            if key == arcade.key.UP:
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
                self.isGround = False

        if key==arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key==arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


if __name__ == '__main__':
    game = Game()
    game.setup()
    arcade.run()