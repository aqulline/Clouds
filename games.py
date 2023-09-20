import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
PADDLE_COLOR = (0, 128, 0)
BALL_COLOR = (255, 0, 0)
FONT = pygame.font.Font(None, 36)

# Initialize Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Ball")

# Paddle
paddle_width, paddle_height = 100, 20
paddle_x = (WIDTH - paddle_width) // 2
paddle_y = HEIGHT - paddle_height - 10
paddle_speed = .3

# Ball
ball_radius = 20
ball_x = random.randint(ball_radius, WIDTH - ball_radius)
ball_y = 0
ball_speed = .15

# Game variables
score = 0

def sides():
    print()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT]:
        paddle_x += paddle_speed

    # Keep the paddle within the screen boundaries
    paddle_x = max(0, min(WIDTH - paddle_width, paddle_x))

    # Move the ball
    ball_y += ball_speed

    # Check if the ball hit the paddle
    if (
        ball_y + ball_radius >= paddle_y
        and ball_x + ball_radius >= paddle_x
        and ball_x - ball_radius <= paddle_x + paddle_width
    ):
        score += 1
        ball_x = random.randint(ball_radius, WIDTH - ball_radius)
        ball_y = 0

    # Check if the ball missed the paddle
    if ball_y > HEIGHT:
        ball_x = random.randint(ball_radius, WIDTH - ball_radius)
        score -= 1
        ball_y = 0

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, PADDLE_COLOR, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, BALL_COLOR, (ball_x, int(ball_y)), ball_radius)
    score_text = FONT.render(f"Score: {score}", True, BLUE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

# Quit Pygame
pygame.quit()
