import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,'Прив')
        self.x = 100
        self.y = 100
        self.radius = 30
        self.color = arcade.color.YELLOW
        self.change_x = 3
        self.change_y = 4

    def on_draw(self):
        self.clear()
        arcade.draw_circle_outline(self.x,self.y,self.radius,self.color)

    def update(self, delta_time: float):
        self.x+=self.change_x
        self.y+=self.change_y
        if self.x + self.radius > SCREEN_WIDTH or self.x - self.radius < 0:
            self.change_x = -self.change_x
        if self.y + self.radius > SCREEN_HEIGHT or self.y - self.radius < 0:
            self.change_y = -self.change_y

game = Game()
arcade.run()