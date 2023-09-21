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
color = (255, 255, 255)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)
COLOR_BUTTON = (100, 100, 100)

# Diretorios
DIR = os.getcwd()
IMAGE_DIR = os.path.join(DIR, "sprites")

FROG_SPRITE_NAME = "Frog_Sheet.png"
WALL_SPRITE_NAME = "Wall_Sheet.png"
GRASS_SPRITE_NAME = "Grass_Sheet.png"
MD_SPRITE_NAME = "MD_Book.png"
AVLC_SPRITE_NAME = "AVLC_Book.png"
CALC_SPRITE_NAME = "CALC_Book.png"
SKELETON_IDLE_NAME = "skeleton-idle.png"
BACKGROUND_NAME = 'background.jpg'

FROG_SHEET_DIR = os.path.join(IMAGE_DIR, FROG_SPRITE_NAME)
WALL_SHEET_DIR = os.path.join(IMAGE_DIR, WALL_SPRITE_NAME)
GRASS_SHEET_DIR = os.path.join(IMAGE_DIR, GRASS_SPRITE_NAME,)
SKELETON_SHEET_DIR = os.path.join(IMAGE_DIR, SKELETON_IDLE_NAME)
BACKGROUND_DIR = os.path.join(IMAGE_DIR, BACKGROUND_NAME)

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

ALTERNATIVE_MAP = [
    "WWW.....C....WWW",
    ".....WWWWWWW....",
    "......WWWW......",
    ".......WW.......",
    ".......A.........",
    ".................",
    "................",
    "A....WWWWW.....M",
    "W......M.......W",
    "M....WWWWW.....C",
    "W......C.......W",
    "C.....WWW......A",
    ".......A.......",
    "................",
    "..WWWW.M.WWWW...",
    "......WWW.......",

]

ALTERNATIVE_MAP_2 = [
    "WW............WW",
    "W.......C......W",
    ".......WWW......",
    ".....WWWWWWW.....",
    "........A.......",
    "................",
    "......W.A.W.....",
    ".......W.W......",
    ".C.....WWW....M.",
    ".......W.W......",
    "......W.M.W.....",
    "................",
    "......WWWWWW.....",
    ".......WWWW......",
    "W.......A......W",
    "WW............WW", 
]

TEMPLE_MAP = [
    "................",
    ".....MW..W......",
    "..WWWWW..WWWWW..",
    "..W.........MW..",
    "..W..WWWWWW..W..",
    "..W...CWWA...W..",
    "..W..WWWWWW..W..",
    "......CWW.......",
    ".......WWC......",
    "..W..WWWWWW..W..",
    "..W...MWWC...W..",
    "..W..WWWWWW..W..",
    "..WA.........W..",
    "..WWWWW..WWWWW..",
    "......W..WM.....",
    "................",

]

RANDOM_MAP = [MAZE_MAP, INITIAL_MAP, MARKER_MAP, SOME_MAP, ALTERNATIVE_MAP, ALTERNATIVE_MAP_2, TEMPLE_MAP]