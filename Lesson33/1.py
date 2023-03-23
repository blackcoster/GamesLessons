import random

import  arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'OKNA'

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.25
COIN_COUNT = 50

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
        arcade.set_background_color(arcade.color.AMAZON)
        self.player_list = None
        self.player_sprite = None
        self.coin_list = None
        self.set_mouse_visible(False)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png",SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        self.coin_list = arcade.SpriteList()
        for i in range(COIN_COUNT):
            coin = arcade.Sprite(':resources:images/items/coinGold.png',SPRITE_SCALING_COIN)
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            self.coin_list.append(coin)


    def on_draw(self):
        self.clear()
        self.player_list.draw()
        self.coin_list.draw()

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_update(self, delta_time: float):
        self.coin_list.update()
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite,self.coin_list)
        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()

window = MyGame()
window.setup()
arcade.run()