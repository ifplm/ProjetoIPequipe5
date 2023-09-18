import pygame
from pygame.locals import *
import sys
sys.path.append('..')
from constants import *

class Enemy(pygame.sprite.Sprite):

    def __init__(self, spriteGroup, colliders, player, x, y, image, w = MOB_WIDTH, h=MOB_HEIGTH, velocity=MOB_VELOCITY):
        
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.player = player
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
        # direção que o sapo está olhando | 1 - Right | 0 - Left |

        self.pontos = [0, 0, 0]


    def update(self):

        if self.player.rect.x > self.rect.x:
            self.moveRight()
        if self.player.rect.x < self.rect.x:
            self.moveLeft()
        if self.player.rect.y > self.rect.y:
            self.moveDown()
        if self.player.rect.y < self.rect.y:
            self.moveUp()
        self.rect.x += self.delta_x
        self.collider('x')
        self.rect.y += self.delta_y
        self.collider('y')

        self.delta_x = 0
        self.delta_y = 0

    def moveUp(self):
        self.delta_y -= self.VELOCITY
        self.y -= self.VELOCITY

    def moveDown(self):
        self.delta_y += self.VELOCITY
        self.y += self.VELOCITY

    def moveLeft(self):
        self.delta_x -= self.VELOCITY
        self.x -= self.VELOCITY

        if self.facing != 0:
            self.image = pygame.transform.flip(self.image, True, False)
        self.facing = 0

    def moveRight(self):
        self.delta_x += self.VELOCITY
        self.x += self.VELOCITY

        if self.facing != 1:
            self.image = pygame.transform.flip(self.image, True, False)
        self.facing = 1

    def collider(self, dir):
        hits = pygame.sprite.spritecollide(self, self.colliders, False)

        if hits:

            if dir == 'x':
                if self.delta_x > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                    self.x += self.VELOCITY
                if self.delta_x < 0:
                    self.rect.x = hits[0].rect.right
                    self.x -= self.VELOCITY

            elif dir == 'y':
                if self.delta_y > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    self.y += self.VELOCITY
                if self.delta_y < 0:
                    self.rect.y = hits[0].rect.bottom
                    self.y -= self.VELOCITY