import random

import pygame

pygame.init()
screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()

class ParticleStyle:
    def __init__(self):
        self.particles = []
        self.star_img = pygame.image.load('star.png')
        self.width = self.star_img.get_rect().width
        self.height = self.star_img.get_rect().height

    def add_particles(self):
        pos_x = pygame.mouse.get_pos()[0] - self.width/2
        pos_y = pygame.mouse.get_pos()[1] - self.height/2
        direction_x = random.randint(-3,3)
        direction_y = random.randint(-3, 3)
        lifetime = random.randint(4,10)
        particle_rect = pygame.Rect(pos_x,pos_y,self.width,self.height)

        self.particles.append([particle_rect,direction_x,direction_y,lifetime])


    def delete_particles(self):
        particles_copy = [particle for particle in self.particles if particle[3]>0]
        self.particles = particles_copy

    def process_particles(self):
        if self.particles:
            self.delete_particles()
            for particle in self.particles:
                particle[0].x += particle[1]
                particle[0].y += particle[2]
                particle[3] -= 0.2
                screen.blit(self.star_img,particle[0])



PARTICLE_EVENT = pygame.USEREVENT
pygame.time.set_timer(PARTICLE_EVENT,60)
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
