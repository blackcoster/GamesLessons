import pygame
from pygame.locals import *

GRAY = (127, 127, 127)
RED = (255,0,0)
BLUE = (0,0,255)

background = GRAY
size = 640, 320
width, height = size
screen = pygame.display.set_mode(size)
start = (0, 0)
size = (0, 0)
drawing = False
rect_list = []
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            start = event.pos  # x y
            size = 0, 0
            drawing = True

        elif event.type == MOUSEBUTTONUP:
            end = event.pos  # x y
            size = end[0] - start[0], end[1] - start[1]
            rect = pygame.Rect(start,size)
            rect_list.append(rect)
            drawing = False

        elif event.type == MOUSEMOTION and drawing:
            end = event.pos
            size = end[0] - start[0], end[1] - start[1]

    screen.fill(background)

    for rect in rect_list:
        pygame.draw.rect(screen,RED,rect,6)
    pygame.draw.rect(screen,BLUE,(start,size),1)

    pygame.display.update()
pygame.quit()
