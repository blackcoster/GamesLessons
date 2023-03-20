import arcade

SCREEN_WIDTH = 650
SCREEN_HEIGHT = 480
SCREEN_TITLE = "звуууки"


class ColumnTop(arcade.Sprite):
    def update(self):
        self.center_x-=self.change_x

class Penguin(arcade.Sprite):
    def __init__(self):
        super().__init__(filename='resources/penguin1.png',scale=1)
        self.textures.append(arcade.load_texture('resources/penguin1.png'))
        self.textures.append(arcade.load_texture('resources/penguin2.png'))
        self.textures.append(arcade.load_texture('resources/penguin3.png'))
        self.cur_texture = 0

    def update(self):
        self.center_y+=self.change_y
        self.angle+=self.change_angle
        self.change_y -= 0.4
        self.change_angle-=0.4
        if self.angle>=40:
            self.angle = 40
        if self.angle<=-40:
            self.angle=-30

        if self.center_y<0:
            self.center_y=0
        if self.center_y>SCREEN_HEIGHT:
            self.center_y=SCREEN_HEIGHT

    def update_animation(self, delta_time: float = 1 / 60):
        self.cur_texture+=1
        if self.cur_texture >= len(self.textures)*5:
            self.cur_texture=0
        self.texture = self.textures[self.cur_texture//5]



class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.background = arcade.load_texture('resources/space.png')
        self.player = None
        self.column_list = None

    def setup(self):
        self.player = Penguin()
        self.player.center_x = 100
        self.player.center_y = 180
        self.player.change_y = 0
        self.player.change_angle = 0
        print(self.player.textures)
        self.column_list = arcade.SpriteList()
        for i in range(5):
            column_top = ColumnTop('resources/column_top.png',1)
            column_top.center_x = 130*i + SCREEN_WIDTH
            column_top.center_y = 400
            column_top.change_x = 4
            self.column_list.append(column_top)

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT,self.background)
        self.player.draw()
    # def update(self, delta_time: float):

    def on_key_press(self, key: int, modifiers: int):
        if key==arcade.key.SPACE:
            self.player.change_y = 5
            self.player.change_angle=5

    def on_update(self, delta_time: float):
        self.player.update()
        self.player.update_animation( )
        self.column_list.update()

window = MyGame()
window.setup()
arcade.run()
