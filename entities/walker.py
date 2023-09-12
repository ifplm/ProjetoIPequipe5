import pygame
import sys
sys.path.append('..')
from constants import *
# from ..constants import *


class Walker(pygame.sprite.Sprite):

    def __init__(self, spriteGroup, x, y, w = MOB_WIDTH, h=MOB_HEIGTH):
        
        self.x = x*TILE_SIZE
        self.y = y*TILE_SIZE
     
        self.HEIGHT = h
        self.WIDTH = w
     
        self.groups = spriteGroup
        pygame.sprite.Sprite.__init__(self, self.groups)

        self._layer = MOB_LAYER
        self.image = pygame.Surface([self.WIDTH, self.HEIGHT])
        self.image.fill(VERDE)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



    def update(self):
        self.rect.y = self.y
        self.rect.x = self.x


    def moveUp(self):
        self.y -= TILE_SIZE

    def moveDown(self):
        self.y += TILE_SIZE

    def moveLeft(self):
        self.x -= TILE_SIZE

    def moveRight(self):
        self.x += TILE_SIZE
