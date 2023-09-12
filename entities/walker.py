import pygame
from pygame.locals import *
import sys
sys.path.append('..')
from constants import *
# from ..constants import *


class Walker(pygame.sprite.Sprite):

    def __init__(self, spriteGroup, x, y, image, w = MOB_WIDTH, h=MOB_HEIGTH, velocity=MOB_VELOCITY):
        
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
     
        self.HEIGHT = h
        self.WIDTH = w
        self.VELOCITY = velocity
     
        self._layer = MOB_LAYER
        
        self.groups = spriteGroup
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = image

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


    def update(self):
        self.rect.y = self.y
        self.rect.x = self.x



    def moveUp(self):
        self.y -= self.VELOCITY

    def moveDown(self):
        self.y += self.VELOCITY

    def moveLeft(self):
        self.x -= self.VELOCITY

    def moveRight(self):
        self.x += self.VELOCITY


    def checkMove(self):
        if pygame.key.get_pressed()[K_w]:
            self.moveUp()
        if pygame.key.get_pressed()[K_s]:
            self.moveDown()
        if pygame.key.get_pressed()[K_a]:
            self.moveLeft()
        if pygame.key.get_pressed()[K_d]:
            self.moveRight()