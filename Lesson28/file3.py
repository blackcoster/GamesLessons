import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CHARACTER_SCALE = 1
TILE_SCALING = 0.5


class Game(arcade.Window):
    def __init__(self):
        super().__init__(
            width=SCREEN_WIDTH,
            height=SCREEN_HEIGHT,
            title='Работа со спрайтами',
        )
        self.player_sprite = None
        self.scene = None

    def setup(self):

        self.scene = arcade.Scene()
        self.scene.add_sprite_list('Player')
        self.scene.add_sprite_list('Wall', use_spatial_hash=True)


        image_source = ':resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png'
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALE)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.scene.add_sprite('Player',self.player_sprite)


        for x in range(0, 800, 64):
            self.ground = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
            self.ground.center_x = x
            self.ground.center_y = 32
            self.scene.add_sprite('Wall',self.ground)

        coordinate_list = [[512, 96], [256, 96], [768, 96]]

        for coordinate in coordinate_list:
            self.box = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", TILE_SCALING)
            self.box.position = coordinate
            self.scene.add_sprite('Wall',self.box)

    def on_draw(self):
        self.clear()
        self.scene.draw()

    def update(self, delta_time: float):
        pass


if __name__ == '__main__':
    game = Game()
    game.setup()
    arcade.run()