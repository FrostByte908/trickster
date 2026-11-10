import pygame
import random


pygame.init()

WIDTH = 1200
HEIGHT = 600


class Player:
    def __init__(self):
        self.image = pygame.image.load("1.png").convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (80, 80))
        self.rect = self.image.get_rect(
            midbottom=(WIDTH // 2, HEIGHT - 20)
        )
        self.speed = 2

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        self.rect.left = max(self.rect.left, 0)
        self.rect.right = min(self.rect.right, WIDTH)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Coin:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, WIDTH - 20), -20, 20, 20)
        self.speed = 1

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - 20)
            self.rect.top = -20

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 215, 0), self.rect.center, 10)

    def respawn(self,):
        self.rect.x = random.randint(0, WIDTH - 20)
        self.rect.top = -20


class Enemy:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, WIDTH - 20), -20, 20, 20)
        self.speed = 1

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - 20)
            self.rect.top = -20

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 60, 60), self.rect.center, 12)

    def respawn(self,):
        self.rect.x = random.randint(0, WIDTH - 20)
        self.rect.top = -20


screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True
clock = pygame.time.Clock()

player = Player()
coin = Coin()
bomb = Enemy()

score = 0

font = pygame.font.SysFont(None, 36)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.update(keys)
    coin.update()
    bomb.update()

    if player.rect.colliderect(coin.rect):
        score += 1
        coin.respawn()
        print(score)

    if player.rect.colliderect(bomb.rect):
        score -= 10
        bomb.respawn()
        print(f'Бум! {score}')

    text = font.render(f"Счёт: {score}", True, (255, 255, 255))
    screen.blit(text, (10,10))

    screen.fill((15, 15, 15))
    screen.blit(text, (10, 10))
    player.draw(screen)
    coin.draw(screen)
    bomb.draw(screen)
    pygame.display.flip()

pygame.quit()