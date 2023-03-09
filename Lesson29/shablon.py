import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Шутер"

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)

    def setup(self):
        pass

    def on_draw(self):
        self.clear()

game = Game()
game.setup()
arcade.run()
