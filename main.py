import pygame, random
from pygame.locals import *
from entities.walker import Walker
from entities.map import Block, BackGround, Item, Map
from constants import *


pygame.init()
pygame.display.set_caption(NOME_JOGO)

TELA = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
FONTE = pygame.font.match_font(FONTE_NAME)
SpriteGroup = pygame.sprite.LayeredUpdates() 


FROG_SPRITE_SHEET = pygame.image.load(FROG_SHEET_DIR).convert_alpha()
MENU_FROG_IMG = pygame.transform.scale(FROG_SPRITE_SHEET.subsurface((0, 0), (48, 48)), (48*2, 48*2))
FROG_IMG  = FROG_SPRITE_SHEET.subsurface((12, 18), (22, 16)).convert_alpha()



Mapa = Map(SpriteGroup)

BlockGroup = Mapa.BlockGroup
BackGroundGroup = Mapa.BackGroundGroup
ItemGroup = Mapa.ItemGroup

player = Walker(SpriteGroup, BlockGroup, ItemGroup, WIDTH/TILE_SIZE/2, HEIGHT/TILE_SIZE/2, FROG_IMG)


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
    Mapa.checkForUpdates(player.rect.x, player.rect.y)
    SpriteGroup.update()


# Desenha tudo na tela
def Draw():

    TELA.fill((0, 0, 0))
    SpriteGroup.draw(TELA)

    Write(f"COLETADOS:", WIDTH/2, 3*HEIGHT/4)
    Write(f"MD: {player.pontos[1]}", WIDTH/2, HEIGHT/2+HEIGHT/3)
    Write(f"AVLC: {player.pontos[0]}", WIDTH/2, HEIGHT/2+HEIGHT/3 + FONTE_SZ)
    Write(f"CALC: {player.pontos[2]}", WIDTH/2, HEIGHT/2+HEIGHT/3 + FONTE_SZ + FONTE_SZ)
    
    pygame.display.flip()


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




BackGroundGroup.draw(TELA)
ShowMenu()


JOGANDO = True

while True:

    if JOGANDO:
        Events()
        Update()
        Draw()

    else :
        ShowMenu()

    CLOCK.tick(FPS)
