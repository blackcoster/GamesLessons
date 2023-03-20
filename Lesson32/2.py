import random

import arcade

SCREEN_WIDTH = 650
SCREEN_HEIGHT = 480
SCREEN_TITLE = "звуууки"


class ColumnTop(arcade.Sprite):
    def update(self):
        self.center_x -= self.change_x
        if self.center_x<=0:
            self.center_x = SCREEN_WIDTH
            self.center_y = random.randint(390,480)

class ColumnBottom(arcade.Sprite):
    def update(self):
        self.center_x -= self.change_x
        if self.center_x<=0:
            self.center_x = SCREEN_WIDTH
            self.center_y = random.randint(0,70)


class Penguin(arcade.Sprite):
    def __init__(self):
        super().__init__(filename='resources/penguin1.png', scale=1)
        self.textures.append(arcade.load_texture('resources/penguin1.png'))
        self.textures.append(arcade.load_texture('resources/penguin2.png'))
        self.textures.append(arcade.load_texture('resources/penguin3.png'))
        self.cur_texture = 0

    def update(self):
        self.center_y += self.change_y
        self.angle += self.change_angle
        self.change_y -= 0.4
        self.change_angle -= 0.4

        if self.angle >= 40:
            self.angle = 40
        if self.angle <= -40:
            self.angle = -30

        if self.center_y < 0:
            self.center_y = 0
        if self.center_y > SCREEN_HEIGHT:
            self.center_y = SCREEN_HEIGHT

    def update_animation(self, delta_time: float = 1 / 60):
        self.cur_texture += 1
        if self.cur_texture >= len(self.textures) * 5:
            self.cur_texture = 0
        self.texture = self.textures[self.cur_texture // 5]


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.background = arcade.load_texture('resources/space.png')
        self.player = None
        self.column_list = None
        self.stop = False
        self.sound_lose = None
        self.sound = None
        self.music_player = None
        self.sound_wing = None

    def setup(self):
        self.player = Penguin()
        self.player.center_x = 100
        self.player.center_y = 180
        self.player.change_y = 0
        self.player.change_angle = 0
        self.column_list = arcade.SpriteList()
        for i in range(5):
            column_top = ColumnTop("resources/column_top.png", 1)
            column_top.center_x = 130 * i + SCREEN_WIDTH
            column_top.center_y = 400
            column_top.change_x = 4
            self.column_list.append(column_top)
            column_bottom = ColumnBottom("resources/column_bottom.png", 1)
            column_bottom.center_x = 130 * i + SCREEN_WIDTH
            column_bottom.center_y = 70
            column_bottom.change_x = 4
            self.column_list.append(column_bottom)

        self.sound_lose = arcade.load_sound('resources/lose.wav',False)
        self.sound = arcade.load_sound('resources/music.mp3')
        self.music_player = arcade.play_sound(self.sound,volume=0.1,looping=True)
        self.sound_wing = arcade.load_sound('resources/sfx_wing.ogg')

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.player.draw()
        self.column_list.draw()

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.SPACE and self.stop==False:
            self.player.change_y = 5
            self.player.change_angle = 5
            arcade.play_sound(self.sound_wing)

    def on_update(self, delta_time: float):
        if self.stop==False:
            self.player.update()
            self.player.update_animation()
            self.column_list.update()
        hit_list = arcade.check_for_collision_with_list(self.player,self.column_list)
        if len(hit_list)>0:
            self.player.stop()
            for column in self.column_list:
                column.stop()
            arcade.stop_sound(self.music_player)
            arcade.play_sound(self.sound_lose,volume=0.1)
            self.stop = True



window = MyGame()
window.setup()
arcade.run()
