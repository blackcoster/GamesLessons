import random

import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SCREEN_TITLE = 'аНИМАЦИЯ'
GRAVITY = 1
PLAYER_MOVEMENT_SPEED = 2


class Person(arcade.AnimatedTimeBasedSprite):
    def __init__(self,sprite,scale):
        super().__init__(sprite,scale)

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
        self.bg_layer1 = arcade.load_texture('resources/bg/background.png')
        self.bg_layer2 = arcade.load_texture('resources/bg/middleground.png')
        self.ground_list = None
        self.house_list = None
        self.player = None
        self.physics_engine = None

    def setup(self):
        self.ground_list = arcade.SpriteList()
        for j in range(0,SCREEN_WIDTH+1,16):
            r_sprite = random.randint(1,2)
            ground = arcade.Sprite(f'resources/enviroments/wall-{r_sprite}.png')
            ground.center_x = j
            ground.center_y = 5
            self.ground_list.append(ground)

        self.house_list = arcade.SpriteList()
        for i in range(3):
            house = arcade.Sprite(f'resources/enviroments/house-{i}.png')
            house.center_x = 80+i*220
            if i!=1:
                house.center_y = 105
            else:
                house.center_y = 135
            self.house_list.append(house)

            self.player = Person(f'resources/person/bearded-idle/bearded-idle-1.png',1)
            self.player.center_x = 50
            self.player.bottom = self.ground_list[0].top

            self.physics_engine = arcade.PhysicsEnginePlatformer(self.player,gravity_constant=GRAVITY,walls = self.ground_list)


    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH,SCREEN_HEIGHT,self.bg_layer1)
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg_layer2)
        self.ground_list.draw()
        self.house_list.draw()
        self.player.draw()

    def on_update(self, delta_time: float):
        self.physics_engine.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.change_x = 0

game = Game()
game.setup()
arcade.run()