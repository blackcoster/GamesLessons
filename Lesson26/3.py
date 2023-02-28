import arcade

class Game(arcade.Window):
    # def __init__(self):
    #     super().__init__()
    #     self.height = 300
    #     self.width = 400
    #     self.set_caption('polina')

    # def __init__(self,w,h,t):
    #     super().__init__(w,h,t)

    def __init__(self):
        super().__init__(width = 300,height = 400,title = 'polina',resizable=True,) #fullscreen = True, visible = False
        self.background_color =(0,0,150)
        self.center_window()
        print(self.get_size())
        print(self.get_location())
        self.set_max_size(900, 700)
        self.set_mouse_visible(False)

    def on_draw(self):
        self.clear()
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        self.set_location(500,500)
        self.set_size(300,100)
        self.set_caption('tfyghjk')
        self.background_color=(255,0,0)


game = Game()
arcade.run()