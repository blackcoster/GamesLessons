import arcade

SCREEN_TITLE = 'физека'

SPRITE_IMAGE_SIZE = 128

SPRITE_SCALING_PLAYER = 0.3
SPRITE_SCALING_TILES = 0.3

SPRITE_SIZE = int(SPRITE_IMAGE_SIZE * SPRITE_SCALING_PLAYER)

SCREEN_GRID_W = 25
SCREEN_GRID_H = 15

SCREEN_WIDTH = SPRITE_SIZE*SCREEN_GRID_W
SCREEN_HEIGHT = SPRITE_SIZE*SCREEN_GRID_H

GRAVITY = 1500

DEFAULT_DAMPING = 1.0
PLAYER_DAMPING = 0.4

PLAYER_FRICTION = 1.0
WALL_FRICTION = 0.7
DYNAMIC_ITEM_FRICTION = 0.6

PLAYER_MASS = 2.0

PLAYER_MAX_HORIZONTAL_SPEED = 200
PLAYER_MAX_VERTICAL_SPEED = 1600
PLAYER_MOVE_FORCE_ON_GROUND = 8000

class Game(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        self.player_sprite = None
        self.player_list = None
        self.wall_list = None
        self.bullet_list = None
        self.item_list = None

        self.left_pressed = False
        self.right_pressed = False
        arcade.set_background_color(arcade.color.AMAZON)

        self.physics_engine = None

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        map_name = ":resources:/tiled_maps/pymunk_test_map.json"
        tile_map = arcade.load_tilemap(map_name,SPRITE_SCALING_TILES)
        print(tile_map.sprite_lists)

        self.item_list = tile_map.sprite_lists['Dynamic Items']
        self.wall_list = tile_map.sprite_lists['Platforms']
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png",SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = SPRITE_SIZE+SPRITE_SIZE/2
        self.player_sprite.center_y = SPRITE_SIZE + SPRITE_SIZE / 2
        self.player_list.append(self.player_sprite)

        damping = DEFAULT_DAMPING
        garvity = (0,-GRAVITY)
        self.physics_engine = arcade.PymunkPhysicsEngine(damping=damping,gravity=garvity)

        self.physics_engine.add_sprite(self.player_sprite,
                                       friction=PLAYER_FRICTION,
                                       mass = PLAYER_MASS,
                                       moment=arcade.PymunkPhysicsEngine.MOMENT_INF,
                                       collision_type='player',
                                       max_horizontal_velocity=PLAYER_MAX_HORIZONTAL_SPEED,
                                       max_vertical_velocity=PLAYER_MAX_VERTICAL_SPEED)
        self.physics_engine.add_sprite_list(self.wall_list,
                                            friction=WALL_FRICTION,
                                            collision_type='wall',
                                            body_type=arcade.PymunkPhysicsEngine.STATIC)

    def on_draw(self):
        self.clear()
        self.wall_list.draw()
        self.item_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()

    def on_update(self, delta_time: float):
        if self.left_pressed and not self.right_pressed:
            force = (-PLAYER_MOVE_FORCE_ON_GROUND,0)
            self.physics_engine.apply_force(self.player_sprite,force)
            self.physics_engine.set_friction(self.player_sprite,0)
        elif self.right_pressed and not self.left_pressed:
            force = (PLAYER_MOVE_FORCE_ON_GROUND, 0)
            self.physics_engine.apply_force(self.player_sprite, force)
            self.physics_engine.set_friction(self.player_sprite, 0)
        else:
            self.physics_engine.set_friction(self.player_sprite,1.0)
        self.physics_engine.step()

    def on_key_press(self, key: int, modifiers: int):
        if key==arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key: int, modifiers: int):
        if key==arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

game = Game(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
game.setup()
arcade.run()
