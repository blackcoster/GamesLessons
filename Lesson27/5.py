import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT=600

class Rectangle:
    def __init__(self,x,y,w,h,color,tilt = 0,filled = False):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.tilt = tilt
        self.filled = filled
        self.change_x = 3
        self.change_y = 3

    def draw(self):
        if self.filled == False:
            arcade.draw_rectangle_outline(self.x,self.y,self.w,self.h,self.color)
        else:
            arcade.draw_rectangle_filled(self.x, self.y, self.w, self.h, self.color)

    def move(self):
        self.x+=self.change_x
        self.y += self.change_y
        if self.x+self.w/2 > SCREEN_WIDTH or self.x-self.w/2 < 0:
            self.change_x=-self.change_x
        if self.y+self.h/2 > SCREEN_HEIGHT or self.y-self.h/2 < 0:
            self.change_y=-self.change_y

    def resize(self):
        if self.x+self.w/2 >= SCREEN_WIDTH or self.x-self.w/2 <= 0:
            self.w+=2
            self.h+=2
        # if self.y+self.h/2 >= SCREEN_HEIGHT or self.y-self.h/2 <= 0:
        #     self.w+=1
        #     self.h+=1

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=SCREEN_WIDTH,height=SCREEN_HEIGHT,title='рисование фигур')
        self.rec = Rectangle(20,100,40,50,arcade.color.BLUE,filled=True)
        self.rec2 = Rectangle(760,200,40,50,arcade.color.RED,filled=True)

    def on_draw(self):
        self.clear()
        self.rec.draw()
        self.rec2.draw()

    def update(self, delta_time: float):
        self.rec.move()
        self.rec2.move()
        self.rec2.resize()



game = Game()
arcade.run()
