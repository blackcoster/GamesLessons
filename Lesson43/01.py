import pygame
from pygame.locals import *
import math


class CarSprite(pygame.sprite.Sprite):
    def __init__(self, car_image, x, y, rotations=360):
        pygame.sprite.Sprite.__init__(self)
        self.rot_img = []
        self.min_angle = (360 / rotations)
        for i in range(rotations):
            rotated_image = pygame.transform.rotozoom(car_image, 360 - 90 - (i * self.min_angle), 1)
            self.rot_img.append(rotated_image)
        self.min_angle = math.radians(self.min_angle)
        self.image = self.rot_img[0]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.heading = 0
        self.reversing = False
        self.speed = 0
        self.velocity = pygame.math.Vector2(0, 0)
        self.position = pygame.math.Vector2(x, y)

    def accelerate(self, amount):
        if not self.reversing:
            self.speed += amount
        else:
            self.speed -= amount

    def brake(self):
        self.speed /= 2
        if abs(self.speed) < 0.1:
            self.speed = 0

    def reverse(self):
        self.speed = 0
        self.reversing = not self.reversing

    def turn(self, angle_degrees):
        self.heading += math.radians(angle_degrees)
        image_index = int(self.heading / self.min_angle) % len(self.rot_img)
        if self.image != self.rot_img[image_index]:
            x, y = self.rect.center
            self.image = self.rot_img[image_index]
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)

    def update(self):
        self.velocity.from_polar((self.speed,math.degrees(self.heading)))
        self.position+=self.velocity
        self.rect.center = (round(self.position[0]),round(self.position[1]))

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT),pygame.RESIZABLE)
pygame.display.set_caption('машинка')

clock = pygame.time.Clock()
running = True

road_image = pygame.image.load('road_texture.png')
background = pygame.transform.smoothscale(road_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

car_image = pygame.image.load('car_128.png').convert_alpha()

black_car = CarSprite(car_image, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
car_sprites = pygame.sprite.Group()
car_sprites.add(black_car)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == VIDEORESIZE:
            WINDOW_WIDTH = event.w
            WINDOW_HEIGHT = event.h
            screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
            background = pygame.transform.smoothscale(road_image,(WINDOW_WIDTH,WINDOW_HEIGHT))

        elif event.type == KEYUP:
            if event.key == K_b:
                print('beep-beep')
            elif event.key == K_r:
                print('задняя передача')
                black_car.reverse()

            elif event.key == K_UP:
                print('газ')
                black_car.accelerate(0.5)
            elif event.key == K_DOWN:
                print("тормоз")
                black_car.brake()

    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        black_car.turn(-1.8)
    if keys[K_RIGHT]:
        black_car.turn(1.8)


    car_sprites.update()
    screen.blit(background, (0, 0))
    car_sprites.draw(screen)
    pygame.display.flip()
    clock.tick_busy_loop(60)

pygame.quit()
