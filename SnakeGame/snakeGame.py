import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen configuration
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
GRID_COLOR = (0, 0, 0)
BACKGROUND_COLOR = (0, 0, 0)

# Snake configuration
snake = [(5, 5)]
snake_direction = (1, 0)
snake_speed = 10

# Food configuration
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Score configuration
score = 0

# Window setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Function to draw the snake and food
def draw_objects():
    screen.fill(BACKGROUND_COLOR)
    
    for segment in snake:
        pygame.draw.rect(screen, (0, 128, 0), (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    
    pygame.draw.rect(screen, (255, 0, 0), (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    pygame.display.update()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN:
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT:
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT:
                snake_direction = (1, 0)

    snake_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    snake.insert(0, snake_head)

    if snake_head == food:
        score += 1
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    else:
        snake.pop()

    if (
        snake_head[0] < 0
        or snake_head[0] >= GRID_WIDTH
        or snake_head[1] < 0
        or snake_head[1] >= GRID_HEIGHT
        or snake_head in snake[1:]
    ):
        pygame.quit()
        sys.exit()

    draw_objects()
    pygame.time.delay(1000 // snake_speed)
