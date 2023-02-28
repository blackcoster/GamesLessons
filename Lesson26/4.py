import arcade
import random

def randomColor():
    a = random.randint(0,255)
    b = random.randint(0, 255)
    c = random.randint  (0, 255)
    return a,b,c

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=400,height=600,title = 'Задача 1',resizable=False)
        self.background_color =(255,255,0)
        self.set_mouse_visible(False)

    def on_draw(self):
        self.clear()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        self.background_color = randomColor()

game = Game()
arcade.run()