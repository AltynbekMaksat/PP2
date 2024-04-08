import pygame
import random

pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

#paddle
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

#Ball
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2**0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2,
                   ball_rect, ball_rect)
dx, dy = 1, -1

#Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}',
                                          True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

#Catching sound
collision_sound = pygame.mixer.Sound('music/catch.mp3')


def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy


#block settings

# Define the original block list with 'normal' blocks
block_list = [(pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50), 'normal')
              for i in range(10) for j in range(4)]

# Assign random colors to all blocks
color_list = [(random.randrange(0, 255), random.randrange(0, 1),
               random.randrange(0, 255)) for _ in range(len(block_list))]

# Define the number of unbreakable and bonus bricks
num_unbreakable_bricks = 10
num_bonus_bricks = 5

# Randomly select and replace 'normal' bricks with 'unbreakable' bricks
for _ in range(num_unbreakable_bricks):
    index = random.randint(0, len(block_list) - 1)
    block_list[index] = (block_list[index][0], 'unbreakable')

# Randomly select and replace 'normal' bricks with 'bonus' bricks
for _ in range(num_bonus_bricks):
    index = random.randint(0, len(block_list) - 1)
    block_list[index] = (block_list[index][0], 'bonus')

print(block_list)

# Increase the speed of the ball with time
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Shrink the paddle with time
SHRINK_PADDLE = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 10000)

#Game over Screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

#Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

# Variable to track if the game is paused
paused = False

# Function to display the pause menu
# def show_pause_menu():
#     pause_font = pygame.font.SysFont('comicsansms', 40)
#     pause_text = pause_font.render('Paused', True, (255, 255, 255))
#     pause_text_rect = pause_text.get_rect()
#     pause_text_rect.center = (W // 2, H // 2)
#     screen.blit(pause_text, pause_text_rect)
#     pygame.display.flip()


# Function to handle settings menu
def handle_settings():
    global paused, ballSpeed, paddleW, done

    settings_font = pygame.font.SysFont('comicsansms', 30)
    speed_text_rect = settings_font.render(
        f'Ball Speed: {ballSpeed}', True,
        (255, 255, 255)).get_rect(center=(W // 2, H // 2 + 100))
    paddle_text_rect = settings_font.render(
        f'Paddle Size: {paddleW}', True,
        (255, 255, 255)).get_rect(center=(W // 2, H // 2 + 50))

    while True:
        screen.fill(bg)

        # Display pause text
        if paused:
            pause_text = settings_font.render('PAUSED', True, (255, 255, 255))
            pause_text_rect = pause_text.get_rect(center=(W // 2, H // 2))
            screen.blit(pause_text, pause_text_rect)

        # Display settings menu
        screen.blit(
            settings_font.render(f'Ball Speed: {ballSpeed}', True,
                                 (255, 255, 255)), speed_text_rect)
        screen.blit(
            settings_font.render(f'Paddle Size: {paddleW}', True,
                                 (255, 255, 255)), paddle_text_rect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False
                    return
                elif event.key == pygame.K_UP:
                    # Increase ball speed
                    ballSpeed += 1

                elif event.key == pygame.K_DOWN:
                    # Decrease ball speed (ensure it doesn't go below 1)
                    ballSpeed = max(1, ballSpeed - 1)
                elif event.key == pygame.K_LEFT:
                    # Decrease paddle size (ensure it doesn't go below minimum)
                    paddleW = max(50, paddleW - 10)
                    paddle.width = paddleW
                elif event.key == pygame.K_RIGHT:
                    # Increase paddle size
                    paddleW = min(W, paddleW + 10)
                    paddle.width = paddleW
                elif event.key == pygame.K_RETURN:
                    # Return to the game
                    paused = False
                    return


# Main game loop
while not done:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            ballSpeed += 0.5
        if event.type == SHRINK_PADDLE:
            if paddleW > 50:  # Minimum paddle width
                paddleW -= 5
                paddle.width = paddleW
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Toggle pause
                paused = not paused

    screen.fill(bg)

    if paused:
        # show_pause_menu()
        handle_settings()  # Handle settings even when paused
        pygame.display.flip()
        continue

    # print(next(enumerate(block_list)))

    for color, (brick_rect, brick_type) in enumerate(block_list):
        if brick_type == 'normal':
            pygame.draw.rect(screen, color_list[color], brick_rect)
        elif brick_type == 'unbreakable':
            pygame.draw.rect(screen, (255, 255, 255),
                             brick_rect)  # Color for unbreakable bricks
        elif brick_type == 'bonus':
            pygame.draw.rect(screen, (0, 255, 0),
                             brick_rect)  # Color for bonus bricks

    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center,
                       ballRadius)
    # print(next(enumerate (block_list)))

    #Ball movement
    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    #Collision left
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    #Collision top
    if ball.centery < ballRadius + 50:
        dy = -dy
    #Collision with paddle
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    #Collision blocks
    hitIndex = next((i for i, (block_rect, _) in enumerate(block_list)
                     if ball.colliderect(block_rect)), -1)

    if hitIndex != -1:
        hitRect, hitType = block_list[hitIndex]
        hitColor = color_list[hitIndex]
        if hitType == 'normal':
            dx, dy = detect_collision(dx, dy, ball, hitRect)
            game_score += 1
            del block_list[hitIndex]
            del color_list[hitIndex]
            collision_sound.play()
        elif hitType == 'bonus':
            dx, dy = detect_collision(dx, dy, ball, hitRect)
            game_score += 5
            del block_list[hitIndex]
            del color_list[hitIndex]
            collision_sound.play()
        elif hitType == 'unbreakable':
            dx, dy = detect_collision(dx, dy, ball, hitRect)

    #Game score
    game_score_text = game_score_fonts.render(
        f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)

    #Win/lose screens
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not len(block_list):
        screen.fill((255, 255, 255))
        screen.blit(wintext, wintextRect)
    # print(pygame.K_LEFT)
    #Paddle Control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed

    pygame.display.flip()
    clock.tick(FPS)