import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BALL_SIZE, WHITE


class Ball:
    def __init__(self, x, y, size=BALL_SIZE, speed=7):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.dx = speed
        self.dy = speed

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.size, self.size))

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def bounce_y(self):
        self.dy = -self.dy

    def bounce_x(self):
        self.dx = -self.dx

    def reset(self):
        self.x = SCREEN_WIDTH // 2 - self.size // 2
        self.y = SCREEN_HEIGHT // 2 - self.size // 2
        self.dx = self.speed
        self.dy = self.speed

    def check_boundary(self):
        if self.y <= 0 or self.y + self.size >= SCREEN_HEIGHT:
            self.bounce_y()

    def check_paddle_collision(self, paddle):
        if (
            self.x < paddle.rect.x + paddle.rect.width
            and self.x + self.size > paddle.rect.x
            and self.y < paddle.rect.y + paddle.rect.height
            and self.y + self.size > paddle.rect.y
        ):
            self.bounce_x()
            return True
        return False

    def check_scoring(self, left_score, right_score):
        if self.x < 0:
            right_score += 1
            self.reset()
            return left_score, right_score, True
        elif self.x + self.size > SCREEN_WIDTH:
            left_score += 1
            self.reset()
            return left_score, right_score, True
        return left_score, right_score, False
