import pygame
from pygame import *

WIDTH = 800
HEIGHT = 640
BACKGROUND_COLOR = '#004400'

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = '#FF6262'

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
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Платформер')

bg = Surface((WIDTH, HEIGHT))
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
