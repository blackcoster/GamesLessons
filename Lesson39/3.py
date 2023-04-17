# Rect(left,top,width,height)
# Rect(pos,size)
# Rect(obj)

import pygame
from pygame.locals import *

SIZE = 500,200

RED = (255,0,0)
GREEN = (0,255,0)
GRAY = (150,150,150)
BLUE = (0,0,255)

dir = {K_LEFT:(-5,0),
       K_RIGHT:(5,0),
       K_UP:(0,-5),
       K_DOWN:(0,5)}

pygame.init()
screen = pygame.display.set_mode(SIZE)

# rect = Rect(50,SIZE[1]/2,200,80)
rect0 = Rect(50,60,200,80)
rect = rect0.copy()

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type ==KEYDOWN:
            if event.key in dir:
                v = dir[event.key]
                rect.move_ip(v)

    screen.fill(GRAY)
    pygame.draw.rect(screen,BLUE,rect0,1)
    pygame.draw.rect(screen,RED,rect,4)
    pygame.display.flip()


pygame.quit()

