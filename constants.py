import os

HEIGHT = 480
WIDTH = 640

FPS = 30

NOME_JOGO = "CC Frog"
FONTE_NAME = "arial"
FONTE_SZ = 32
TITLE_SZ = 64

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 155, 50)


# Diretorios
DIR = os.getcwd()
IMAGE_DIR = os.path.join(DIR, "sprites")
FROG_SPRITE = "Frog_Sheet.png"
SHEET_DIR = os.path.join(IMAGE_DIR, FROG_SPRITE)

