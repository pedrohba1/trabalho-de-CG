import pygame
import sys
import math
from primitives import *
import time

screen_size = (800, 600)

# Variaveis de estilo
background = white
foreground = black

pygame.init()
window = pygame.display.set_mode(screen_size)

pygame.display.set_caption('Trabalho computacao grafica')
window.fill(background)
pygame.display.flip()


# Cor 0
quadrado(window, 0, 50, 50, 50, black)
# Cor 1
quadrado(window, 50, 100, 50, 50, black)
# Cor 2
quadrado(window, 100, 150, 50, 50, black)
# Cor 3
quadrado(window, 150, 200, 50, 50, black)
# Cor 4
quadrado(window, 200, 250, 50, 50, black)
# Cor 5
quadrado(window, 250, 300, 50, 50, black)
# Cor 6
quadrado(window, 300, 350, 50, 50, black)
# Cor 7
quadrado(window, 350, 400, 50, 50, black)
# Cor 8
quadrado(window, 400, 450, 50, 50, black)
# Cor 9
quadrado(window, 450, 500, 50, 50, black)
# Cor 10
quadrado(window, 500, 550, 50, 50, black)
# Cor 11
quadrado(window, 550, 600, 50, 50, black)
# Cor 12
quadrado(window, 600, 650, 50, 50, black)
# Cor 13
quadrado(window, 650, 700, 50, 50, black)
# Cor 14
quadrado(window, 700, 750, 50, 50, black)
# Cor 15
quadrado(window, 750, 800, 50, 50, black)


# Variaveis de controle
clicked = False
start = (0, 0)

# primitiva escolhida atual:
primitiva = 0


# interface:

bresenham(window, 50, 50, 800, 50, black)
bresenham(window, 50, 50, 50, 600, black)


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
circulo(window, 25, 225, 20, black)
# spline ou bezier
quadrado(window, 50, 50, 250, 300, black)
bezier(window, (10, 260), (20, 285), (45, 290), black)
# polilinha
quadrado(window, 50, 50, 300, 350, black)
bresenham(window, 10, 260, 20, 280, black)
bresenham(window, 20, 280, 30, 260, black)
bresenham(window, 30, 260, 40, 280, black)

colorAtual = black
#
pygame.display.flip()


def muda_botao(position):
    if (position[0] < 50 and position[0] > 0) and (position[1] > 50 and position[1] < 100):
        print("aqui agora")
        primitiva = 1
        if (primitiva == 1):
            desenha_linha(position)
            pygame.display.update()


def desenha_linha(position):
    print("aqui desenahndo")
    while 1:
        position2 = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("cheguei")
                bresenham(window, position[0], position[1],
                          position2[0], position2[1], colorAtual)
            if (event.type == pygame.MOUSEBUTTONUP):
                return


def ClickHandler(position):
    if (position[0] < 50 and position[1] > 50):
        muda_botao(position)


while True:

    position = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            ClickHandler(position)

        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
