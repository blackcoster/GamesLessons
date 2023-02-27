import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"

class MyGame(arcade.Window):
   def __init__(self):
       super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

       arcade.set_background_color(arcade.csscolor.BURLYWOOD)

   def setup(self):
       pass

   def on_draw(self):
       self.clear()
       arcade.draw_circle_filled(300, 300, 200, arcade.color.YELLOW)
       arcade.draw_circle_filled(380, 350, 20, arcade.color.BLACK)
       arcade.draw_circle_filled(220, 350, 20, arcade.color.BLACK)
       center_x = 300
       center_y = 230
       width = 150
       height = 80
       start_angle = 180
       end_angle = 360
       line_width = 10
       arcade.draw_arc_outline(center_x, center_y, width, height, arcade.color.BLACK, start_angle, end_angle,
                               line_width)


def main():
   window = MyGame()
   window.setup()
   arcade.run()


if __name__ == "__main__":
   main()
