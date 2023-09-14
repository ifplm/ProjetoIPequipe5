import pygame, random, math
from pygame.locals import *
import sys
sys.path.append('..')
from constants import *
# from ..constants import *


WALL_SPRITE_SHEET = pygame.image.load(WALL_SHEET_DIR)
GRASS_SPRITE_SHEET = pygame.image.load(GRASS_SHEET_DIR)

AVLC_IMG = pygame.image.load(AVLC_DIR)
MD_IMG = pygame.image.load(MD_DIR)
CALC_IMG = pygame.image.load(CALC_DIR)

WALL1_IMG = WALL_SPRITE_SHEET.subsurface((TILE_SIZE*2, TILE_SIZE*4), (TILE_SIZE, TILE_SIZE))

GRASS_IMGS = []
for i in range(5):
    for j in range(8):
        GRASS_IMGS.append(GRASS_SPRITE_SHEET.subsurface((TILE_SIZE*i, TILE_SIZE*j), (TILE_SIZE, TILE_SIZE)))



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


class Item(pygame.sprite.Sprite):
    
    def __init__(self, spriteGroups, x, y, image, id):

        self.id = id

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


class Map:

    def __init__(self, SpriteGroup):

        self.map = {}

        self.SpriteGroup = SpriteGroup
        self.BlockGroup = pygame.sprite.LayeredUpdates() 
        self.ItemGroup = pygame.sprite.LayeredUpdates() 
        self.BackGroundGroup = pygame.sprite.LayeredUpdates() 

        self.anchor = BackGround([self.SpriteGroup, self.BackGroundGroup], 0, 0, GRASS_IMGS[0])
        self.map[(0, 0)] = INITIAL_MAP

        self.CreateMap(0, 0)
        self.checkForUpdates(0, 0)


    # Coloca os objetos no mapa
    def CreateMap(self, Chunk_X, Chunk_Y):

        delta_x = (Chunk_X * CHUNK_SIZE + (self.anchor.rect.x / TILE_SIZE))
        delta_y = (Chunk_Y * CHUNK_SIZE + (self.anchor.rect.y / TILE_SIZE))

        print(Chunk_X, Chunk_Y)
        print(delta_x, delta_y)
        print()

        for i, linha in enumerate(self.map[(Chunk_X, Chunk_Y)]):
            for j, b in enumerate(linha):
                if b == "W":
                    Block([self.SpriteGroup, self.BlockGroup], j+delta_x, i+delta_y, WALL1_IMG)
                if b == "A":
                    Item([self.SpriteGroup, self.ItemGroup], j+delta_x, i+delta_y, AVLC_IMG, 0)
                if b == "M":
                    Item([self.SpriteGroup, self.ItemGroup], j+delta_x, i+delta_y, MD_IMG, 1)
                if b == "C":
                    Item([self.SpriteGroup, self.ItemGroup], j+delta_x, i+delta_y, CALC_IMG, 2)

        for i in range(CHUNK_SIZE):
            for j in range(CHUNK_SIZE):
                BackGround([self.SpriteGroup, self.BackGroundGroup], j+delta_x, i+delta_y, GRASS_IMGS[random.randint(0, len(GRASS_IMGS)-16)])
    

    # Cria um novo chunk randômico
    def GenerateChunk(self, Chunk_X, Chunk_Y):

        if (Chunk_X, Chunk_Y) in self.map:
            return

        self.map[(Chunk_X, Chunk_Y)] = MARKER_MAP

        self.CreateMap(Chunk_X, Chunk_Y)


    #verifica se é preciso atualizar os chunks pra o jogador não cair no vazio
    def checkForUpdates(self, player_x, player_y):

        ax = -int((self.anchor.rect.x - player_x)/TILE_SIZE)
        ay = -int((self.anchor.rect.y - player_y)/TILE_SIZE)

        Chunk_X = math.ceil(ax / CHUNK_SIZE) - 1
        Chunk_Y = math.ceil(ay / CHUNK_SIZE) - 1

        self.GenerateChunk(Chunk_X+1, Chunk_Y)
        self.GenerateChunk(Chunk_X-1, Chunk_Y)
        self.GenerateChunk(Chunk_X, Chunk_Y+1)
        self.GenerateChunk(Chunk_X, Chunk_Y-1)

        self.GenerateChunk(Chunk_X+1, Chunk_Y+1)
        self.GenerateChunk(Chunk_X+1, Chunk_Y-1)
        self.GenerateChunk(Chunk_X-1, Chunk_Y+1)
        self.GenerateChunk(Chunk_X-1, Chunk_Y-1)
