import os

TILE_SIZE = 32

HEIGHT = TILE_SIZE * 20
WIDTH = TILE_SIZE * 25

MOB_HEIGTH = TILE_SIZE
MOB_WIDTH = TILE_SIZE
MOB_VELOCITY = 5

MOB_LAYER = 3
BLOCK_LAYER = 2
BACK_GROUND_LAYER = 1

FPS = 30

NOME_JOGO = "CC Frog"
FONTE_NAME = "arial"
FONTE_SZ = 32
TITLE_SZ = 64

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 100)
AZUL = (0, 0, 255)
BLUE = (0, 0, 255)


# Diretorios
DIR = os.getcwd()
IMAGE_DIR = os.path.join(DIR, "sprites")

FROG_SPRITE_NAME = "Frog_Sheet.png"
WALL_SPRITE_NAME = "Wall_Sheet.png"
GRASS_SPRITE_NAME = "Grass_Sheet.png"
MD_SPRITE_NAME = "MD_Book.png"
AVLC_SPRITE_NAME = "AVLC_Book.png"
CALC_SPRITE_NAME = "CALC_Book.png"

FROG_SHEET_DIR = os.path.join(IMAGE_DIR, FROG_SPRITE_NAME)
WALL_SHEET_DIR = os.path.join(IMAGE_DIR, WALL_SPRITE_NAME)
GRASS_SHEET_DIR = os.path.join(IMAGE_DIR, GRASS_SPRITE_NAME)

MD_DIR = os.path.join(IMAGE_DIR, MD_SPRITE_NAME)
AVLC_DIR = os.path.join(IMAGE_DIR, AVLC_SPRITE_NAME)
CALC_DIR = os.path.join(IMAGE_DIR, CALC_SPRITE_NAME)



TILE_MAP = [
    "WWWWWWWWWWWWWWWWWWWWWWWWW",
    "W.......................W",
    "WWWW..........A.........W",
    "W.......................W",
    "W....W............C.....W",
    "W....W..................W",
    "W....W.............WWWWWW",
    "W........A..............W",
    "W.......................W",
    "W......WWWWWW........C..W",
    "W.......................W",
    "W.....M.................W",
    "W..............M........W",
    "W.......................W",
    "WWWWWWWWWWWWWWWWWWWWWWWWW",
]