import pygame
from pygame import *

WIN_WIDTH = 800
WIN_HEIGHT = 640
BACKGROUND_COLOR = '#004400'

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = '#FF6262'

MOVE_SPEED = 7
WIDTH = 22
HEIGHT = 32
COLOR = '#888888'

class Player(sprite.Sprite):
    def __init__(self,x,y):
        sprite.Sprite.__init__(self)
        self.xvel = 0
        self.startX = x
        self.startY = y

        self.image = Surface((WIDTH,HEIGHT))
        self.image.fill(Color(COLOR))

        self.rect = Rect(x,y,WIDTH,HEIGHT)

    def update(self,left,right):
        if left:
            self.xvel = -MOVE_SPEED

        if right:
            self.xvel = MOVE_SPEED

        if not(left or right):
            self.xvel = 0

        self.rect.x += self. # сдвигаем координаты игрока на значение смещения

    def draw(self):
        screen.blit(self.image,(self.rect.x, self.rect.y))


level = [
    "-------------------------",
    "-                       -",
    "-                       -",
    "-                       -",
    "-            --         -",
    "-                       -",
    "--                      -",
    "-                       -",
    "-                   --- -",
    "-                       -",
    "-                       -",
    "-      ---              -",
    "-                       -",
    "-   -----------         -",
    "-                       -",
    "-                -      -",
    "-                   --  -",
    "-                       -",
    "-                       -",
    "-------------------------"]

pygame.init()
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Платформер')

bg = Surface((WIN_WIDTH, WIN_HEIGHT))
bg.fill(Color(BACKGROUND_COLOR))

while True:
    for e in pygame.event.get():
        if e.type == QUIT:
            raise SystemExit

        screen.blit(bg, (0, 0))  # отрисовка поверхности bg на поверхности screen

        # x = y = 0
        x = 0
        y = 0
        for row in level:
            for col in row:
                if col == '-':
                    pf = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                    pf.fill(Color(PLATFORM_COLOR))
                    screen.blit(pf,(x,y))

                x += PLATFORM_WIDTH
            y+= PLATFORM_HEIGHT
            x = 0




        pygame.display.update()
