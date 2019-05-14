import pygame
import sys
import math
from primitives import *


screen_size = (800, 600)

# Variaveis de estilo
background = white
foreground = black

pygame.init()
window = pygame.display.set_mode(screen_size)

pygame.display.set_caption('Trabalho computacao grafica')
window.fill(background)
pygame.display.flip()

# Variaveis de controle
clicked = False
start = (0, 0)

# primitiva escolhida atual:
primitiva = 0


# interface:

bresenham(window, 50, 50, 800, 50, black)
bresenham(window, 50, 50, 50, 600, black)
#Moldura da janela
bresenham(window,0,0,0,600,black)
bresenham(window,0,0,800,0,black)
bresenham(window,800,0,800,600,black)
bresenham(window,0,600,800,600,black)


# para as primitivas
# linha
quadrado(window, 50, 50, 50, 100, black)
bresenham(window, 10, 60, 40, 90, black)
# retângulo
quadrado(window, 50, 50, 100, 150, black)
retangulo(window, 10, 120, 40, 140, black)
# quadrado
quadrado(window, 50, 50, 150, 200, black)
quadrado(window, 10, 40, 160, 180, black)
# círculo
quadrado(window, 50, 50, 200, 250, black)
# spline ou bezier
quadrado(window, 50, 50, 250, 300, black)
bezier(window,(10,210),(20,240),(45,240),black)
# polilinha
quadrado(window, 50, 50, 300, 350, black)
bresenham(window,10,260,20,280,black)
bresenham(window,20,280,30,260,black)
bresenham(window,30,260,40,280,black)


#
pygame.display.flip()


# try
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
