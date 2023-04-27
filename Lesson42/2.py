import pygame
from pygame.locals import *

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))

        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)

        return image


pygame.init()

SCREEN_WIDTH = 500
BLACK = (0, 0, 0)
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spritesheets')

BG = (50, 50, 50)
animation_list = []
animation_steps = [4, 6, 3, 4,7]
last_update = pygame.time.get_ticks()
animation_cooldown = 500
frame = 0
action = 0

sprite_sheet_image = pygame.image.load('dino.png').convert_alpha()
sprite_sheet = SpriteSheet(sprite_sheet_image)

step_counter = 0
for animation in animation_steps:
    temp_img_list = []
    for _ in range(animation):
        temp_img_list.append(sprite_sheet.get_image(step_counter, 24, 24, 3, BLACK))
        step_counter += 1
    animation_list.append(temp_img_list)

running = True
while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
                if event.key == K_DOWN and action > 0:
                    action -= 1
                    frame = 0
                if event.key == K_UP and action < len(animation_list) - 1:
                    action += 1
                    frame = 0

    screen.fill(BG)

    screen.blit(animation_list[action][frame], (0, 0))

    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        if frame >= len(animation_list[action]):
            frame = 0
        last_update = current_time

    pygame.display.update()

pygame.quit()
