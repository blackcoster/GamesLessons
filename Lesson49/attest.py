import pygame
import random
import sys

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Простой платформер")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > SCREEN_WIDTH - 20:
            self.rect.x = SCREEN_WIDTH - 20
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > SCREEN_HEIGHT - 20:
            self.rect.y = SCREEN_HEIGHT - 20


class Item(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - 10)
        self.rect.y = random.randrange(SCREEN_HEIGHT - 10)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - 10)
        self.rect.y = random.randrange(SCREEN_HEIGHT - 10)


all_sprites = pygame.sprite.Group()
item_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for i in range(10):
    item = Item()
    all_sprites.add(item)
    item_sprites.add(item)

for i in range(10):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemy_sprites.add(enemy)

clock = pygame.time.Clock()
time_remaining = 700
score = 0
player_lives = 3

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    items_collected = pygame.sprite.spritecollide(player, item_sprites, True)
    for item in items_collected:
        score += 1

    enemies_hit = pygame.sprite.spritecollide(player, enemy_sprites, False)
    if enemies_hit:
        player.rect.x = 20
        player.rect.y = 20
        player_lives -= 1
        for i in range(5):
            item = Item()
            all_sprites.add(item)
            item_sprites.add(item)
        if player_lives <= 0:
            running = False

    screen.fill(BLACK)
    all_sprites.draw(screen)

    font = pygame.font.Font(None, 36)
    score_text = font.render("Счет: " + str(score), True, WHITE)
    screen.blit(score_text, [10, 10])
    time_text = font.render("Время: " + str(time_remaining), True, WHITE)
    screen.blit(time_text, [SCREEN_WIDTH - 150, 10])
    lives_text = font.render("Жизни: " + str(player_lives), True, WHITE)
    screen.blit(lives_text, [150, 10])

    time_remaining -= 1
    if time_remaining == 0:
        running = False

    pygame.display.flip()

    clock.tick(60)

result_text = font.render("Вы набрали " + str(score) + " очков!", True, WHITE)
screen.fill(BLACK)
screen.blit(result_text, [SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50])
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()