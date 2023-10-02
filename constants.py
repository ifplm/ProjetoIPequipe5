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

MAX_MOBS = 15
SPAW_CHANCE = 10 # %
SPAW_MIN_DIST = 10
SPAW_MAX_DIST = SPAW_MIN_DIST +  1 * CHUNK_SIZE
UNSPAW_DIST =   2 * CHUNK_SIZE * TILE_SIZE
GHOST_RARITY = 25

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
OBJETOS_SPRITES_NAME = "Misc_Sheet.png"

FROG_SHEET_DIR = os.path.join(IMAGE_DIR, FROG_SPRITE_NAME)
WALL_SHEET_DIR = os.path.join(IMAGE_DIR, WALL_SPRITE_NAME)
GRASS_SHEET_DIR = os.path.join(IMAGE_DIR, GRASS_SPRITE_NAME,)
SKELETON_SHEET_DIR = os.path.join(IMAGE_DIR, SKELETON_IDLE_NAME)
GHOST_SHEET_DIR = os.path.join(IMAGE_DIR, GHOST_IDLE_NAME)
BACKGROUND_DIR = os.path.join(IMAGE_DIR, BACKGROUND_NAME)
OBJETO_SHEET_DIR = os.path.join(IMAGE_DIR, OBJETOS_SPRITES_NAME)

MD_DIR = os.path.join(IMAGE_DIR, MD_SPRITE_NAME)
AVLC_DIR = os.path.join(IMAGE_DIR, AVLC_SPRITE_NAME)
CALC_DIR = os.path.join(IMAGE_DIR, CALC_SPRITE_NAME)


MUSICA_DE_FUNDO = pygame.mixer.music.load('musica_de_fundo.mp3')

SOM_DA_COLISAO = pygame.mixer.Sound('som_da_colisao.wav')

SOM_MORREU = pygame.mixer.Sound('som_morreu.wav')


INITIAL_MAP = [
    "WWW.............",
    "................",
    "...WWWWW...L....",
    "....PBBWC.......",
    ".......W........",
    ".......WWWWW....",
    "........V.......",
    "...............W",
    "....M..........W",
    "WB.............W",
    "WV..............",
    "W....B..........",
    "WWWWWW.......A..",
    "...........WWW..",
    "............V...",
    "......WWW.......",
]

MARKER_MAP = [
    "WW............WW",
    "WB.............W",
    "................",
    "....E...C.......",
    ".......2.V...E..",
    ".......P........",
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
    "..WWWWWW......A.",
    "..........W.....",
    ".WWWWWWW..W.....",
    ".WC.......W.....",
    ".W.WWWWW..WM....",
    ".......A.WWW..W.",
    "WWWW.....WM...W.",
    "W.CW....WWWW..W.",
    "W.WW..W.......W.",
    "......W.W.WWWWWW",
    ".....MW.W.....AW",
    "...WWWW.W......W",
    "W...C...W......W",
    "WWWWWWWWW.......",
]

SOME_MAP = [
    "........WWW..C.W",
    "........vWVv...W",
    "................",
    "...WWWW..M......",
    ".....BW.........",
    "....A.WWWW......",
    "......WP2.......",
    "......V.........",
    "...........W....",
    "...M.......M....",
    "..........LW....",
    "...........C....",
    "..P........W....",
    ".WVv.....A......",
    ".WWWv....WWWV...",
    ".........WWW....",

]

ALTERNATIVE_MAP = [
    "WWW.....C....WWW",
    ".....WWWWWW.....",
    "......WWWWB.....",
    ".......WWVv......",
    ".......L........",
    "......PA........",
    ".......A........",
    "A....WWWWW.....M",
    "W......M.......W",
    "M....WWWWW.....C",
    "WV.....C.......W",
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
    ".....vLW.WL.....",
    ".C....VWWWVB..M.",
    "......LW.WBB....",
    "......W.M.W.....",
    "................",
    "......WWWWWW....",
    ".......WWWW.....",
    "WV......A......W",
    "WW............WW", 
]

TEMPLE_MAP = [
    "................",
    "...vVMW..WVv....",
    "..WWWWW..WWWWW..",
    "..W.........MW..",
    "..W..WWWWWW..W..",
    "..W...CWWA...W..",
    "..W..WWWWWW..W..",
    "....P.CWWPL.....",
    "......VWWC......",
    "..W..WWWWWW..W..",
    "..W...MWWC...W..",
    "..W..WWWWWW..W..",
    "..WA.........W..",
    "..WWWWW..WWWWW..",
    "...B2.W..WM.....",
    "................",

]
ALTERNATIVE_MAP_3 = [
    "................",
    ".BWWWWWWWWWWWWW.",
    ".W.....C...ACAW.",
    ".W.WW...W..MWMW.",
    ".W....WWWWWWWWW.",
    ".WWWB.....P2....",
    ".W............W.",
    ".W.WWW.......AW.",
    ".W...W.WWW...WW.",
    ".WWW.W...W...MW.",
    ".....W.W.W....W.",
    "...VWW.W.W....W.",
    ".....V.W.WWW..W.",
    ".......W........",
    "..WWWWWW....VWW.",
    "................",
]
LABIRINT_1 = [
    "................",
    ".WWWWWW..WWWWWW.",
    "...Pv...........",
    ".W.......WWWW.W.",
    ".WWWWWWW....W.W.",
    ".W..........W.W.",
    ".W.WWWWWWWW.W.W.",
    ".....CWv....W.W.",
    ".W.WWWW..WWWW...",
    ".W.WAC..M.MCW.W.",
    ".W.WWWWWWWWWW.W.",
    ".W....PL2.....W.",
    ".W.W...B......W.",
    "...W............",
    ".WWWWWW..WWWWWW.",
    "................",
]
LABIRINT_2 = [
    "................",
    ".W.WWWWWWWWWW.W.",
    ".W.....A......W.",
    ".W.W.WW.WWWW.WW.",
    ".W.W.W........W.",
    ".W.WCW.L......W.",
    ".W.W.V.W..W.WWW.",
    "................",
    ".W...WWWWWW...W.",
    ".W........v...W.",
    "...WWWW.........",
    ".W...AW.......W.",
    ".W......WWW..WW.",
    "...CW..M........",
    "...WWWWW..WWW...",
    "................",
]
LABIRINT_3 = [
    "................",
    ".W..WWWWWWWWWWW.",
    ".W.P2...........",
    ".W.....WWWW.....",
    ".LWWWWW.......W.",
    ".W....MW......W.",
    ".W.W......W.WWW.",
    ".W.W..A.W.W.....",
    ".W..WWW.W.W.WWW.",
    ".W....C.V.W...W.",
    ".W.cWWW...W...W.",
    ".W.WA...WWW.AAW.",
    ".W.WWW.WWMCMM.W.",
    ".W......WACMAMW.",
    ".W.WWWWWWWWWWWW.",
    "................",
]
LABIRINT_4 = [
    ".....WWWWBVv.....",
    ".W...C..A........",
    ".W.WWWWWWWWWWWW.",
    ".W...C......M.W.",
    ".WWWWWWWWWWWW.W.",
    ".W.....A......W.",
    ".W.WWWWWWWWWWWW.",
    ".W..M.....C...W.",
    ".WWWWWWWWWWWW.W.",
    ".W......A.....W.",
    ".W.WWWWWWWWWWWW.",
    ".W.C..A.....M.W.",
    ".WWWWWWWWWWWW.W.",
    ".......M......W.",
    ".WWWWWWWWWWWWWW.",
    "................",
]
LABIRINT_5 = [
    "................",
    ".v.2.WWWWWW.....",
    ".W............W.",
    ".W.WWWWWWW....W.",
    ".W..WWWWC.....W.",
    ".W.......W....W.",
    ".W.W...MCW....W.",
    ".W.W....WW...BW.",
    ".W.WVA......BVW.",
    ".W.......WWWWWW.",
    ".W..WWWW...PLAW.",
    ".W......W.....W.",
    ".W.WWWW.W.WWWWW.",
    ".W...AW.W.......",
    ".WWWWWW.WWWWWWW.",
    "................",
]
LABIRINT_6 = [
    ".W..............",
    ".W.VWWWWWWWWWWW.",
    "..............W.",
    ".W.WWWWWWWWW....",
    ".W.W..W.........",
    ".W.WA.........W.",
    ".W...W..WWW...W.",
    ".W...W....L...W.",
    ".W.W.W....W.W.W.",
    ".W.W.WA..AW.W.W.",
    ".W.W.WAAAvW.W...",
    "..CW.WVAAAW.W.W.",
    ".WWW.WWWWWW.W.W.",
    ".W..............",
    "...WWWWWWWWWWWW.",
    "....V......L2.W.",
]
LABIRINT_7 = [
    "................",
    ".WW.WWWWWWWW.WW.",
    ".WM...L.......W.",
    "......WW..WWAAW.",
    ".W.W.......WWWW.",
    ".W.W...M........",
    ".W.W........WWW.",
    ".W.W.VWWW.WWM...",
    ".W.W...CW.W.W.W.",
    ".W.WCC.CW...W.W.",
    ".W.WWWCCW.W.W...",
    ".WPL.WCCW.W.V.W.",
    ".W...WWWW.W...W.",
    ".W..............",
    ".WWWWWW..WWWWWW.",
    "................",
]
ALTERNATIVE_MAP_4 = [
    "................",
    ".W.WWWWWWWWW..W.",
    "...WM.AWM.AWCCW.",
    ".WAW.W.W.W.W..W.",
    ".W.W.W.W.W.W..W.",
    ".W.W.W.W.W.W..W.",
    ".W.W.W.W.W.WV.W.",
    ".W.WCW.W.WAW..W.",
    ".WAW.W.W.W.W..W.",
    ".W.W.WMW.W.W.vW.",
    ".W.W.W.W.W.W..W.",
    ".W.W.W.WMW.W..W.",
    ".....W...W....W.",
    ".L.WWWWWWWWW..W.",
    "...W.2.V2..W....",
    "................",
]
ALTERNATIVE_MAP_5 = [
    "................",
    "................",
    "....WB..........",
    "..W..W....PLv...",
    "...W..W...v.A...",
    "....W..W........",
    "..W..W..W.......",
    "...W..W..W......",
    "...VW..W..W.....",
    "....WAWMWCW.....",
    ".....W..WWW.....",
    "......W..WvB....",
    ".PL....W..WV....",
    ".......VW.W.....",
    "................",
    "................",
]
ALTERNATIVE_MAP_6 = [
    "................",
    ".WWWWWW..WWWW.W.",
    ".WL....M.....MW.",
    "..............W.",
    ".W..WWWWWWWW..W.",
    ".W..W...A..W..W.",
    ".W..W.M....W..W.",
    ".W..M...M..M..W.",
    ".W..W...M..W..W.",
    ".W..WVvBM..W..W.",
    ".W..WWWWWWWW..W.",
    ".....LP2......W.",
    ".WV...........W.",
    ".WB.............",
    ".WWWWWW..WWWWWW.",
    "................",
]
ALTERNATIVE_MAP_7 = [
    "................",
    ".W..W....W..W...",
    "..W..WP...W..W..",
    "...W...L...W..W.",
    "..W..W....W..W..",
    "...W..W..W..W...",
    ".....W....W.....",
    ".....MW....W..W.",
    "....W..W..WM.W..",
    "....W.W......W..",
    "....WB.W..W..W..",
    "....W..M.M.W.W..",
    "....W..W.M..VW..",
    ".P..WW.MMMM.WW..",
    "..L...WWWWWW....",
    "................",
]
ALTERNATIVE_MAP_8 = [
    ".......WWW..W...",
    ".WW.WW..M.W..W..",
    "W...VW..W..W..W.",
    "W......A.W..W..W",
    ".W..W.....W....W",
    "..W..W...BAW..WW",
    "...W.CW..WW.....",
    "....W..W........",
    ".M..W..W...MB...",
    "...W..W.........",
    "..W..WWW..WWWWWW",
    ".W..W.....W..M.W",
    "W..W..W..W..W..W",
    "W.A..W..W..W..W.",
    ".WWWWW....W..W..",
    "......WWWW..W...",
]
RANDOM_MAP = [MAZE_MAP, INITIAL_MAP, MARKER_MAP, SOME_MAP, ALTERNATIVE_MAP, ALTERNATIVE_MAP_2, TEMPLE_MAP, ALTERNATIVE_MAP_3, LABIRINT_1, LABIRINT_2, LABIRINT_3, LABIRINT_4, LABIRINT_5, LABIRINT_6, LABIRINT_7, ALTERNATIVE_MAP_5, ALTERNATIVE_MAP_6, ALTERNATIVE_MAP_7, ALTERNATIVE_MAP_8]
