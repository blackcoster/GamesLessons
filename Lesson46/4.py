import pygame
from pygame.locals import *


class Button:
    def __init__(self,text,width,height,pos,elevation):
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]
        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = '#475F77'
        self.text_surface = font.render(text,True,'#FFFFFF')
        self.text_rect = self.text_surface.get_rect(center = self.top_rect.center)

        self.bottom_rect = pygame.Rect(pos,(width,elevation))
        self.bottom_color = '#354B5E'

    def draw(self):
        self.text_rect.center = self.top_rect.center
        self.top_rect.y = self.original_y_pos-self.dynamic_elevation
        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height+self.dynamic_elevation

        pygame.draw.rect(screen,self.bottom_color,self.bottom_rect,border_radius=12)
        pygame.draw.rect(screen,self.top_color,self.top_rect,border_radius=12)
        screen.blit(self.text_surface,self.text_rect)
        self.check_click()

    def check_click(self):
        # global running
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#D73B4B'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                if self.pressed:
                    self.dynamic_elevation = self.elevation
                    # running = False
                    print('нажата кнопка')
                    self.pressed = False
        else:
            self.dynamic_elevation = self.elevation
            self.top_color = '#475F77'

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('GUI BUTTON')
clock = pygame.time.Clock()
font = pygame.font.Font(None,30)

button1 = Button('Нажми на меня',200,40,(150,250),6)

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type ==  QUIT:
            running  = False


    screen.fill('#DCDDD8')
    button1.draw()
    pygame.display.update()
pygame.quit()