# -*-coding utf-8-*-
import sys
import pygame
import time
import function
import math


black = (0, 0, 0)
white = (255, 255, 255)

pygame.init()  # inicialization do pygame

window = pygame.display.set_mode((500, 500))  # cria uma janela
window.fill(white)
pygame.display.set_caption("Teste do bresenham")  # Altera o nome da janela
controle = 1
while True:

    for event in pygame.event.get():  # um loop para checar se os eventos estao ocorrendo exemplo mouse,click,teclar

        if event.type == pygame.QUIT:  # quando clica no x da janela ele para o jogo
            pygame.quit()
            sys.exit()
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if controle == 1:
                x1, y1 = pygame.mouse.get_pos()
                controle += 1
            elif controle == 2 and pygame.mouse.get_pressed() == (1, 0, 0):
                x2, y2 = pygame.mouse.get_pos()
                controle = 1
                if y1 == y2 or x1 == x2:
                    if x1 == x2:
                        if x1 > x2:
                            distancia = y2-y1
                        else:
                            distancia = y1-y2

                        function.bresenham_completo(
                            window, x2, y2, x2+distancia, y2)
                        function.bresenham_completo(
                            window, x2, y2, x2, y2+distancia)
                        function.bresenham_completo(
                            window, x2+distancia, y2, x2+distancia, y2+distancia)
                        function.bresenham_completo(
                            window, x2, y2+distancia, x2+distancia, y2+distancia)
                    elif y1 == y2:
                        if y1 > y2:
                            distancia = x2-x1
                        else:
                            distancia = x1-x2

                        function.bresenham_completo(
                            window, x2, y2, x2 + distancia, y2)
                        function.bresenham_completo(
                            window, x2, y2, x2, y2 + distancia)
                        function.bresenham_completo(
                            window, x2 + distancia, y2, x2 + distancia, y2 + distancia)
                        function.bresenham_completo(
                            window, x2, y2 + distancia, x2 + distancia, y2 + distancia)
                else:
                    if y2 > y1 and x2 > x1:
                        distancia = int(
                            math.sqrt(((y2-y1)*(y2-y1))+((x2-x1)*(x2-x1))))
                        function.bresenham_completo(
                            window, x1, y1, x1 + distancia, y1)
                        function.bresenham_completo(
                            window, x1, y1, x1, y1 + distancia)
                        function.bresenham_completo(
                            window, x1 + distancia, y1, x1 + distancia, y1 + distancia)
                        function.bresenham_completo(
                            window, x1, y1 + distancia, x1 + distancia, y1 + distancia)
                    elif y2 > y1 and x2 < x1:
                        distancia = int(
                            math.sqrt(((y2 - y1) * (y2 - y1)) + ((x1 - x2) * (x1 - x2))))
                        function.bresenham_completo(
                            window, x1, y1, x1 - distancia, y1)
                        function.bresenham_completo(
                            window, x1, y1, x1, y1 + distancia)
                        function.bresenham_completo(
                            window, x1 - distancia, y1, x1 - distancia, y1 + distancia)
                        function.bresenham_completo(
                            window, x1, y1 + distancia, x1 - distancia, y1 + distancia)
                    elif y2 < y1 and x2 > x1:
                        distancia = int(
                            math.sqrt(((y1 - y2) * (y1 - y2)) + ((x1 - x2) * (x1 - x2))))
                        function.bresenham_completo(
                            window, x1, y1, x1 + distancia, y1)
                        function.bresenham_completo(
                            window, x1, y1, x1, y1 - distancia)
                        function.bresenham_completo(
                            window, x1 + distancia, y1, x1 + distancia, y1 - distancia)
                        function.bresenham_completo(
                            window, x1, y1 - distancia, x1 + distancia, y1 - distancia)
                    else:
                        distancia = int(
                            math.sqrt(((y1 - y2) * (y1 - y2)) + ((x2 - x1) * (x2 - x1))))
                        function.bresenham_completo(
                            window, x1, y1, x1 - distancia, y1)
                        function.bresenham_completo(
                            window, x1, y1, x1, y1 - distancia)
                        function.bresenham_completo(
                            window, x1 - distancia, y1, x1 - distancia, y1 - distancia)
                        function.bresenham_completo(
                            window, x1, y1 - distancia, x1 - distancia, y1 - distancia)

    time.sleep(0.03)
    pygame.display.update()  # refresh da janela
