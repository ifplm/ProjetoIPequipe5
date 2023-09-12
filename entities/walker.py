import pygame
from pygame.locals import *
import sys
sys.path.append('..')
from constants import *
# from ..constants import *


class Walker(pygame.sprite.Sprite):

    def __init__(self, spriteGroup, colliders, x, y, image, w = MOB_WIDTH, h=MOB_HEIGTH, velocity=MOB_VELOCITY):
        
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
     
        self.HEIGHT = h
        self.WIDTH = w
        self.VELOCITY = velocity
     
        self._layer = MOB_LAYER
        
        self.groups = spriteGroup
        self.colliders = colliders
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = image

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


        self.delta_x = 0
        self.delta_y = 0

        self.facing = 1
        # direção que o sapo está olhando | 1 - Right | 2 - Left |


    def update(self):

        self.rect.x += self.delta_x
        self.collider('x')
        self.rect.y += self.delta_y
        self.collider('y')

        self.delta_x = 0
        self.delta_y = 0



    def moveUp(self):
        self.delta_y -= self.VELOCITY
    def moveDown(self):
        self.delta_y += self.VELOCITY
    def moveLeft(self):
        self.delta_x -= self.VELOCITY
    def moveRight(self):
        self.delta_x += self.VELOCITY



    def checkMove(self):
        if pygame.key.get_pressed()[K_w]:
            self.moveUp()
        if pygame.key.get_pressed()[K_s]:
            self.moveDown()
        if pygame.key.get_pressed()[K_a]:
            self.moveLeft()
        if pygame.key.get_pressed()[K_d]:
            self.moveRight()



    def collider(self, dir):
        hits = pygame.sprite.spritecollide(self, self.colliders, False)

        if hits:

            if dir == 'x':
                if self.delta_x > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.delta_x < 0:
                    self.rect.x = hits[0].rect.right

            elif dir == 'y':
                if self.delta_y > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.delta_y < 0:
                    self.rect.y = hits[0].rect.bottom