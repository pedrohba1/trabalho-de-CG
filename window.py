import pygame
import sys
import math
import primitives
from primitives import *
from pynput.mouse import Listener
from pynput.keyboard import Key, Listener
from pynput import mouse
from threading import Thread


screen_size = (800, 600)

# Variaveis de estilo
background = white
foreground = black

pygame.init()
window = pygame.display.set_mode(screen_size)
layer = pygame.surface.Surface(screen_size)
layer.blit(window, (0, 0))

pygame.display.set_caption('Trabalho computacao grafica')
window.fill(background)
layer.fill(white)
pygame.display.flip()

# Variaveis de controle
clicked = False
start = (0, 0)


primitiva = 0
# interface:
bresenham(window, 50, 50, 800, 50, black)
bresenham(window, 50, 50, 50, 600, black)


# para as primitivas
# linha
quadrado(window, 50, 50, 50, 100, black)
# retângulo
quadrado(window, 50, 50, 100, 150, black)
# quadrado
quadrado(window, 50, 50, 150, 200, black)
# círculo
quadrado(window, 50, 50, 200, 250, black)
# spline ou bezier
quadrado(window, 50, 50, 250, 300, black)
# polilinha
quadrado(window, 50, 50, 300, 350, black)

#
pygame.display.flip()

# try
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
