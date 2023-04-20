import math

import pygame
from pygame.locals import *


RED = (255,0,0)
GRAY = (127,127,127)
GREEN = (0,255,0)

pygame.init()
w,h = 640,400
screen = pygame.display.set_mode((w,h))


running = True
# сохраняем исходное изображение чтобы модифицировать img
img0 = pygame.image.load('bird.png')
img0.convert()

img = pygame.image.load('bird.png')
img.convert()

rect0 = img0.get_rect()
center = w//2, h//2

img = img0
rect = img.get_rect()

rect.center = center
moving = False

angle = 0
scale = 1

mouse = pygame.mouse.get_pos()
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        # elif event.type == MOUSEBUTTONDOWN:
        #     if rect.collidepoint(event.pos):
        #         moving = True
        # elif event.type == MOUSEBUTTONUP:
        #     moving = False
        # elif event.type == MOUSEMOTION and moving:
        #     rect.move_ip(event.rel)
        elif event.type == MOUSEMOTION:
            mouse = event.pos
            x = mouse[0] - center[0]
            y = mouse[1] - center[1]
            d = math.sqrt(x**2 + y**2)

            angle = math.degrees(-math.atan2(y,x))
            # scale = abs(5*d/w)
            scale = abs(d)
            img = pygame.transform.rotozoom(img0,angle,scale)
            rect = img.get_rect()
            rect.center = center

        elif event.type ==KEYDOWN:
            if event.key == K_r:
                if event.mod & KMOD_SHIFT:
                    angle-=10
                else:
                    angle+=10
                img = pygame.transform.rotozoom(img0, angle, scale)
            elif event.key == K_s:
                if event.mod & KMOD_SHIFT:
                    scale/= 1.1
                else:
                    scale*= 1.1
                img = pygame.transform.rotozoom(img0,angle,scale)
            elif event.key == K_o:
                img = img0
                angle = 0
                scale = 1
            elif event.key ==K_h:
                img = pygame.transform.flip(img,True, False)
            elif event.key == K_v:
                img = pygame.transform.flip(img,False,True)
            elif event.key == K_l:
                img = pygame.transform.laplacian(img)
            elif event.key == K_2:
                img = pygame.transform.scale2x(img)

    screen.fill(GRAY)
    rect = img.get_rect()
    rect.center = center
    screen.blit(img,rect)  # создает поверхность img на поверхности screen в координатах прямоугольника rect
    pygame.draw.rect(screen,RED,rect,1)
    pygame.draw.line(screen,GREEN,center,mouse,1)
    pygame.draw.circle(screen,RED,center,6,1)
    pygame.draw.circle(screen, RED, mouse, 6, 1)
    pygame.display.update()

pygame.quit()