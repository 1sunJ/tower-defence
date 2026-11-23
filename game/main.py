import pygame
import sys
import common.gamemap_loader as gamemap_loader
from common.constants import *

WIDTH, HEIGHT = 600, 400

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # gamemap select screen
map_surface = None

basic_font = pygame.font.SysFont(None, 32)

state = SELECTION # SELECTION | PLAYING

# selection
selected_index = 0
gamemap_names = gamemap_loader.get_gamemap_names()

# playing
name, start_gold, lives, tiles = None, None, None, None
header_rect, map_rect, panel_rect = None, None, None
towers = {}

while True :

    # [ Handle event ]
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN :
            # selection event
            if state == SELECTION :
                if event.key == pygame.K_UP :
                    selected_index = (selected_index - 1) % len(gamemap_names)
                elif event.key == pygame.K_DOWN :
                    selected_index = (selected_index + 1) % len(gamemap_names)
                elif event.key == pygame.K_RETURN :
                    state = PLAYING
                    name = gamemap_names[selected_index]
                    name, start_gold, lives, tiles = gamemap_loader.load_gamemap(name)

                    map_w = len(tiles[0]) * CELL_SIZE
                    map_h = len(tiles) * CELL_SIZE
                    screen = pygame.display.set_mode((map_w, HEADER_HEIGHT + map_h + PANEL_HEIGHT))

                    header_rect = pygame.Rect(0, 0, map_w, HEADER_HEIGHT)
                    map_rect    = pygame.Rect(0, header_rect.bottom, map_w, map_h)
                    panel_rect  = pygame.Rect(0, map_rect.bottom, map_w, PANEL_HEIGHT)
                    map_surface = screen.subsurface(map_rect)
                
            # playing event
            elif state == PLAYING :
                pass

    # [ Game logic ]

    # [ Draw screen ]
    screen.fill(BLACK)

    # selection screen
    if state == SELECTION :
        for i, name in enumerate(gamemap_names) :
            if i == selected_index :
                color = YELLOW
            else : 
                color = WHITE

            text = basic_font.render(name, False, color)
            text_rect = text.get_rect(center = (WIDTH // 2, 100 + i * 64))
            screen.blit(text, text_rect)

    # playing screen
    if state == PLAYING :
        # header
        pygame.draw.rect(screen, GRAY, header_rect)

        # map
        pygame.draw.rect(screen, BLACK, map_rect)
        n, m = len(tiles), len(tiles[0])
        for i in range(n) :
            for j in range(m) :
                rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                if tiles[i][j] == 'S' :
                    pygame.draw.rect(map_surface, BLUE, rect)
                elif tiles[i][j] == 'G' :
                    pygame.draw.rect(map_surface, RED, rect)
                elif tiles[i][j] == '#' :
                    pygame.draw.rect(map_surface, YELLOW, rect)
                else : # '.'
                    pygame.draw.rect(map_surface, WHITE, rect)

        # panel
        pygame.draw.rect(screen, GRAY, panel_rect)

    pygame.display.flip()

    clock.tick(FPS)