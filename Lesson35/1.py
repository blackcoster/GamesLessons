import arcade
from arcade.experimental.lights import LightLayer, Light

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN_TITLE = 'LIGHT'
MOVEMENT_SPEED = 5
VIEWPORT_MARGIN = 200
AMBIENT_COLOR = (10, 10, 10)


# AMBIENT_COLOR = (50,50,50)


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)

        self.background_sprite_list = None
        self.player_list = None
        self.wall_list = None
        self.player_sprite = None

        self.physics_engine = None

        self.view_left = 0
        self.view_bottom = 0
        self.light_layer = None
        self.player_light = None

    def setup(self):
        self.background_sprite_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        self.player_sprite = arcade.Sprite(':resources:images/animated_characters/female_person/femalePerson_idle.png',
                                           0.4)

        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 270
        self.player_list.append(self.player_sprite)

        for x in range(-128, 2000, 128):
            for y in range(-128, 1000, 128):
                sprite = arcade.Sprite(':resources:images/tiles/brickTextureWhite.png')
                sprite.position = x, y
                self.background_sprite_list.append(sprite)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        self.view_left = 0
        self.view_bottom = 0

        self.light_layer = LightLayer(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.light_layer.set_background_color(arcade.color.YELLOW_ROSE)

        radius = 150
        mode = 'soft'
        color = arcade.color.WHITE
        self.player_light = Light(0, 0, radius, color, mode)

        x = 100
        y = 200
        radius = 100
        mode = 'soft'
        color = arcade.color.WHITE
        light= Light(x,y, radius, color, mode)
        self.light_layer.add(light)

        x = 300
        y = 150
        radius = 200
        mode = 'soft'
        color = arcade.color.WHITE
        light = Light(x, y, radius, color, mode)
        self.light_layer.add(light)

        x = 50
        y = 450
        radius = 100
        mode = 'soft'
        color = arcade.color.RED
        light = Light(x, y, radius, color, mode)
        self.light_layer.add(light)

        x = 450
        y = 450
        radius = 100
        mode = 'soft'
        color = arcade.color.BLUE
        light = Light(x, y, radius, color, mode)
        self.light_layer.add(light)

        x = 250
        y = 450
        radius = 100
        mode = 'soft'
        color = arcade.color.GREEN
        light = Light(x, y, radius, color, mode)
        self.light_layer.add(light)

        x = 650
        y = 450
        radius = 100
        mode = 'soft'
        color = arcade.color.RED
        light = Light(x, y, radius, color, mode)
        self.light_layer.add(light)

        x = 750
        y = 450
        radius = 100
        mode = 'soft'
        color = arcade.color.GREEN
        light = Light(x, y, radius, color, mode)
        self.light_layer.add(light)

        x = 850
        y = 450
        radius = 100
        mode = 'soft'
        color = arcade.color.BLUE
        light = Light(x, y, radius, color, mode)
        self.light_layer.add(light)

        x = 650
        y = 150
        radius = 100
        mode = 'hard'
        color = arcade.color.RED
        light = Light(x, y, radius, color, mode)
        self.light_layer.add(light)

        x = 750
        y = 150
        radius = 100
        mode = 'hard'
        color = arcade.color.GREEN
        light = Light(x, y, radius, color, mode)
        self.light_layer.add(light)

        x = 850
        y = 150
        radius = 100
        mode = 'hard'
        color = arcade.color.BLUE
        light = Light(x, y, radius, color, mode)
        self.light_layer.add(light)

    def on_draw(self):
        self.clear()
        with self.light_layer:
            self.background_sprite_list.draw()
            self.player_list.draw()
        self.light_layer.draw(ambient_color=AMBIENT_COLOR)
        arcade.draw_text('НАЖМИ ПРОБЕЛ - ВКЛЮЧИШЬ/ВЫКЛЮЧИШЬ ФОНАРИК',
                         10 + self.view_left,
                         10 + self.view_bottom,
                         arcade.color.WHITE)

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.SPACE:
            if self.player_light in self.light_layer:
                self.light_layer.remove(self.player_light)
            else:
                self.light_layer.add(self.player_light)

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time: float):
        self.physics_engine.update()
        self.scroll_screen()
        self.player_light.position = self.player_sprite.position

    def on_resize(self, width: float, height: float):
        self.light_layer.resize(width, height)
        self.scroll_screen()

    def scroll_screen(self):
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left

        right_boundary = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary

        top_boundary = self.view_bottom + self.height - VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary

        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom

        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

        arcade.set_viewport(self.view_left,
                            self.view_left + self.width,
                            self.view_bottom,
                            self.view_bottom + self.height)


window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()
