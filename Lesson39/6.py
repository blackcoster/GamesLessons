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
rect = Rect(50,60,200,80)
moving = False

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos)==True:
                moving = True

        elif event.type == MOUSEBUTTONUP:
            moving = False

        elif event.type == MOUSEMOTION and moving==True:
            rect.move_ip(event.rel)

    screen.fill(GRAY)
    pygame.draw.rect(screen,RED,rect)
    if moving==True:
        pygame.draw.rect(screen,BLUE,rect,4)
    pygame.display.flip()
pygame.quit()