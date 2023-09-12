import pygame, random
from pygame.locals import *
from entities.walker import Walker
# from entities.player import Player
from constants import *


pygame.init()
pygame.display.set_caption(NOME_JOGO)

TELA = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
FONTE = pygame.font.match_font(FONTE_NAME)
SpriteGroup = pygame.sprite.LayeredUpdates() 
SPRITE_SHEET = pygame.image.load(SHEET_DIR)
FROG_IMG = pygame.transform.scale(SPRITE_SHEET.subsurface((0, 0), (48, 48)), (48*2, 48*2))

player = Walker(SpriteGroup, 20, 20)


# Realiza as ações do Jogo
def Events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

            if event.type == KEYDOWN:
                if event.key == K_a:
                    player.moveLeft()
                elif event.key == K_d:
                    player.moveRight()
                elif event.key == K_w:
                    player.moveUp()
                elif event.key == K_s:
                    player.moveDown()



# Atualiza as infos dos personagens, itens e mapa
def Update():

    if pygame.key.get_pressed()[K_w]:
        player.moveUp()
        print("up")
    if pygame.key.get_pressed()[K_s]:
        player.moveDown()
        print("down")
    if pygame.key.get_pressed()[K_a]:
        player.moveLeft()
    if pygame.key.get_pressed()[K_d]:
        player.moveRight()


    SpriteGroup.update()


def WaitPlayer():
    waiting = True
    while waiting:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYUP:
                waiting = False


# Desenha tudo na tela
def Draw():
    TELA.fill((0, 0, 0))
    SpriteGroup.draw(TELA)
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

    frg_rect = FROG_IMG.get_rect()
    frg_rect.center = (WIDTH/2, 2*HEIGHT/3)
    TELA.blit(FROG_IMG, frg_rect)

    pygame.display.flip()

    WaitPlayer()




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





