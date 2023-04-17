# Rect(left,top,width,height)
# Rect(pos,size)
# Rect(obj)

import pygame
from pygame.locals import *

SIZE = 500,200

RED = (255,0,0)
GREEN = (0,255,0)
GRAY = (150,150,150)


pygame.init()
screen = pygame.display.set_mode(SIZE)

rect = Rect(50,SIZE[1]/2,200,80)

print(f'x = {rect.x},y = {rect.y}, width = {rect.w},height = {rect.h}')
print(f'left = {rect.left}, right = {rect.right},top = {rect.top}, bottom = {rect.bottom}')
print(f'center = {rect.center}')

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type ==KEYDOWN:
            if event.key == K_l:
                rect.left = 0
            if event.key == K_r:
                rect.right = SIZE[0]
            if event.key == K_t:
                rect.top = 0
            if event.key == K_b:
                rect.bottom = SIZE[1]
            if event.key == K_c:
                rect.centerx = SIZE[0]//2
            if event.key == K_m:
                rect.centery = SIZE[1]//2
    screen.fill(GRAY)
    pygame.draw.rect(screen,RED,rect)
    pygame.display.flip()

pygame.quit()

