import pygame
from pygame.locals import *


screen = pygame.display.set_mode((600,300))

running = True

BLACK = (0,0,0)
GRAY = (127,127,127)
WHITE = (255,255,255)

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

YELLOW = (255,255,0)
CYAN = (0,255,255)
MAGENTA = (255,0,255)

background = GRAY

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                background = RED
            elif event.key == pygame.K_g:
                background = GREEN
        elif event.type == pygame.QUIT:
            running = False

    caption = 'Цвет фона =' + str(background)
    pygame.display.set_caption(caption)
    screen.fill(background)
    pygame.display.update()

pygame.quit()

# Теперь мы можем обратиться к ключевым модификаторам, таким как alt, ctrl, cmd и т.д
# KMOD_ALT, KMOD_CAPS, KMOD_CTRL, KMOD_LALT,
# KMOD_LCTRL, KMOD_LMETA, KMOD_LSHIFT, KMOD_META,
# KMOD_MODE, KMOD_NONE, KMOD_NUM, KMOD_RALT, KMOD_RCTRL,
# KMOD_RMETA, KMOD_RSHIFT, KMOD_SHIFT
#
#
# числовым клавишам
# K_0, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9
#
#
# специальным символьным клавишам
# K_AMPERSAND, K_ASTERISK, K_AT, K_BACKQUOTE,
# K_BACKSLASH, K_BACKSPACE, K_BREAK
#
#
# и соответственно буквенном клавишам
# K_a, K_b, K_c, K_d, K_e, K_f, K_g, K_h, K_i, K_j, K_k, K_l, K_m,
# K_n, K_o, K_p, K_q, K_r, K_s, K_t, K_u, K_v, K_w, K_x, K_y, K_z

