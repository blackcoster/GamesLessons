import pygame
from pygame.locals import *
from random import randint,randrange

def circle_surf(radius,color):
    surf = pygame.Surface((radius*2,radius*2))
    pygame.draw.circle(surf,color,(radius,radius),radius)
    # surf.set_colorkey((0,0,0))
    return surf

pygame.init()
pygame.display.set_caption('свет')
screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()

particles = []
# [
# [3,10],8 , [2,0]
# [10,10],10,[-1,0]
# ]
# particles[0][0][0],particles[0][0][1]
running = True
while running:
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == QUIT:
            running = False
        if e.type == KEYDOWN and e.key == K_ESCAPE:
            running = False
    screen.fill((0, 0, 0))
    mx,my = pygame.mouse.get_pos()
    particles.append([[mx,my],
                      randint(6,11),
                      [randrange(-3,4),randrange(-3,4)]])
    for p in particles:
        p[0][1] += 2
        p[0][0]+= p[2][0]
        p[0][1]+=p[2][1]
        p[1] -= 0.1
        radius = p[1]*2
        screen.blit(circle_surf(radius,(20,20,80)),
                    ((int(p[0][0]-radius)),int(p[0][1]-radius)),
                    special_flags=BLEND_RGB_ADD)
        pygame.draw.circle(screen,"white",
                           (int(p[0][0]),int(p[0][1])),int(p[1]))
        if p[1]<=0:
            particles.remove(p)
    pygame.display.update()
pygame.quit()