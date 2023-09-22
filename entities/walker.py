import pygame
from pygame.locals import *
import sys
sys.path.append('..')
from constants import *
# from ..constants import *


class Walker(pygame.sprite.Sprite):

    def __init__(self, spriteGroup, colliders, ItemColliders, enemyCollider, x, y, image, w = MOB_WIDTH, h=MOB_HEIGTH, velocity=MOB_VELOCITY):
        
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.vivo = True
        self.HEIGHT = h
        self.WIDTH = w
        self.VELOCITY = velocity
        self.enemyCollider = enemyCollider
        self._layer = MOB_LAYER
        
        self.groups = spriteGroup
        self.colliders = colliders
        self.ItemColliders = ItemColliders
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

        self.rect.x += self.delta_x
        self.collider('x')
        self.rect.y += self.delta_y
        self.collider('y')
        self.collider_enemy()
        self.colliderItem()

        self.delta_x = 0
        self.delta_y = 0


    def moveUp(self):
        self.delta_y -= self.VELOCITY
        self.y -= self.VELOCITY

        for sprite in self.groups:
            sprite.rect.y += self.VELOCITY

    def moveDown(self):
        self.delta_y += self.VELOCITY
        self.y += self.VELOCITY

        for sprite in self.groups:
            sprite.rect.y -= self.VELOCITY

    def moveLeft(self):
        self.delta_x -= self.VELOCITY
        self.x -= self.VELOCITY

        for sprite in self.groups:
            sprite.rect.x += self.VELOCITY

        if self.facing != 0:
            self.image = pygame.transform.flip(self.image, True, False)
        self.facing = 0

    def moveRight(self):
        self.delta_x += self.VELOCITY
        self.x += self.VELOCITY

        for sprite in self.groups:
            sprite.rect.x -= self.VELOCITY

        if self.facing != 1:
            self.image = pygame.transform.flip(self.image, True, False)
        self.facing = 1


    def checkMove(self):
        if pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP]:
            self.moveUp()
        if pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN]:
            self.moveDown()
        if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT]:
            self.moveLeft()
        if pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT]:
            self.moveRight()


    def colliderItem(self):
        hits = pygame.sprite.spritecollide(self, self.ItemColliders, False)

        if hits:
            self.pontos[hits[0].id] += 1
            hits[0].kill()
            #som_da_colisao = pygame.mixer.Sound('som_da_colisao.wav')
            SOM_DA_COLISAO.play()
            SOM_DA_COLISAO.set_volume(1)

    def collider_enemy(self):
        hits = pygame.sprite.spritecollide(self, self.enemyCollider, False)

        if hits:
            hits[0].kill()
            self.kill()
            self.vivo = False
            pygame.mixer.music.stop()
            SOM_MORREU.play()
            SOM_MORREU.set_volume(1)

    def collider(self, dir):
        hits = pygame.sprite.spritecollide(self, self.colliders, False)

        if hits:

            if dir == 'x':
                if self.delta_x > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                    self.x += self.VELOCITY
                    for sprite in self.groups:
                        sprite.rect.x += self.VELOCITY
                if self.delta_x < 0:
                    self.rect.x = hits[0].rect.right
                    self.x -= self.VELOCITY
                    for sprite in self.groups:
                        sprite.rect.x -= self.VELOCITY

            elif dir == 'y':
                if self.delta_y > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    self.y += self.VELOCITY
                    for sprite in self.groups:
                        sprite.rect.y += self.VELOCITY
                if self.delta_y < 0:
                    self.rect.y = hits[0].rect.bottom
                    self.y -= self.VELOCITY
                    for sprite in self.groups:
                        sprite.rect.y -= self.VELOCITY

    def Alive(self):
        self.vivo = True