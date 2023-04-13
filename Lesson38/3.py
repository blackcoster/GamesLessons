import pygame
from pygame.locals import *

RED = (255,0,0)



size = (640,320)
width,height = size
screen = pygame.display.set_mode(size)
background = (127,127,127)
running = True
window_title = 'Шарик'
speed = [1,1]

ball = pygame.image.load('ball.gif')
rect = ball.get_rect()


while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    rect = rect.move(speed)
    if rect.left < 0 or rect.right > width:
        speed[0] = - speed[0]
    if rect.top <0 or rect.bottom > height:
        speed[1] = - speed[1]

    pygame.draw.rect(screen,RED,rect,1)
    screen.fill(background)
    screen.blit(ball, rect)
    pygame.display.set_caption(window_title)

    pygame.draw.ellipse(screen, RED, (100,60,160,100))
    pygame.draw.rect(screen, RED, (100, 60, 160, 100),1)
    pygame.draw.polygon(screen,RED,([10,10],[20,50],[70,80]))
    pygame.draw.circle(screen,RED,(10,10),20)


    pygame.display.update()

pygame.quit()
