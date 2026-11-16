import pygame
import sys
from common.constants import *

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600)) # gamemap select screen

basic_font = pygame.font.SysFont(None, 32)

while True :

    # handle event
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()


        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT :
                pass

    # game logic


    # draw screen
    screen.fill(BLACK)

    text = basic_font.render("hello tower defence", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()

    clock.tick(FPS)