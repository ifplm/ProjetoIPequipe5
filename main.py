import pygame, random
from pygame.locals import *
from entities.walker import Walker
from entities.map import Block, BackGround, Item, Map
from UI import UI
from constants import *


pygame.init()
pygame.display.set_caption(NOME_JOGO)

musica_de_fundo = pygame.mixer.music.load('musica_de_fundo.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

TELA = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()

SpriteGroup = pygame.sprite.LayeredUpdates() 


FROG_SPRITE_SHEET = pygame.image.load(FROG_SHEET_DIR).convert_alpha()
MENU_FROG_IMG = pygame.transform.scale(FROG_SPRITE_SHEET.subsurface((0, 0), (48, 48)), (48*2, 48*2))
FROG_IMG  = FROG_SPRITE_SHEET.subsurface((12, 18), (22, 16)).convert_alpha()



Mapa = Map(SpriteGroup)
Ui = UI(TELA)

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
    Ui.telaInGame(player.pontos[1], player.pontos[0], player.pontos[2])
    pygame.display.flip()


BackGroundGroup.draw(TELA)

Ui.ShowMenu()
WaitPlayer()


JOGANDO = True

while True:

    if JOGANDO:
        Events()
        Update()
        Draw()

    else :
        Ui.ShowMenu()

    CLOCK.tick(FPS)
