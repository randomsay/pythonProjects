import pygame as pg, sys
from pygame.locals import *

# initialize global variables
XO = 'x'
winner = None
draw = False
width = 400
height = 400
white = (255,255,255)
line_color = (10,10,10)

# tic tac toe 3x3 board
TTT = [[None]*3, [None]*3, [None]*3]

# initializing pygame window
pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height+100), 0, 32)
pg.display.set_caption("Tic Tac Toe")

