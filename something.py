import sys
import pygame

# Initialize Pygame
pygame.init()

# Define colors
fill_color = (0, 255, 255)
ball_color = (255, 0, 0)

# Set up the display
pygame.display.set_caption("MAX")
pygame.display.set_icon(pygame.image.load("Enemy.png"))
size = (320, 320)
screen = pygame.display.set_mode(size)

# Load the background image
background_image = pygame.image.load("Enemy.png").convert()
pygame.transform.scale(background_image, (300,300))

# Set up variables
XC = 160
YC = 160
fps = 30
clock = pygame.time.Clock()
running = True

# Main loop
while running:
    screen.fill(fill_color)  # Fill the screen with the fill color
    screen.blit(background_image, (0, 0))  # Blit the background image onto the screen

    # Draw the circle
    pygame.draw.circle(screen, ball_color, (XC, YC), 20)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP and YC > 20:
                YC -= 20
            elif event.key == pygame.K_DOWN and YC < 300:
                YC += 20
            elif event.key == pygame.K_RIGHT and XC < 300:
                XC += 20
            elif event.key == pygame.K_LEFT and XC > 20:
                XC -= 20

    pygame.display.flip()  # Update the display
    clock.tick(fps)  # Cap the frame rate

pygame.quit()
sys.exit()

