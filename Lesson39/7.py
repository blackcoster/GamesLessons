from time import sleep
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
v = [2,2]

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    rect.move_ip(v)
    sleep(0.05)
    if rect.left < 0:
        v[0]*= -1
    if rect.right > SIZE[0]:
        v[0]*= -1
    if rect.top < 0:
        v[1]*= -1
    if rect.bottom > SIZE[1]:
        v[1]*= -1

    screen.fill(GRAY)
    pygame.draw.rect(screen,RED,rect)
    pygame.display.flip()
pygame.quit()