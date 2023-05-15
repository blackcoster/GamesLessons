import time
from random import randint
import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640,320))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('player.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = 100
        self.rect.bottom = 100

class Item(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('light.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

light = pygame.image.load('light.png')
light = pygame.transform.scale(light,(100,100))
player = Player()
light_on = False
running = True
score = 0
lives = 3
brick = pygame.rect.Rect(200,200,50,50)
start = time.time()
items = [] # список предметов

item = Item(130,50)
items.append(item)


# for _ in range(10):
#     item = Item(randint(0,640),randint(0,320))
#     items.append(item)

while running:
    for e in pygame.event.get():
        if e.type == QUIT:
            running = False
        if e.type == KEYDOWN and e.key == K_SPACE:
            light_on = True
        if e.type == KEYUP and e.key == K_SPACE:
            light_on = False
        if e.type == KEYDOWN and e.key == K_RIGHT:
            player.rect.x += 10
        if e.type == KEYDOWN and e.key == K_LEFT:
            player.rect.x -= 10
        if e.type == KEYDOWN and e.key == K_UP:
            player.rect.y -= 10
        if e.type == KEYDOWN and e.key == K_DOWN:
            player.rect.y += 10
        # if e.type == MOUSEMOTION:
        #     print(e.pos)

    screen.fill(pygame.color.Color('Red'))
    filter = pygame.surface.Surface((640,320))
    filter.fill(pygame.color.Color('Gray'))
    if light_on:
        filter.blit(light,(player.rect.x -25,player.rect.y-25))
    pygame.display.set_caption(f'жизней осталось - {lives}')
    screen.blit(filter,(0,0),special_flags=pygame.BLEND_RGBA_SUB)
    for i in items:
        screen.blit(item.image,item.rect)

    # if player.rect.colliderect(item.rect):
    #     score+=1
    #     items.pop()
    #     print(score)
    if player.rect.colliderect(brick):
        player.rect.x = 20
        player.rect.y = 20
        lives -=1
    if lives == 0:
        running = False
        print('жизни всё')
    end = time.time()
    if (end-start) >= 100:
        running = 0
        print('вы проиграли')
    screen.blit(player.image,player.rect)
    pygame.draw.rect(screen,(0,255,0),brick)
    pygame.display.update()
pygame.quit()