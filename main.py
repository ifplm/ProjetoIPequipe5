import pygame, random, sys
from pygame.locals import *
from entities.walker import Walker
from entities.enemy import Enemy, Ghost
from entities.map import Block, BackGround, Item, Map
from constants import *
from UI import UI

pygame.init()
pygame.display.set_caption(NOME_JOGO)

pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

TELA = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()


FROG_SPRITE_SHEET = pygame.image.load(FROG_SHEET_DIR).convert_alpha()
FROG_IMG  = FROG_SPRITE_SHEET.subsurface((12, 18), (22, 16)).convert_alpha()
SKELETON_SPRITE_SHEET = pygame.image.load(SKELETON_SHEET_DIR).convert_alpha()
SKELETON_IMG  = SKELETON_SPRITE_SHEET.subsurface((0, 0), (48, 48)).convert_alpha()
GHOST_SPRITE_SHEET = pygame.image.load(GHOST_SHEET_DIR).convert_alpha()
GHOST_IMG  = GHOST_SPRITE_SHEET.subsurface((0, 0), (32, 32)).convert_alpha()


SpriteGroup = pygame.sprite.LayeredUpdates() 
EnemyGroup = pygame.sprite.LayeredUpdates()
Ui = UI(TELA, CLOCK)

#Gera aleatoriamente com essa chance de spawnar e esse limite de mobs
def generateEnemies():
    if random.randint(1, 100) > SPAW_CHANCE:
        return
    if len(EnemyGroup) >= MAX_MOBS:
        return
    
    x = random.randint(SPAW_MIN_DIST, SPAW_MAX_DIST)
    y = random.randint(SPAW_MIN_DIST, SPAW_MAX_DIST)

    if random.randint(0, 1) == 0:
        x *= -1

    if random.randint(0, 1) == 0:
        y *= -1


    if random.randint(0, 100) > GHOST_RARITY:
        Enemy([SpriteGroup, EnemyGroup], BlockGroup, player, x + PLAYER_DEFAULT_X, y + PLAYER_DEFAULT_Y, SKELETON_IMG, velocity=2)
    
    else:
        Ghost([SpriteGroup, EnemyGroup], BlockGroup, player, x + PLAYER_DEFAULT_X, y + PLAYER_DEFAULT_Y, GHOST_IMG, velocity=1.5)

# Realiza as ações do Jogo
def Events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

# Atualiza as infos dos personagens, itens e mapa
def Update():
    if player.vivo:
        player.checkMove()
    else:
        global JOGANDO
        JOGANDO = False

        Ui.GameOver()

    generateEnemies()
    Mapa.checkForUpdates(player.rect.x, player.rect.y)
    SpriteGroup.update()


# Desenha tudo na tela
def Draw():

    TELA.fill((0, 0, 0))
    SpriteGroup.draw(TELA)
    Ui.TelaInGame(player.pontos[1], player.pontos[0], player.pontos[2])
    pygame.display.flip()


# Inicia todos os componentes do jogo
def InitGame():

    SpriteGroup.empty()

    global Mapa
    Mapa = Map(SpriteGroup)

    global BlockGroup
    global BackGroundGroup
    global ItemGroup

    BlockGroup = Mapa.BlockGroup
    BackGroundGroup = Mapa.BackGroundGroup
    ItemGroup = Mapa.ItemGroup
    
    global player
    player = Walker(SpriteGroup, BlockGroup, ItemGroup, EnemyGroup, WIDTH/TILE_SIZE/2, HEIGHT/TILE_SIZE/2, FROG_IMG)
    
    global JOGANDO
    JOGANDO = True


JOGANDO = False

while True:

    if JOGANDO:
        Events()
        Update()
        Draw()

    else:
        pygame.mixer.Sound.stop(SOM_MORREU)
        pygame.mixer.music.play(-1)
        Ui.ShowMenu()
        InitGame()


    CLOCK.tick(FPS) 
