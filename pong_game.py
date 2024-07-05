import pygame
import sys

pygame.init()

# Screen dimensions
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Paddle dimensions
paddle_width, paddle_height = 10, 100

# Ball properties
ball_radius, ball_speed = 7, [4, 4]

# Initial positions
left_paddle_pos = [10, height // 2 - paddle_height // 2]
right_paddle_pos = [width - 20, height // 2 - paddle_height // 2]
ball_pos = [width // 2, height // 2]

# Paddle movement speed
paddle_speed = 6

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle_pos[1] > 0:
        left_paddle_pos[1] -= paddle_speed
    if keys[pygame.K_s] and left_paddle_pos[1] < height - paddle_height:
        left_paddle_pos[1] += paddle_speed
    if keys[pygame.K_UP] and right_paddle_pos[1] > 0:
        right_paddle_pos[1] -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle_pos[1] < height - paddle_height:
        right_paddle_pos[1] += paddle_speed

    # Move the ball
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Ball collision with top and bottom walls
    if ball_pos[1] - ball_radius < 0 or ball_pos[1] + ball_radius > height:
        ball_speed[1] = -ball_speed[1]

    # Ball collision with paddles
    if (ball_pos[0] - ball_radius < left_paddle_pos[0] + paddle_width and
        left_paddle_pos[1] < ball_pos[1] < left_paddle_pos[1] + paddle_height):
        ball_speed[0] = -ball_speed[0]
    if (ball_pos[0] + ball_radius > right_paddle_pos[0] and
        right_paddle_pos[1] < ball_pos[1] < right_paddle_pos[1] + paddle_height):
        ball_speed[0] = -ball_speed[0]

    # Clear the screen
    window.fill(black)

    # Draw the paddles and ball
    pygame.draw.rect(window, white, (*left_paddle_pos, paddle_width, paddle_height))
    pygame.draw.rect(window, white, (*right_paddle_pos, paddle_width, paddle_height))
    pygame.draw.circle(window, white, ball_pos, ball_radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)