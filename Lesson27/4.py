import arcade

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800,height=600,title='рисование фигур')
        self.background_color = (255,255,255)
        self.box = arcade.ShapeElementList()


    def setup(self):
        self.ellipse1 = arcade.create_ellipse(100, 100, 50, 60, arcade.color.BLUE)
        self.ellipse2 = arcade.create_ellipse_filled_with_colors(300, 300, 200, 250, arcade.color.RED,
                                                                 arcade.color.GREEN, tilt_angle=45)

        self.box.append(self.ellipse1)
        self.box.append(self.ellipse2)
    def on_draw(self):
        self.clear()
        self.box.draw()

game = Game()
game.setup()
arcade.run()