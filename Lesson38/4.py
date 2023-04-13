import pygame


GRAY = (127,127,127)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

background = GRAY
size = 640,320
width,height = size
screen = pygame.display.set_mode(size)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

    screen.fill(background)
#левая верхняя точка,(x y), ширина, высота
    pygame.draw.ellipse(screen,RED,(50,20,160,100))
    pygame.draw.ellipse(screen, GREEN, (100,60,160,100))
    pygame.draw.ellipse(screen, BLUE, (150, 100, 160, 100))

    pygame.draw.ellipse(screen, RED, (350, 20, 160, 100),1)
    pygame.draw.ellipse(screen, GREEN, (400, 60, 160, 100),4)
    pygame.draw.ellipse(screen, BLUE, (450, 100, 160, 100),8)

    pygame.display.update()
pygame.quit()
