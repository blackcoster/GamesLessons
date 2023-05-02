from random import randrange

import pygame
import pymunk.pygame_util
from pygame.locals import *

def create_square(space,pos):
    square_mass = 1
    square_size = (60,60)
    square_moment = pymunk.moment_for_box(square_mass,square_size)
    square_body = pymunk.Body(square_mass,square_moment)
    square_body.position = pos

    square_shape = pymunk.Poly.create_box(square_body,square_size)
    square_shape.elasticity = 0.8
    square_shape.friction = 1.0
    square_shape.color = [randrange(256) for i in range(4)]
    space.add(square_body,square_shape)

pymunk.pygame_util.positive_y_is_up = False

SIZE = WIDTH,HEIGHT = 900,600
pygame.init()

screen = pygame.display.set_mode(SIZE)

draw_options = pymunk.pygame_util.DrawOptions(screen)
clock = pygame.time.Clock()
running = True

space = pymunk.Space()
space.gravity = 0,8000

segment_shape = pymunk.Segment(space.static_body,(0,HEIGHT),(WIDTH,HEIGHT),26)
space.add(segment_shape)
segment_shape.elasticity = 0.8
segment_shape.friction = 1.0



while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running=False
        if event.type == MOUSEBUTTONDOWN:
            create_square(space,event.pos)
            print(event.pos)

    screen.fill(pygame.Color('black'))

    space.step(1/60)
    space.debug_draw(draw_options)


    pygame.display.update()
    clock.tick(60)

pygame.quit()

