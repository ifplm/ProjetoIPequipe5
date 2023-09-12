import pygame

class Walker():

    def __init__(self, x, y, h, w, v=10, skinColor = (100, 200, 50)):
        self.x = x
        self.y = y
        self.HEIGHT = h
        self.WIDTH = w
        self.Velocity = v
        self.skin = pygame.Surface((self.HEIGHT, self.WIDTH))
        self.skin.fill(skinColor)


    def draw(self, tela):
        tela.blit(self.skin, (self.x, self.y))


    def moveUp(self):
        self.y -= self.Velocity

    def moveDown(self):
        self.y += self.Velocity

    def moveLeft(self):
        self.x -= self.Velocity

    def moveRight(self):
        self.x += self.Velocity