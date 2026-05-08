import pygame

from constants import PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_SPEED, SCREEN_HEIGHT, WHITE


class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = PADDLE_SPEED

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)

    def move_up(self):
        if self.rect.top > 0:
            self.rect.y -= self.speed

    def move_down(self):
        if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed

    def update(self, keys, player_num):
        if player_num == 1:
            if keys[pygame.K_w]:
                self.move_up()
            if keys[pygame.K_s]:
                self.move_down()
        elif player_num == 2:
            if keys[pygame.K_UP]:
                self.move_up()
            if keys[pygame.K_DOWN]:
                self.move_down()
