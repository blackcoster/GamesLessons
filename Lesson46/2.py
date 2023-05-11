import time

import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

text = 'PyGame!'
font = pygame.font.SysFont(None,40)
text_surf = font.render(text,True,(0,0,0))
rect = text_surf.get_rect()
rect.topleft = (20,20)

cursor = pygame.Rect(rect.topright,(3,rect.height))

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Text')
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                if len(text)>0:
                   text = text[:-1]
            else:
                text += event.unicode
            text_surf = font.render(text,True,(0,0,0))
            rect.size = text_surf.get_size()
            cursor.topleft = rect.topright
    screen.fill((255,0,0))
    screen.blit(text_surf,rect)
    if time.time() % 1 > 0.5:
        pygame.draw.rect(screen,(0,0,0),cursor)
    pygame.display.update()
    print(time.time())
pygame.quit()