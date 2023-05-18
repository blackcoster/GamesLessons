# particles = [[pos_x,pos_y],radius,direction],[[pos_x,pos_y],radius,direction],[[pos_x,pos_y],radius,direction],[[pos_x,pos_y],radius,direction]
# particle =[[pos_x,pos_y],radius,direction]
#
# particles[0] = [pos_x,pos_y]
# pos_y = particles[0][1]
# a = [x,y]
# x = a[0]
# particles[1] = radius
# particles[2] = direction
import random

import pygame

pygame.init()
screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()

class ParticleStyle:
    def __init__(self):
        self.particles = []

    def add_particles(self):
        pos_x = pygame.mouse.get_pos()[0]
        pos_y = pygame.mouse.get_pos()[1]
        radius = 10
        direction_x = random.randint(-3,3)
        direction_y = random.randint(-3, 3)
        particle_item = [[pos_x,pos_y],radius,[direction_x,direction_y]]

        self.particles.append(particle_item)


    def delete_particles(self):
        particles_copy = [particle for particle in self.particles if particle[1]>0]
        self.particles = particles_copy

    def process_particles(self):
        if self.particles:
            self.delete_particles()
            for particle in self.particles:
                particle[0][0] += particle[2][0]
                particle[0][1] += particle[2][1]
                particle[1] -= 0.2
                pygame.draw.circle(screen,pygame.Color('White'),particle[0],particle[1])






PARTICLE_EVENT = pygame.USEREVENT
pygame.time.set_timer(PARTICLE_EVENT,150)
particle1 = ParticleStyle()

running = True

while running:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == PARTICLE_EVENT:
            particle1.add_particles()

    screen.fill((30,30,30))
    particle1.process_particles()
    pygame.display.update()
pygame.quit()
