import pygame
from constants import *


class UI:

    def __init__(self, TELA, CLOCK):

        self.FONTE = pygame.font.match_font(FONTE_NAME)
        self.TELA = TELA
        self.CLOCK = CLOCK

        FROG_SPRITE_SHEET = pygame.image.load(FROG_SHEET_DIR).convert_alpha()
        self.MENU_FROG_IMG = pygame.transform.scale(FROG_SPRITE_SHEET.subsurface((0, 0), (48, 48)), (48*2, 48*2))
        self.background = pygame.image.load(BACKGROUND_DIR)

        self.currentEvents = []



    def ShowMenu(self):

        LOOP = True
        while LOOP:
            self.TELA.blit(self.background, (0 , 0, WIDTH, HEIGHT))
            self.Write(NOME_JOGO, WIDTH/2, HEIGHT/3, TITLE_SZ, VERDE)

            self.MenuFrog()

            credits = self.create_button(WIDTH/2, HEIGHT/2 + 50, 140, 40, 'Credits', VERDE)
            play = self.create_button(WIDTH/2, HEIGHT/2, 140, 40, 'Play', AZUL)

            pygame.display.flip()

            if play:
                print("play")
                self.resetEvents()
                return
            
            if credits:
                print("CREDITS")
                self.resetEvents()
            

            self.Events()
            self.CLOCK.tick(FPS)
                


    def GameOver(self):
        
        s = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        s.fill((0, 0, 0, 128))
        self.TELA.blit(s, (0, 0))
        
        self.Write("GAME OVER", WIDTH/2, HEIGHT/3, TITLE_SZ, VERDE)

        self.MenuFrog()


        while True:
            menu = self.create_button(WIDTH/2, HEIGHT/2, 140, 40, 'Menu', AZUL)
            # play = self.create_button(WIDTH/2, HEIGHT/2 + 50, 140, 40, 'Play Again', VERDE) 

            pygame.display.flip()
         
            if menu:       
                self.resetEvents()
                return

            self.Events()
            self.CLOCK.tick(FPS)



    def TelaInGame(self, md, avlc, calc):
            self.Write(f"COLETADOS:", WIDTH/2, 3*HEIGHT/4)
            self.Write(f"MD: {md}", WIDTH/2, HEIGHT/2+HEIGHT/3)
            self.Write(f"AVLC: {avlc}", WIDTH/2, HEIGHT/2+HEIGHT/3 + FONTE_SZ)
            self.Write(f"CALC: {calc}", WIDTH/2, HEIGHT/2+HEIGHT/3 + FONTE_SZ + FONTE_SZ)



    def Write(self, text, x, y, size=FONTE_SZ, color=BRANCO, anchor = 0):
        fonte = pygame.font.Font(self.FONTE, size)
        txt = fonte.render(text, True, color)
        txt_rect = txt.get_rect()

        if anchor == 0:
            txt_rect.midtop = (x, y)
        elif anchor == 1:
            txt_rect.left = (x, y)
        elif anchor == 2:
            txt_rect.right = (x, y)

        self.TELA.blit(txt, txt_rect)

    def create_button(self, x, y, width, height, text, color = COLOR_BUTTON):

        clk = self.TesteClick(x, y, width, height)

        if clk == -1:
            color = VERMELHO

        rect = (pygame.Rect(x, y, width, height)) 
        rect.center = (x, y)
        pygame.draw.rect(self.TELA, color, rect)
        self.Write(text, x, y - FONTE_SZ/2)

        return bool(clk == 1)

    
    def resetEvents(self):
        self.currentEvents = []


    def Events(self):
        self.currentEvents = pygame.event.get()
        for event in self.currentEvents:
            if event.type == pygame.locals.QUIT:
                pygame.quit()

    
    def MenuFrog(self):
        frg_rect = self.MENU_FROG_IMG.get_rect()
        frg_rect.center = (WIDTH/2, 2*HEIGHT/3)
        self.TELA.blit(self.MENU_FROG_IMG, frg_rect)


    def TesteClick(self, X, Y, W, H):

        for event in self.currentEvents:
            if event.type == pygame.locals.QUIT:
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if X - W/2 <= event.pos[0] <= X+W/2 and Y-H/2 < event.pos[1] < Y+H/2 :
                        return 1

        mouse = pygame.mouse.get_pos()
        if X - W/2 <= mouse[0] <= X+W/2 and Y-H/2 < mouse[1] < Y+H/2 :            
            return -1
        return 0


    def ShowCredits(self):
        pass

            







