import pygame
import sys
sys.path.append('..')
from constants import *
# from ..constants import *


class SpriteController:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, WIDTH=TILE_SIZE, HEIGHT=TITLE_SZ):
        sprite = pygame.Surface([WIDTH, HEIGHT])
        sprite.blit(self.sheet, (0, 0), (x, y, WIDTH, HEIGHT))

        return sprite
