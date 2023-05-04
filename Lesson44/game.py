# import pygame
# print(pygame.__file__)

import pygame
from pygame.locals import *

clock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('пинг-понг')

xb = 500
yb = 300

ball_speed = 5
right = False
top = False

x1 = 490
y1 = 250
x2 = 0
y2 = 250

score1 = 0
score2 = 0

pygame.mixer.pre_init(44100,-16,1,12)
pygame.init()

s = pygame.mixer.Sound('sound.wav')
win = pygame.mixer.Sound('win.wav')

running = True
print(f'score 1 : {score1}, score2 : {score2}')

def collision():
    global x1,y1,x2,y2,xb,yb,x,y,right,score1,score2


    if right==True:
        if xb > 480:
            if yb >= y_mouse and yb <y_mouse +50:
                right = False
                s.play()
            else:
                score2 += 1
                pygame.display.set_caption(f' PING-PONG   {score2}   :   {score1}')
                xb,yb = 10,20
                pygame.time.delay(500)
                win.play()

    else:
        if xb < 10:
            if yb >= y2 and yb <y2 +50:
                right = True
                s.play()
            else:
                score1 += 1
                pygame.display.set_caption(f' PING-PONG   {score2}   :   {score1}')
                xb,yb = 480,20
                pygame.time.delay(500)
                win.play()




def sprite1(y):
    pygame.draw.rect(screen, (255, 0, 0), (x1, y, 10, 50))


def sprite2(y):
    pygame.draw.rect(screen, (0, 255, 0), (x2, y, 10, 50))


def move2():
    global y2
    if y2 <= 450:
        if keys[K_z]:
            y2 += 10
    if y2 > 0:
        if keys[K_a]:
            y2 -= 10


def move_ball():
    global right, top, xb, yb, ball_speed

    if right == False:
        xb -= ball_speed
    if top == False:
        yb += ball_speed
        if yb > 490:
            top = True

    if right == True:
        xb += ball_speed

    if top == True:
        yb -= ball_speed
        if yb < 10:
            top = False


def ball():
    global xb, yb
    pygame.draw.ellipse(screen, (0, 255, 0), (xb, yb, 10, 10))


while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    screen.fill((0, 0, 0))
    ball()
    move_ball()
    sprite2(y2)
    move2()
    x_mouse, y_mouse = pygame.mouse.get_pos()
    sprite1(y_mouse)
    collision()
    pygame.display.update()

pygame.quit()
