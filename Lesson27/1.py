import arcade

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800,height=600,title='рисование фигур')
        self.background_color = (255,255,255)

    def on_draw(self):
        self.clear()
        arcade.draw_arc_outline(
            center_x = 400,
            center_y = 300,
            width = 155,
            height=155,
            color=(0,0,0),
            start_angle = 0,
            end_angle=90,
            tilt_angle=0,
            num_segments=16,
            border_width=2

        )
        # arcade.draw_ellipse_filled()
        # arcade.draw_circle_filled()
        arcade.draw_line(
            start_x=300,
            start_y=300,
            end_x=500,
            end_y=300,
            color=(0, 0, 0),
            line_width=2
        )
        arcade.draw_line_strip(
            point_list = [(100,200),(150,250),(200,200)],
            color=(0,0,0),
            line_width=3)
        # arcade.draw_rectangle_outline()
        arcade.draw_lrtb_rectangle_outline(
            left=100,
            right = 300,
            top = 300,
            bottom=100,
            color = (0,0,0)

        )
        arcade.draw_point(
            x = 100,
            y = 200,
            color = (0,0,0,125),
            size = 10
        )
        arcade.draw_triangle_filled(
            x1 = 100,
            y1 = 100,
            x2 = 200,
            y2 = 200,
            x3 = 300,
            y3 = 100,
            color = (0,0,0,150)
            
        )
game = Game()
arcade.run()