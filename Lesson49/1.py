import pygame
import math
import numpy as np

WHITE = 255,255,255
RED = 255,0,0
BLACK = 0,0,0

WIDTH,HEIGHT = 800,600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('3D')

points= []
points.append(np.matrix([-1,-1,1]))
points.append(np.matrix([1,-1,1]))
points.append(np.matrix([1,1,1]))
points.append(np.matrix([-1,1,1]))
points.append(np.matrix([-1,-1,-1]))
points.append(np.matrix([1,-1,-1]))
points.append(np.matrix([1,1,-1]))
points.append(np.matrix([-1,1,-1]))

projection_matrix = np.matrix([[1,0,0],
                              [0,1,0]])

running = True
scale = 100
circle_pops = [WIDTH/2,HEIGHT/2]
angle = 0
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    rotation_z = np.matrix([
        [math.cos(angle), -math.sin(angle), 0],
        [math.sin(angle), math.cos(angle), 0],
        [0, 0, 1],
    ])
    angle+=0.01
    screen.fill(WHITE)
    for point in points:
        projected2d = np.dot(projection_matrix,point.reshape((3,1)))
        x = int(projected2d[0][0]*scale)+circle_pops[0]
        y = int(projected2d[1][0]*scale)+circle_pops[1]
        pygame.draw.circle(screen,BLACK,(x,y),5)
    pygame.display.update()
pygame.quit()