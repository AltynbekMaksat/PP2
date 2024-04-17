import pygame , sys

pygame.init()

w,h = 300 , 700 
screen = pygame.display.set_mode((w,h))


pygame.display.set_caption("MAX")


black = (0,0,0)
white = (255,255,255)

font = pygame.font.SysFont("Verdana",60)
game  = font.render("Game_over" , True, black)

game_rect = game.get_rect()
game_rect.center = (w/2,h/2)

screen.blit(white)

run = True
while run:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()

    