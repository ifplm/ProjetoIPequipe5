import pygame, random
from pygame.locals import *
from entities.walker import Walker
from constants import *


pygame.init()
pygame.display.set_caption(NOME_JOGO)

TELA = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
FONTE = pygame.font.match_font(FONTE_NAME)
SpriteGroup = pygame.sprite.Group() 
SPRITE_SHEET = pygame.image.load(SHEET_DIR)
FROG_IMG = pygame.transform.scale(SPRITE_SHEET.subsurface((0, 0), (48, 48)), (48*2, 48*2))



# Realiza as ações do Jogo
def Events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()



# Atualiza as infos dos personagens, itens e mapa
def Update():
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

    CLOCK.tick(FPS)

    if JOGANDO:
        Events()
        Update()
        Draw()

    else :
        ShowMenu()





# if pygame.key.get_pressed()[K_w]:
#     jogador.moveUp()
# if pygame.key.get_pressed()[K_s]:
#     jogador.moveDown()
# if pygame.key.get_pressed()[K_a]:
#     jogador.moveLeft()
# if pygame.key.get_pressed()[K_d]:
#     jogador.moveRight()