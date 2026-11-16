# Map editor
# run : python3 -m editor.main maps/test.json
# keys : 1~4 select tile, mouse drag paint, Ctrl+S save

import json
import pygame
import sys
from common.constants import *

TILES = ['.', '#', 'S', 'G'] # buildable, road, spawn, goal
TILE_COLORS = {
    '.' : (70, 120, 60),
    '#' : (170, 140, 90),
    'S' : (200, 60, 60),
    'G' : (60, 100, 210),
}
NEW_MAP_COLS = 20
NEW_MAP_ROWS = 15

path = sys.argv[1]

# load map, or make a new one if the file doesn't exist
# other keys in the json (besides "tiles") are kept as they are
try :
    with open(path) as f :
        map_data = json.load(f)
except FileNotFoundError :
    map_data = {'tiles' : ['.' * NEW_MAP_COLS] * NEW_MAP_ROWS}

grid = [list(row) for row in map_data['tiles']]

rows = len(grid)
cols = len(grid[0])

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((cols * CELL_SIZE, rows * CELL_SIZE + 30))
font = pygame.font.SysFont(None, 24)

selected = '#'

while True :

    # handle event
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN :
            if pygame.K_1 <= event.key <= pygame.K_4 :
                selected = TILES[event.key - pygame.K_1]

            elif event.key == pygame.K_s and event.mod & pygame.KMOD_CTRL :
                map_data['tiles'] = [''.join(row) for row in grid]
                with open(path, 'w') as f :
                    json.dump(map_data, f, indent=2)
                print('saved :', path)

    # paint the tile under the mouse
    if pygame.mouse.get_pressed()[0] :
        mouse_x, mouse_y = pygame.mouse.get_pos()
        x = mouse_x // CELL_SIZE
        y = mouse_y // CELL_SIZE
        if x < cols and y < rows :
            grid[y][x] = selected

    # draw screen
    screen.fill(BLACK)

    for y in range(rows) :
        for x in range(cols) :
            # 1px smaller than the cell, so the black background shows as grid lines
            rect = (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1)
            pygame.draw.rect(screen, TILE_COLORS[grid[y][x]], rect)

    text = font.render('selected : ' + selected + '   (1~4 select, Ctrl+S save)', True, WHITE)
    screen.blit(text, (5, rows * CELL_SIZE + 7))

    pygame.display.flip()

    clock.tick(FPS)
