import pygame

class Entity():

    def __init__(self, x, y, h, w, v=10, skinColor = (100, 200, 50)):
        self.x = x
        self.y = y
        self.HEIGHT = h
        self.WIDTH = w
        self.Velocity = v
        self.skin = pygame.Surface((self.HEIGHT, self.WIDTH))
        self.skin.fill(skinColor)


    def draw(tela):
        tela.blit(self.skin, (self.x, self.y))

    def Teste():
        print("sla")

    def moveUp():
        self.y -= self.Velocity

    def moveDown():
        self.y += self.Velocity

    def moveLeft():
        self.x -= self.Velocity

    def moveRight():
        self.x += self.Velocity