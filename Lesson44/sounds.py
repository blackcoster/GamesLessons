# pygame.mixer
# pygame.mixer.music
#
# pygame.mixer.music.load('1.wav')
# queue()

import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((400,300))

#фоновый звук
pygame.mixer.music.load('1.ogg')
pygame.mixer.music.play(-1)

#короткие звуки
sound1 = pygame.mixer.Sound('2.ogg')
sound2 = pygame.mixer.Sound('3.ogg')

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                sound1.play()
            elif event.button == 3:
                sound2.play()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_0:
                pygame.mixer.music.pause()
            elif event.key == pygame.K_1:
                pygame.mixer.music.unpause()
            elif event.key == pygame.K_2:
                pygame.mixer.music.unpause()
                pygame.mixer.music.set_volume(0.5)
            elif event.key == pygame.K_3:
                pygame.mixer.music.unpause()
                pygame.mixer.music.set_volume(1)

pygame.exit()