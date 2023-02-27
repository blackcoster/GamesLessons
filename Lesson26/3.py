import arcade

class Game(arcade.Window):
    def __init__(self):
        super().__init__()
        self.height = 300
        self.width = 400
        self.set_caption('Моя игра')
        arcade.set_background_color(arcade.color.AO)

    def on_draw(self):
       self.clear()

if __name__ == '__main__':
   game = Game()
   arcade.run()

