import pygame
import sys

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, WINNING_SCORE, SCORE_FONT_SIZE
from paddle import Paddle
from ball import Ball


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pong Duel")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, SCORE_FONT_SIZE)

    left_paddle = Paddle(20, SCREEN_HEIGHT // 2 - 50)
    right_paddle = Paddle(SCREEN_WIDTH - 35, SCREEN_HEIGHT // 2 - 50)
    ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    left_score = 0
    right_score = 0

    running = True
    game_over = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                left_score = 0
                right_score = 0
                game_over = False
                ball.reset()
            continue

        left_paddle.update()
        right_paddle.update()
        ball.update()

        if ball.check_collision(left_paddle) or ball.check_collision(right_paddle):
            ball.handle_paddle_collision()

        if ball.check_wall_collision():
            ball.handle_wall_collision()

        score_result = ball.check_scoring()
        if score_result == "left":
            left_score += 1
            ball.reset()
        elif score_result == "right":
            right_score += 1
            ball.reset()

        if left_score >= WINNING_SCORE or right_score >= WINNING_SCORE:
            game_over = True

        screen.fill(BLACK)

        for i in range(0, SCREEN_HEIGHT, 40):
            pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH // 2 - 2, i, 4, 20))

        left_paddle.draw(screen)
        right_paddle.draw(screen)
        ball.draw(screen)

        score_text = font.render(f"{left_score}  {right_score}", True, WHITE)
        screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 20))

        if game_over:
            winner = "Left Player" if left_score >= WINNING_SCORE else "Right Player"
            game_over_text = font.render(f"{winner} Wins! Press R to restart", True, WHITE)
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
