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

MAX_MOBS = 30
SPAW_CHANCE = 20 # %
SPAW_MIN_DIST = 3
SPAW_MAX_DIST = SPAW_MIN_DIST +  1 * CHUNK_SIZE
UNSPAW_DIST =   2 * CHUNK_SIZE * TILE_SIZE

MOB_LAYER = 3
BLOCK_LAYER = 2
BACK_GROUND_LAYER = 1

FPS = 30

PLAYER_DEFAULT_X = WIDTH/TILE_SIZE/2
PLAYER_DEFAULT_Y = HEIGHT/TILE_SIZE/2

NOME_JOGO = "Frog Adventures"
FONTE_NAME = "arial"
SMALL_FONT = 'Corbel'
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
GHOST_IDLE_NAME = "ghostDead-Sheet.png"
BACKGROUND_NAME = 'background.jpg'

FROG_SHEET_DIR = os.path.join(IMAGE_DIR, FROG_SPRITE_NAME)
WALL_SHEET_DIR = os.path.join(IMAGE_DIR, WALL_SPRITE_NAME)
GRASS_SHEET_DIR = os.path.join(IMAGE_DIR, GRASS_SPRITE_NAME,)
SKELETON_SHEET_DIR = os.path.join(IMAGE_DIR, SKELETON_IDLE_NAME)
GHOST_SHEET_DIR = os.path.join(IMAGE_DIR, GHOST_IDLE_NAME)
BACKGROUND_DIR = os.path.join(IMAGE_DIR, BACKGROUND_NAME)

MD_DIR = os.path.join(IMAGE_DIR, MD_SPRITE_NAME)
AVLC_DIR = os.path.join(IMAGE_DIR, AVLC_SPRITE_NAME)
CALC_DIR = os.path.join(IMAGE_DIR, CALC_SPRITE_NAME)


MUSICA_DE_FUNDO = pygame.mixer.music.load('musica_de_fundo.mp3')

SOM_DA_COLISAO = pygame.mixer.Sound('som_da_colisao.wav')

SOM_MORREU = pygame.mixer.Sound('som_morreu.wav')


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
    "WWWWWWWW.......W",
    "WM........WWWWWW",
    "..WWWWWW......AW",
    "..........W....W",
    ".WWWWWWW..W....W",
    ".WC.......W.....",
    ".W.WWWWW..WM....",
    ".......A.WWW..W.",
    "WWWW.....WM...W.",
    "W.CW....WWWW..W.",
    "W.WW..W.......W.",
    "......W.W.WWWWWW",
    "WWWW.MW.W.....AW",
    "...WWWW.WWWWWW.W",
    "W...C...W......W",
    "WWWWWWWWW...WWWW",
]

SOME_MAP = [
    "........WWW..C.W",
    ".........W.....W",
    "................",
    "...WWWW..M......",
    "......W.........",
    "....A.WWWW......",
    "......W.........",
    "................",
    "...........W....",
    "...M.......M....",
    "...........W....",
    "...........C....",
    "...........W....",
    ".W.......A......",
    ".WWW.....WWW....",
    ".........WWW....",

]

ALTERNATIVE_MAP = [
    "WWW.....C....WWW",
    ".....WWWWWWW....",
    "......WWWW......",
    ".......WW.......",
    ".......A........",
    "................",
    "................",
    "A....WWWWW.....M",
    "W......M.......W",
    "M....WWWWW.....C",
    "W......C.......W",
    "C.....WWW......A",
    ".......A........",
    "................",
    "..WWWW.M.WWWW...",
    "......WWW.......",

]

ALTERNATIVE_MAP_2 = [
    "WW............WW",
    "W.......C......W",
    ".......WWW......",
    ".....WWWWWWW....",
    "........A.......",
    "................",
    "......W.A.W.....",
    ".......W.W......",
    ".C.....WWW....M.",
    ".......W.W......",
    "......W.M.W.....",
    "................",
    "......WWWWWW....",
    ".......WWWW.....",
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
ALTERNATIVE_MAP_3 = [
    "................",
    ".WWWWWWWWWWWWWW.",
    ".W....WC..WACAW.",
    ".W.WW...W..MWMW.",
    ".W...WWWWWWWWWW.",
    ".WWW.W..........",
    ".W...W........W.",
    ".W.WWW........W.",
    ".W...WWWWW.WWWW.",
    ".WWW.W...W....W.",
    ".W...W.W.W...WW.",
    ".W.WWW.W.W....W.",
    ".W...W.W.WWW..W.",
    "..WW...W........",
    ".WWWWWWWWWWWWWW.",
    "................",
]
LABIRINT_1 = [
    "................",
    ".WWWWWWWWWWWWWW.",
    ".W............W.",
    ".W.......WWWW.W.",
    ".WWWWWWW....W.W.",
    ".W..........W.W.",
    ".W.WWWWWWWWWW.W.",
    ".W......W...W.W.",
    ".W.WWWW..WWW..W.",
    ".W.WAC..M.MCW.W.",
    ".W.WWWWWWWWWW.W.",
    ".W.W..........W.",
    ".W.W..........W.",
    "...W............",
    ".WWWWWWWWWWWWWW.",
    "................",
]
LABIRINT_2 = [
    "................",
    ".WWWWWWWWWWWWWW.",
    ".W.....A......W.",
    ".W.W.WW.WWWW.WW.",
    ".W.W.W..W.....W.",
    ".W.WCW.W......W.",
    ".W.WW..W..W.WWW.",
    "...W..W.........",
    ".W.WWWWWWWW.WWW.",
    ".W.....WW.....W.",
    ".W.WWWW.......W.",
    ".W..W.WW......W.",
    ".W......WWW..WW.",
    ".W..W..M......W.",
    ".WWWWWWWWWWWWWW.",
    "................",
]
LABIRINT_3 = [
    "................",
    ".W.WWWWWWWWWWWW.",
    ".W............W.",
    ".W.......WW...W.",
    ".WWWWWW.W..W..W.",
    ".W....MW...W..W.",
    ".W.W.WW...W..W..",
    ".W.W....W.W...W.",
    ".W..WWW.W.W...W.",
    ".W....CW..W...W.",
    ".W.WWWW...W...W.",
    ".W.WA...WW....W.",
    ".W.WWW.W.....W..",
    ".W...W........W.",
    ".W.WWWWWWWWWWWW.",
    "................",
]
LABIRINT_4 = [
    ".WWWW.WWWWW.....",
    ".W..............",
    ".W.WWWWWWWWWWWW.",
    ".W............W.",
    ".WWWWWWWWWWWW.W.",
    ".W............W.",
    ".W.WWWWWWWWWWWW.",
    ".W............W.",
    ".WWWWWWWWWWWW.W.",
    ".W......A.....W.",
    ".W.WWWWWWWWWWWW.",
    ".W....A.......W.",
    ".WWWWWWWWWWWW.W.",
    "..............W.",
    ".WWWWWWWWWWWWWW.",
    "................",
]
LABIRINT_5 = [
    "................",
    ".WWWWWWWWWWWWWW.",
    ".W............W.",
    ".W.WWWWWWW.W..W.",
    ".W..WWWW...W..W.",
    ".W......W.W...W.",
    ".W..W..WM.W...W.",
    ".W.W..W.WW....W.",
    ".W.WCW........W.",
    ".W..W....WWWWWW.",
    ".WW.WWWW......W.",
    ".W......W.....W.",
    ".W.WWWW.W.WWWWW.",
    ".W...AW.W.......",
    ".WWWWWW.WWWWWWW.",
    "................",
]
LABIRINT_6 = [
    "................",
    ".WWWWWWWWWWWWWW.",
    "..............W.",
    ".WWWWWWWWWWWW.W.",
    ".W....W.......W.",
    ".W.WA..W...W..W.",
    ".W.WWW..WWW...W.",
    ".W...W........W.",
    ".W.W.W....W.W.W.",
    ".W.W.W....W.W.W.",
    ".W.W.W....W.W.W.",
    ".WCW.W..A.W.W.W.",
    ".WWW.WWWWWW.WWW.",
    ".W..............",
    ".WWWWWWWWWWWWWW.",
    "................",
]
LABIRINT_7 = [
    "................",
    ".WW.WWWWWWWWWWW.",
    ".W...W........W.",
    ".W....WWW.WW..W.",
    ".W.WWW......WWW.",
    ".W.W............",
    ".W.W.W......WWW.",
    ".W.W..WWW.WWM.W.",
    ".W.W.W..W.W.W.W.",
    ".W.W....W...W.W.",
    ".W.WWWCCW.W.W.W.",
    ".W...WCCW.W.W.W.",
    ".W....WW..W.W.W.",
    ".W........W...W.",
    ".WWWWWWWWWWWWWW.",
    "................",
]
ALTERNATIVE_MAP_4 = [
    "................",
    ".WWWWWWWWWWWWWW.",
    ".WAWMWAWMWAWCCW.",
    ".W.W.W.W.W.W..W.",
    ".W.W.W.W.W.W..W.",
    ".W.W.W.W.W.W..W.",
    ".W.W.W.W.W.W..W.",
    ".W.W.W.W.W.W..W.",
    ".W.W.W.W.W.W..W.",
    ".W.W.W.W.W.W..W.",
    ".W.W.W.W.W.W..W.",
    ".W.W.W.W.W.W..W.",
    ".W.W.W.W.W.W..W.",
    ".W.W.W.W.W.W..W.",
    "................",
    "................",
]
ALTERNATIVE_MAP_5 = [
    "................",
    "................",
    "....W...........",
    "..W..W..........",
    "...W..W.........",
    "....W..W........",
    "..W..W..W.......",
    "...W..W..W......",
    "....W..W..W.....",
    "....WAWMWCW.....",
    ".....W..WWW.....",
    "......W..W......",
    ".......W..W.....",
    "........W.W.....",
    "................",
    "................",
]

RANDOM_MAP = [MAZE_MAP, INITIAL_MAP, MARKER_MAP, SOME_MAP, ALTERNATIVE_MAP, ALTERNATIVE_MAP_2, TEMPLE_MAP, ALTERNATIVE_MAP_3, LABIRINT_1, LABIRINT_2, LABIRINT_3, LABIRINT_4, LABIRINT_5, LABIRINT_6, LABIRINT_7, ALTERNATIVE_MAP_5]