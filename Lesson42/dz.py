import pygame
from pygame.locals import *


class SpriteSheet():
    def __init__(self,image):
        self.sheet = image
    def get_image(self,frame,width, height,scale,color):
        image = pygame.Surface((width,height)).convert_alpha()
        image.blit(self.sheet,(0,0),((frame*width),0,width,height))
        image = pygame.transform.scale(image,(width*scale,height*scale))
        image.set_colorkey(color)
        return image


SIZE = WIDTH,HEIGHT = 500,500
BG = (50,50,50)
BLACK = (0,0,0)




pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Spritesheets')
sprite_sheet_image = pygame.image.load('dino.png').convert_alpha()
sprite_sheet = SpriteSheet(sprite_sheet_image)

frame0 = sprite_sheet.get_image(0,24,24,3,BLACK)
frame1 = sprite_sheet.get_image(1,24,24,3,BLACK)
frame2 = sprite_sheet.get_image(2,24,24,3,BLACK)
frame3 = sprite_sheet.get_image(3,24,24,3,BLACK)

running = True
while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        # if event.type == MOUSEMOTION: # уточнить координаты мышкой
        #     print(event.pos)

    screen.fill(BG)
    # screen.blit(sprite_sheet_image,(0,0)) # посмотреть фул картинку
    screen.blit(frame0,(0,0))
    screen.blit(frame1, (72, 0))
    screen.blit(frame2, (144, 0))
    screen.blit(frame3, (216, 0))
    pygame.display.update()

pygame.quit()