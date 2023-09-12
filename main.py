import pygame, random
from pygame.locals import *
from entities.walker import Walker
from entities.map import Block
from entities.map import BackGround
# from entities.player import Player
from constants import *


pygame.init()
pygame.display.set_caption(NOME_JOGO)

TELA = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
FONTE = pygame.font.match_font(FONTE_NAME)
SpriteGroup = pygame.sprite.LayeredUpdates() 
BlockGroup = pygame.sprite.LayeredUpdates() 
BackGroundGroup = pygame.sprite.LayeredUpdates() 

FROG_SPRITE_SHEET = pygame.image.load(FROG_SHEET_DIR).convert_alpha()
WALL_SPRITE_SHEET = pygame.image.load(WALL_SHEET_DIR).convert_alpha()
GRASS_SPRITE_SHEET = pygame.image.load(GRASS_SHEET_DIR).convert_alpha()

MENU_FROG_IMG = pygame.transform.scale(FROG_SPRITE_SHEET.subsurface((0, 0), (48, 48)), (48*2, 48*2))
FROG_IMG  = FROG_SPRITE_SHEET.subsurface((0, 0), (48, 48)).convert_alpha()
WALL1_IMG = WALL_SPRITE_SHEET.subsurface((TILE_SIZE*2, TILE_SIZE*3), (TILE_SIZE, TILE_SIZE))

GRASS_IMGS = []
for i in range(8):
    for j in range(4):
        GRASS_IMGS.append(GRASS_SPRITE_SHEET.subsurface((TILE_SIZE*i, TILE_SIZE*j), (TILE_SIZE, TILE_SIZE)))


player = Walker(SpriteGroup, 2, 2, FROG_IMG)



def WaitPlayer():
    waiting = True
    while waiting:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYUP:
                waiting = False


# Realiza as ações do Jogo
def Events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()


# Atualiza as infos dos personagens, itens e mapa
def Update():
    player.checkMove()
    SpriteGroup.update()


# Desenha tudo na tela
def Draw():
    TELA.fill((0, 0, 0))
    SpriteGroup.draw(TELA)
    pygame.display.flip()


def CreateMap():
    for i, linha in enumerate(TILE_MAP):
        for j, b in enumerate(linha):
            if b == "W":
                Block([SpriteGroup, BlockGroup], j, i, WALL1_IMG)
            
            BackGround([SpriteGroup, BackGroundGroup], j, i, GRASS_IMGS[random.randint(0, len(GRASS_IMGS)-1)])


def Write(text, x, y, size=FONTE_SZ, color=BRANCO):
    fonte = pygame.font.Font(FONTE, size)
    txt = fonte.render(text, True, color)
    txt_rect = txt.get_rect()
    txt_rect.midtop = (x, y)
    TELA.blit(txt, txt_rect)


def ShowMenu():

    Write(NOME_JOGO, WIDTH/2, HEIGHT/3, TITLE_SZ, VERDE)
    Write("Pressione Qualquer Tecla para Jogar...", WIDTH/2, HEIGHT/2+HEIGHT/3)

    frg_rect = MENU_FROG_IMG.get_rect()
    frg_rect.center = (WIDTH/2, 2*HEIGHT/3)
    TELA.blit(MENU_FROG_IMG, frg_rect)

    pygame.display.flip()

    WaitPlayer()




ShowMenu()

CreateMap()

JOGANDO = True

while True:

    if JOGANDO:
        Events()
        Update()
        Draw()

    else :
        ShowMenu()

    CLOCK.tick(FPS)





