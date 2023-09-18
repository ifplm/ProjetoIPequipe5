import pygame, random
from pygame.locals import *
from entities.walker import Walker
from entities.enemy import Enemy
from entities.map import Block, BackGround, Item, Map
from constants import *
from UI import UI

pygame.init()
pygame.display.set_caption(NOME_JOGO)

pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

TELA = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()

SpriteGroup = pygame.sprite.LayeredUpdates() 
EnemyGroup = pygame.sprite.LayeredUpdates()

FROG_SPRITE_SHEET = pygame.image.load(FROG_SHEET_DIR).convert_alpha()
MENU_FROG_IMG = pygame.transform.scale(FROG_SPRITE_SHEET.subsurface((0, 0), (48, 48)), (48*2, 48*2))
FROG_IMG  = FROG_SPRITE_SHEET.subsurface((12, 18), (22, 16)).convert_alpha()
SKELETON_SPRITE_SHEET = pygame.image.load(SKELETON_SHEET_DIR).convert_alpha()
SKELETON_IMG  = SKELETON_SPRITE_SHEET.subsurface((0, 0), (48, 48)).convert_alpha()

Mapa = Map(SpriteGroup)
Ui = UI(TELA)

BlockGroup = Mapa.BlockGroup
BackGroundGroup = Mapa.BackGroundGroup
ItemGroup = Mapa.ItemGroup

player = Walker(SpriteGroup, BlockGroup, ItemGroup, EnemyGroup, WIDTH/TILE_SIZE/2, HEIGHT/TILE_SIZE/2, FROG_IMG)

enemy = Enemy([SpriteGroup, EnemyGroup], BlockGroup, player, 10, 10, SKELETON_IMG, velocity=2)

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

        if event.type == pygame.MOUSEBUTTONDOWN:

            if WIDTH/2 <= mouse[0] <= WIDTH/2+140 and HEIGHT/2 <= mouse[1] <= HEIGHT/2+40:  
                pygame.quit()  


        TELA.fill((60, 25, 60))

        mouse = pygame.mouse.get_pos()

        if WIDTH/2 <= mouse[0] <= WIDTH/2+140 and WIDTH/2 <= mouse[1] <= HEIGHT/2+40:  
            pygame.draw.rect(TELA,color_light,[WIDTH/2,HEIGHT/2,140,40])  


JOGANDO = True

# Atualiza as infos dos personagens, itens e mapa
def Update():
    if player.vivo:
        player.checkMove()
    else:
        JOGANDO = False
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


while True:

    if JOGANDO:
        Events()
        Update()
        Draw()

    else:
        Ui.ShowMenu()
        WaitPlayer()
        JOGANDO = True

    CLOCK.tick(FPS)
