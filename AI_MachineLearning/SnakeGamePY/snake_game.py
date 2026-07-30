import pygame
import random
import sys

# -----------------------------
# Game settings
# -----------------------------
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 180, 0)
RED = (255, 0, 0)
GRAY = (40, 40, 40)

START_SPEED = 8
SPEED_INCREMENT = 1
SCORE_FOR_SPEED_UP = 5   # speed increases every 5 points


# -----------------------------
# Helper functions
# -----------------------------
def random_food_position(snake_body):
    """Generate food position not on the snake."""
    while True:
        pos = [
            random.randint(0, GRID_WIDTH - 1) * CELL_SIZE,
            random.randint(0, GRID_HEIGHT - 1) * CELL_SIZE
        ]
        if pos not in snake_body:
            return pos


def draw_text(surface, text, font, color, x, y, center=False):
    img = font.render(text, True, color)
    rect = img.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    surface.blit(img, rect)


def reset_game():
    snake_body = [
        [100, 100],
        [80, 100],
        [60, 100]
    ]
    direction = "RIGHT"
    next_direction = "RIGHT"
    food_pos = random_food_position(snake_body)
    score = 0
    speed = START_SPEED
    game_over = False
    return snake_body, direction, next_direction, food_pos, score, speed, game_over


def is_opposite(dir1, dir2):
    opposites = {
        "UP": "DOWN",
        "DOWN": "UP",
        "LEFT": "RIGHT",
        "RIGHT": "LEFT"
    }
    return opposites.get(dir1) == dir2


# -----------------------------
# Main game
# -----------------------------
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()

    font = pygame.font.SysFont("Arial", 24)
    big_font = pygame.font.SysFont("Arial", 36)

    snake_body, direction, next_direction, food_pos, score, speed, game_over = reset_game()

    running = True
    while running:
        # -----------------------------
        # Event handling
        # -----------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if not game_over:
                    if event.key == pygame.K_UP and not is_opposite(direction, "UP"):
                        next_direction = "UP"
                    elif event.key == pygame.K_DOWN and not is_opposite(direction, "DOWN"):
                        next_direction = "DOWN"
                    elif event.key == pygame.K_LEFT and not is_opposite(direction, "LEFT"):
                        next_direction = "LEFT"
                    elif event.key == pygame.K_RIGHT and not is_opposite(direction, "RIGHT"):
                        next_direction = "RIGHT"
                else:
                    if event.key == pygame.K_r:
                        snake_body, direction, next_direction, food_pos, score, speed, game_over = reset_game()
                    elif event.key == pygame.K_q:
                        running = False

        # -----------------------------
        # Game update
        # -----------------------------
        if not game_over:
            direction = next_direction

            head_x, head_y = snake_body[0].copy()

            if direction == "UP":
                head_y -= CELL_SIZE
            elif direction == "DOWN":
                head_y += CELL_SIZE
            elif direction == "LEFT":
                head_x -= CELL_SIZE
            elif direction == "RIGHT":
                head_x += CELL_SIZE

            new_head = [head_x, head_y]
            snake_body.insert(0, new_head)

            # Check food collision
            if new_head == food_pos:
                score += 1
                food_pos = random_food_position(snake_body)

                # Increase speed every few points
                speed = START_SPEED + (score // SCORE_FOR_SPEED_UP) * SPEED_INCREMENT
            else:
                snake_body.pop()

            # Check wall collision
            if (
                head_x < 0 or head_x >= WIDTH or
                head_y < 0 or head_y >= HEIGHT
            ):
                game_over = True

            # Check self collision
            if new_head in snake_body[1:]:
                game_over = True

        # -----------------------------
        # Drawing
        # -----------------------------
        screen.fill(BLACK)

        # Optional grid
        for x in range(0, WIDTH, CELL_SIZE):
            pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, CELL_SIZE):
            pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))

        # Draw food
        pygame.draw.rect(
            screen,
            RED,
            pygame.Rect(food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE)
        )

        # Draw snake
        for i, segment in enumerate(snake_body):
            color = GREEN if i == 0 else DARK_GREEN
            pygame.draw.rect(
                screen,
                color,
                pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE)
            )

        # Draw score
        draw_text(screen, f"Score: {score}", font, WHITE, 10, 10)

        # Draw speed
        draw_text(screen, f"Speed: {speed}", font, WHITE, 10, 35)

        # Game over screen
        if game_over:
            overlay = pygame.Surface((WIDTH, HEIGHT))
            overlay.set_alpha(180)
            overlay.fill((0, 0, 0))
            screen.blit(overlay, (0, 0))

            draw_text(screen, "Game Over", big_font, WHITE, WIDTH // 2, HEIGHT // 2 - 40, center=True)
            draw_text(screen, f"Final Score: {score}", font, WHITE, WIDTH // 2, HEIGHT // 2 + 5, center=True)
            draw_text(screen, "Press R to Restart or Q to Quit", font, WHITE, WIDTH // 2, HEIGHT // 2 + 35, center=True)

        pygame.display.flip()

        # Control speed
        clock.tick(speed if not game_over else 15)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()