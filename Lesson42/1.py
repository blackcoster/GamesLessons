import pygame
from pygame.locals import *

SIZE = WIDTH,HEIGHT = 600,400
BACKGROUND_COLOR = pygame.Color('white')
is_walking = False
MOVE_SPEED = 7
left = right = False

class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite,self).__init__()

        self.images = []
        for i in range(1,11):
            self.images.append(pygame.image.load(f'images/walk{i}.png'))

        self.index = 0
        self.xvel = 0
        self.image = self.images[self.index]

        self.rect = pygame.Rect(5,5,150,198)

    def update(self):
        if is_walking:
            self.rect.x += self.xvel
            self.index+=1
            if self.index >= len(self.images):
                self.index = 0
        self.image = self.images[self.index]
        if left:
            self.xvel = - MOVE_SPEED
            self.image = pygame.transform.flip(self.image,True,False)
        if right:
            self.xvel = MOVE_SPEED

        if not(left or right):
            self.xvel = 0

def main():
    global left, right
    global is_walking
    pygame.init()

    screen = pygame.display.set_mode(SIZE)
    my_sprite = MySprite()
    my_group = pygame.sprite.Group()
    my_group.add(my_sprite)
    clock = pygame.time.Clock()



    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                raise SystemExit
            elif event.type == pygame.KEYDOWN and event.key ==K_LEFT:
                left = True
                is_walking = True
            elif event.type == pygame.KEYDOWN and event.key == K_RIGHT:
                right = True
                is_walking = True
            elif event.type == pygame.KEYUP and event.key == K_LEFT:
                left = False
                is_walking = False
            elif event.type == pygame.KEYUP and event.key == K_RIGHT:
                right = False
                is_walking = False

        my_group.update()
        screen.fill(BACKGROUND_COLOR)
        my_group.draw(screen)
        pygame.display.update()
        clock.tick(10)


if __name__=='__main__':
    main()
