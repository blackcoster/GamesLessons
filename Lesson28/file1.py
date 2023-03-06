import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SPRITE_SCALING_COIN = 0.2

class Game(arcade.Window):
    def __init__(self):
        super().__init__(
            width=  SCREEN_WIDTH,
            height=SCREEN_HEIGHT,
            title = 'Работа со спрайтами',
        )
        self.coin = arcade.Sprite('coin.png',SPRITE_SCALING_COIN)
        self.coin.center_x = 64
        self.coin.center_y = 120

    def setup(self):
        pass

    def on_draw(self):
        self.clear()
        self.coin.draw()

    def update(self, delta_time: float):
        pass

if __name__=='__main__':
    game = Game()
    game.setup()
    arcade.run()