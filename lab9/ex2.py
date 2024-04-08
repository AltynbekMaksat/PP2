import pygame
from random import randrange, choices
import time  # Import time module for timer

Res = 600
size = 25
score = 0
speed = 5

# Define different types of food with weights
foods = [(randrange(0, Res, size), randrange(0, Res, size)) for _ in range(10)]
food_weights = [0.6, 0.3, 0.1]  # Adjust probabilities as per your choice
food_types = ['apple', 'banana', 'cherry']

length = 1
snake = [(randrange(0, Res, size), randrange(0, Res, size))]
dx, dy = 0, 0
FPS = 10

pygame.init()
sc = pygame.display.set_mode([Res, Res])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 50, bold=True)

# Timer variables for food disappearance
food_timer = time.time()
food_duration = 5  # Food disappears after 5 seconds

while True:
    sc.fill(pygame.Color('black'))
    [(pygame.draw.rect(sc, pygame.Color('green'), (i, j, size, size))) for i, j in snake]
    
    # Check if food needs to disappear
    if time.time() - food_timer >= food_duration:
        foods.pop(0)  # Remove the first food item
        food_timer = time.time()  # Reset timer
    for food in foods:
        pygame.draw.rect(sc, pygame.Color('red'), (*food, size, size))
    
    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
    sc.blit(render_score, (5, 5))

    x += dx * size
    y += dy * size
    snake.append((x, y))
    snake = snake[-length:]

    # Check if snake eats food
    for food in foods:
        if snake[-1] == food:
            foods.remove(food)
            score += 1
            length += 1
            FPS += 1

    if x < 0 or x > Res - size or y < 0 or y > Res - size or len(snake) != len(set(snake)):
        while True:
            render_end = font_end.render('GAME OVER', 1, pygame.Color('orange'))
            sc.blit(render_end, (Res // 2 - 150, Res // 3))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    pygame.display.flip()
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        dx, dy = 0, -1
    if key[pygame.K_DOWN]:
        dx, dy = 0, 1
    if key[pygame.K_LEFT]:
        dx, dy = -1, 0
    if key[pygame.K_RIGHT]:
        dx, dy = 1, 0
