#Imports
import pygame, sys
import random, time
from pygame.locals import *

#Initialzing
pygame.init()

#Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SPEED2 = 3  #The Speed of Coins
SCORE = 0
COINS = 0
COINS2 = 0
N_COINS = 5  # Number of coins to increase enemy speed

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
background = pygame.image.load("AnimatedStreet.png")

#Create a white screen
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


#Create Coins class with method 'move()'
class Coins(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.weight = random.randint(1,
                                     5)  # Assigning random weight to each coin

    def move(self):
        self.rect.move_ip(0, SPEED2)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.speed = SPEED  # Adding self speed parameter
        print(SPEED)

    def move(self):
        global SCORE
        self.rect.move_ip(0, self.speed)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


#Setting up Sprites
C1 = Coins()  #Setting up Coins Sprite
P1 = Player()
E1 = Enemy()

#Creating Sprites Groups
coins = pygame.sprite.Group()  #Creating Coins Sprite Group
coins.add(C1)
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(C1)
all_sprites.add(P1)
all_sprites.add(E1)

#Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#Game Loop
while True:

    #Cycles through all events occuring
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            E1.speed += 0.5
            SPEED2 += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    coins_score = font_small.render(str(COINS), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coins_score, (370, 10))

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    #To be run if collision occurs between Player and Coin
    if pygame.sprite.spritecollideany(P1, coins):
        # pygame.mixer.Sound('').play()
        COINS += C1.weight
        COINS2 += C1.weight
        
        if COINS2>=3:
            SPEED2*=10

        # Increase enemy speed when player earns N coins
        if COINS2 > 10 and COINS != 0:
            E1.speed += 0.5
            SPEED2 += 0.25
            COINS2 = COINS2 % 10

        C1.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        C1.weight = random.randint(1, 5)

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(1)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)