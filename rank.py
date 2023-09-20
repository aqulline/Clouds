import random
from time import sleep

import pygame

pygame.init()


def sides() -> list:
    upk = 1073741906
    dwk = 1073741905
    rhk = 1073741904
    lfk = 1073741903
    up = (bpos_x + 20, bpox_y - 20)
    down = (bpos_x + 20, bpox_y + 70)
    right = (bpos_x - 20, bpox_y + 20)
    left = (bpos_x + 70, bpox_y + 20)

    choic = ["up", "down", "left", "right"]

    choice = random.choice(choic)

    if choice == "up":
        recommended_key = upk
        print(recommended_key)
        return [up, recommended_key]
    if choice == "down":
        recommended_key = dwk
        print(recommended_key)
        return [down, recommended_key]
    if choice == "left":
        recommended_key = lfk
        print(recommended_key)
        return [left, recommended_key]
    if choice == "right":
        recommended_key = rhk
        print(recommended_key)
        return [right, recommended_key]


WIDTH, HEIGHT = 400, 400
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BALL_COLOR = (255, 0, 0)

FONT = pygame.font.Font(None, 36)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Ball")

box2_w, box2_h = 110, 110
bpos2_x, bpox2_y = 150, 150
bcolor2 = (150, 150, 255)
bspeed2 = .1

box_w, box_h = 50, 50
bpos_x, bpox_y = 175, 175
bcolor = (150, 255, 255)
bspeed = .1

score = 0

# Ball
ball_radius = 15
ball_pos = 10
(ball_x, ball_y), recommended_key = sides()

ball_speed = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        bpos_x -= bspeed
        if recommended_key == pygame.K_LEFT:
            (ball_x, ball_y), recommended_key = sides()
            sleep(.1)
            print(recommended_key, pygame.K_LEFT)
            score += 1
        else:
            (ball_x, ball_y), recommended_key = sides()
            sleep(.1)
            print(recommended_key, pygame.K_LEFT)
            score -= 1
    if keys[pygame.K_RIGHT]:
        bpos_x += bspeed
        if recommended_key == pygame.K_RIGHT:
            (ball_x, ball_y), recommended_key = sides()
            sleep(.1)
            print(recommended_key, pygame.K_RIGHT)
            score += 1
        else:
            (ball_x, ball_y), recommended_key = sides()
            sleep(.1)
            print(recommended_key, pygame.K_RIGHT)
            score -= 1
    if keys[pygame.K_UP]:
        bpox_y -= bspeed
        if recommended_key == pygame.K_UP:
            (ball_x, ball_y), recommended_key = sides()
            sleep(.1)
            print(recommended_key, pygame.K_UP)
            score += 1
        else:
            (ball_x, ball_y), recommended_key = sides()
            sleep(.1)
            print(recommended_key, pygame.K_UP)
            score -= 1
    if keys[pygame.K_DOWN]:
        bpox_y += bspeed
        if recommended_key == pygame.K_DOWN:
            (ball_x, ball_y), recommended_key = sides()
            sleep(.1)
            print(recommended_key, pygame.K_DOWN)
            score += 1
        else:
            (ball_x, ball_y), recommended_key = sides()
            sleep(.1)
            print(recommended_key, pygame.K_DOWN)
            score -= 1

    bpos_x = max(0, min(WIDTH - box_w, bpos_x))
    bpox_y = max(0, min(HEIGHT - box_h, bpox_y))

    screen.fill(WHITE)

    # pygame.draw.rect(screen, bcolor2, (bpos2_x, bpox2_y, box2_w, box2_h))
    pygame.draw.rect(screen, bcolor, (bpos_x, bpox_y, box_w, box_h))
    pygame.draw.circle(screen, BALL_COLOR, (ball_x, int(ball_y)), ball_radius)
    score_text = FONT.render(f"Score: {score}", True, BLUE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
