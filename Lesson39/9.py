from random import randint
import pygame
from pygame.locals import *

SIZE = 500,200

RED = (255,0,0)
GREEN = (0,255,0)
GRAY = (150,150,150)
BLUE = (0,0,255)
YELLOW = (255,255,0)


pygame.init()
screen = pygame.display.set_mode(SIZE)

running = True
rect = Rect(100,50,50,50)

def random_point():
    x = randint(0,SIZE[0])
    y = randint(0,SIZE[1])
    return x,y

def random_rects(n):
    rects = []
    for i in range(n):
        p = random_point()
        r = Rect(p,(20,20))
        rects.append(r)
    return rects
n = 50
rects = random_rects(n)

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                rects = random_rects(n)

    screen.fill(GRAY)
    pygame.draw.rect(screen,GREEN,rect,1)
    for r in rects:
        if rect.colliderect(r)==True:
            pygame.draw.rect(screen,RED,r,2)
        else:
            pygame.draw.rect(screen, BLUE, r, 1)
    pygame.display.flip()
pygame.quit()