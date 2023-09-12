import pygame as pg
from pygame.locals import *
from sys import exit
from random import randint

pg.init()

largura = 640
altura = 480
x = largura/2
y = altura/2

x_azul = randint(40, 600)
y_azul = randint(50, 430)

fonte = pg.font.SysFont('Times New Roman', 40, True, True)

tela = pg.display.set_mode((largura, altura))
pg.display.set_caption('Jogo')
relogio = pg.time.Clock()

pontos = 0

while True:

    
    relogio.tick(30)
    tela.fill((0, 0, 0))
    mensagem = f'Pontos:{pontos}'
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            exit()
        ... 
        if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 20
            
            elif event.key == K_d:
                x = x + 20

            elif event.key == K_w:
                y = y - 20

            elif event.key == K_s:
                y = y + 20

    if pg.key.get_pressed()[K_a]:
        x = x - 20

    if pg.key.get_pressed()[K_d]:
        x = x + 20

    if pg.key.get_pressed()[K_w]:
        y = y - 20 

    if pg.key.get_pressed()[K_s]:
        y = y + 20

    ret_vermelho = pg.draw.rect(tela, (255,0,0), (x, y, 40, 50))
    ret_azul = pg.draw.rect(tela, (0 ,0, 255), (x_azul, y_azul, 40, 50))

    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        pontos = pontos + 1
    tela.blit(texto_formatado, (400, 40))
    pg.display.update()

    







