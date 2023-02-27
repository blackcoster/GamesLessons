import random
import arcade


def get_random_color():
   return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


class Game(arcade.Window):
   def __init__(self):
       super().__init__(width=400, height=600, title='Задача 1', resizable=False)
       self.background_color = (255, 255, 0)
       self.set_mouse_visible(False)

   def on_draw(self):
       self.clear()

   def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
       self.background_color = get_random_color()



if __name__ == '__main__':
   game = Game()
   arcade.run()




