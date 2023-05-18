import random

import pygame

pygame.init()
screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()

pygame.mixer.music.load('nyan.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)
class ParticleStyle:
    def __init__(self):
        self.particles = []
        self.size = 8

    def add_particles(self,offset,color):
        pos_x = pygame.mouse.get_pos()[0]
        pos_y = pygame.mouse.get_pos()[1] + offset

        particle_rect = pygame.Rect(pos_x  -self.size /2, pos_y - self.size/2, self.size, self.size)
        self.particles.append((particle_rect,color))

    def delete_particles(self):
        particles_copy = [particle for particle in self.particles if particle[0].x > 0]
        self.particles = particles_copy

    def process_particles(self):
        if self.particles:
            self.delete_particles()
            for particle in self.particles:
                particle[0].x -= 1
                pygame.draw.rect(screen,particle[1],particle[0])
        self.nyan()

    def nyan(self):
        nyan_rect = nyan_img.get_rect()
        # nyan_rect = nyan_img.get_rect(center=pygame.mouse.get_pos())
        nyan_rect.center = pygame.mouse.get_pos()
        screen.blit(nyan_img,nyan_rect)



nyan_img = pygame.image.load('nyan_cat.png')
w,h = nyan_img.get_rect().w,nyan_img.get_rect().h
nyan_img = pygame.transform.scale(nyan_img,(w*0.66,h*0.66))
PARTICLE_EVENT = pygame.USEREVENT
pygame.time.set_timer(PARTICLE_EVENT,20)
particle2 = ParticleStyle()

running = True

while running:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == PARTICLE_EVENT:
            particle2.add_particles(-20,pygame.Color('Red'))
            particle2.add_particles(-12, pygame.Color('Orange'))
            particle2.add_particles(-4, pygame.Color('Yellow'))
            particle2.add_particles(4, pygame.Color('Green'))
            particle2.add_particles(12, pygame.Color('Blue'))
            particle2.add_particles(20, pygame.Color('Purple'))

    screen.fill((30,30,30))
    particle2.process_particles()
    pygame.display.update()
pygame.quit()
