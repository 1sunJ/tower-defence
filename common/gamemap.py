import pygame
from common.constants import *

class Map :
    def __init__(self, name, start_gold, lives, tiles) :
        self.name = name
        self.start_gold = start_gold
        self.lives = lives
        self.tiles = tiles

class Tile :
    color = GRAY

    def __init__(self, row, col) :
        self.row = row
        self.col = col

    def draw(self, surface) :
        rect = pygame.Rect(self.col * CELL_SIZE, self.row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(surface, self.color, rect)

class RoadTile(Tile) :
    color = YELLOW

class BuildableTile(Tile) :
    color = GREEN

class SpawnTile(RoadTile) :
    color = BLUE

class GoalTile(RoadTile) :
    color = RED
