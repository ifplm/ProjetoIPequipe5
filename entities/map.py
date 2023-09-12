import pygame
from pygame.locals import *
import sys
sys.path.append('..')
from constants import *
# from ..constants import *


class Block(pygame.sprite.Sprite):
    def __init__(self, spriteGroups, x, y, image):

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
     
        self.HEIGHT = TILE_SIZE
        self.WIDTH = TILE_SIZE

        self._layer = BLOCK_LAYER

        self.groups = spriteGroups
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = image

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class BackGround(pygame.sprite.Sprite):
    
    def __init__(self, spriteGroups, x, y, image):

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
     
        self.HEIGHT = TILE_SIZE
        self.WIDTH = TILE_SIZE

        self._layer = BACK_GROUND_LAYER

        self.groups = spriteGroups
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = image

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y