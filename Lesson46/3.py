import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((500,500))

font = pygame.font.Font(None,40)
user_text = ''

input_rect = pygame.Rect(200,200,140,32)

color_active =pygame.Color('lightskyblue')
color_passive = pygame.Color('gray15')
color = color_passive

active = False

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
        if event.type == KEYDOWN and active:
            if event.key == K_BACKSPACE:
                user_text = user_text[0:-1]
            else:
                user_text+=event.unicode

    screen.fill((0,0,0))
    if active:
        color = color_active
    else:
        color = color_passive
    pygame.draw.rect(screen,color,input_rect)
    text_surface = font.render(user_text,True,(255,255,255))
    screen.blit(text_surface,(input_rect.x +5,input_rect.y+5))
    input_rect.w = max(100,text_surface.get_width()+10)
    pygame.display.update()

pygame.quit()