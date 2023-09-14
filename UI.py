import pygame
from constants import *


class UI:

    def __init__(self, TELA):

        self.FONTE = pygame.font.match_font(FONTE_NAME)
        self.TELA = TELA

        FROG_SPRITE_SHEET = pygame.image.load(FROG_SHEET_DIR).convert_alpha()
        self.MENU_FROG_IMG = pygame.transform.scale(FROG_SPRITE_SHEET.subsurface((0, 0), (48, 48)), (48*2, 48*2))


    def ShowMenu(self):

        self.Write(NOME_JOGO, WIDTH/2, HEIGHT/3, TITLE_SZ, VERDE)
        self.Write("Pressione Qualquer Tecla para Jogar...", WIDTH/2, HEIGHT/2+HEIGHT/3)

        frg_rect = self.MENU_FROG_IMG.get_rect()
        frg_rect.center = (WIDTH/2, 2*HEIGHT/3)
        self.TELA.blit(self.MENU_FROG_IMG, frg_rect)

        pygame.display.flip()


    
    def Write(self, text, x, y, size=FONTE_SZ, color=BRANCO):
        fonte = pygame.font.Font(self.FONTE, size)
        txt = fonte.render(text, True, color)
        txt_rect = txt.get_rect()
        txt_rect.midtop = (x, y)
        self.TELA.blit(txt, txt_rect)



    def telaInGame(self, md, avlc, calc):
            self.Write(f"COLETADOS:", WIDTH/2, 3*HEIGHT/4)
            self.Write(f"MD: {md}", WIDTH/2, HEIGHT/2+HEIGHT/3)
            self.Write(f"AVLC: {avlc}", WIDTH/2, HEIGHT/2+HEIGHT/3 + FONTE_SZ)
            self.Write(f"CALC: {calc}", WIDTH/2, HEIGHT/2+HEIGHT/3 + FONTE_SZ + FONTE_SZ)