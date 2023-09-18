import os
import pygame
pygame.init()

TILE_SIZE = 32

HEIGHT = TILE_SIZE * 20
WIDTH = TILE_SIZE * 25

CHUNK_SIZE = 16

MOB_HEIGTH = TILE_SIZE
MOB_WIDTH = TILE_SIZE
MOB_VELOCITY = 5

MOB_LAYER = 3
BLOCK_LAYER = 2
BACK_GROUND_LAYER = 1

FPS = 30

NOME_JOGO = "Frog Adventures"
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

MUSICA_DE_FUNDO = pygame.mixer.music.load('musica_de_fundo.mp3')
 
SOM_DA_COLISAO = pygame.mixer.Sound('som_da_colisao.wav')


INITIAL_MAP = [
    "WWW.............",
    "................",
    "...WWWWW........",
    ".......WC.......",
    ".......W........",
    ".......WWWWW....",
    "................",
    "...............W",
    "....M..........W",
    "W..............W",
    "W...............",
    "W...............",
    "WWWWWW.......A..",
    "...........WWW..",
    "................",
    "......WWW.......",
]

MARKER_MAP = [
    "WW............WW",
    "W..............W",
    "................",
    "....E...C.......",
    ".............E..",
    "................",
    "................",
    "........E.......",
    "....M...........",
    "................",
    "....E.......E...",
    "................",
    ".............A..",
    "...E............",
    "W..............W",
    "WW............WW",
]


MAZE_MAP = [
    "WWWWWWWW......WW",
    "W.........WWWWWW",
    "..WWWWWW.......W",
    "W........WW....W",
    "..WWWWWW..WW...W",
    "WW.W......W....",
    ".W.WWWWW..W.....",
    ".........WWW..W.",
    "WWWW..WW......W.",
    "W.CWW...WWWw..W.",
    "W.W.W.W......W..",
    "W.....W.W.WWWWWW",
    "WWWW..W.W.....AW",
    "...WWWW.WWWWWW.W",
    "W.......W......W",
    "WWWWWWWWW...WWWW",
]

SOME_MAP = [
    "....WWWW....A...",
    "WW..WW..WW..WW..",
    "...C....WWWW...M",
    "WWWW......WWWWA.",
    "WWWWWWW..WWWWWWW",
    "WWW.......WWWWW.",
    "MWWWWWWWWWWWWWW.",
    "WWWWWWWW........",
    "WWWWWWWWWWWWWWWC",
    "................",
    "W........W.....W",
    "................",
    "..........WWWWWW",
    "WWWWWWWWWW......",
    "WWWWWWWWWWWWWWWW",
    "WW..............",

]

RANDOM_MAP = [MAZE_MAP, INITIAL_MAP, MARKER_MAP, SOME_MAP]