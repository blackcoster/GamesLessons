import arcade

SCREEN_WIDTH = 1000
SCREEN_HIGHT = 650
SCREEN_TITLE = 'простой платформер'

CHARACTER_SCALING = 1
TILE_SCALING = 0.5
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 20

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH,SCREEN_HIGHT,SCREEN_TITLE)
        arcade.set_background_color(arcade.csscolor.AQUA)
        self.scene = None
        self.player_sprite = None
        self.physics_engine = None
        self.camera = None
        self.enemy = None
        self.player_exit = None

    def setup(self):
        self.scene = arcade.Scene()
        self.scene.add_sprite_list('Player')
        self.scene.add_sprite_list('Wall',use_spatial_hash=True)

        image_source = ":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png"
        self.player_sprite = arcade.Sprite(image_source,CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.scene.add_sprite('Player',self.player_sprite)

        for x in range(0,1250,64):
            wall = arcade.Sprite(":resources:images/tiles/dirtMid.png", TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.scene.add_sprite('Wall',wall)

        coordinate_list = [[512, 96], [256, 96], [768, 96]]

        for coordinate in coordinate_list:
            wall = arcade.Sprite(
                ":resources:images/tiles/boxCrate_double.png", TILE_SCALING
            )

            wall.position = coordinate
            self.scene.add_sprite("Wall", wall)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,gravity_constant=GRAVITY,walls=self.scene.get_sprite_list('Wall'))

        self.camera = arcade.Camera(self.width,self.height)

        enemy_sprite = ":resources:images/animated_characters/zombie/zombie_idle.png"
        self.enemy = arcade.Sprite(enemy_sprite, CHARACTER_SCALING)
        self.enemy.center_x = 400
        self.enemy.center_y = 128
        self.scene.add_sprite("Enemy", self.enemy)

        exit_sprite = ":resources:images/tiles/signExit.png"
        self.exit_player = arcade.Sprite(exit_sprite, CHARACTER_SCALING)
        self.exit_player.center_x = 1200
        self.exit_player.center_y = 128
        self.scene.add_sprite("Exit", self.exit_player)

    def on_draw(self):
        self.clear()
        self.scene.draw()
        self.camera.use()

    def on_key_press(self, key: int, modifiers: int):
        if key==arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
        elif key==arcade.key.DOWN:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key==arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
        elif key==arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key: int, modifiers: int):
        # if key==arcade.key.UP:
        #     self.player_sprite.change_y = 0
        if key==arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key==arcade.key.RIGHT:
            self.player_sprite.change_x = 0
        elif key==arcade.key.LEFT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        self.physics_engine.update()
        self.center_camera_to_player()
        if arcade.check_for_collision(self.player_sprite, self.enemy):
            self.player_sprite.kill()
            arcade.close_window()
            print('Вы проиграли')
        if arcade.check_for_collision(self.player_sprite, self.exit_player):
            arcade.close_window()
            print('Вы победили')

    def center_camera_to_player(self):
        screen_center_x = self.player_sprite.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player_sprite.center_y - (self.camera.viewport_height / 2)
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y
        self.camera.move_to(player_centered)


game = Game()
game.setup()
arcade.run()
