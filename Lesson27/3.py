import arcade

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800,height=600,title='рисование фигур')
        self.background_color = (255,255,255)
        self.tex = arcade.load_texture('the_teacher.jpg')
        # self.tex = arcade.load_texture(':resources:images/animated_characters/zombie/zombie_jump.png')
    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(
            center_x=100,
            center_y=200,
            width=100,
            height=90,
            texture=self.tex
        )

game = Game()
arcade.run()