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


# Variaveis de controle
clicked = False
start = (0, 0)

# primitiva escolhida atual:
primitiva = 0


# interface:

bresenham(window, 0, 50, 800, 50, black)


# Moldura da janela
bresenham(window, 0, 0, 0, 600, black)
bresenham(window, 0, 0, 800, 0, black)
bresenham(window, 800, 0, 800, 600, black)
bresenham(window, 0, 600, 800, 600, black)


# para as primitivas

#retangulo(window,x1,y1,x2,y2,color)
# linha
retangulo(window ,0,25,25,50,black)
# retângulo
retangulo(window ,25,25,50,50,black)


# quadrado
retangulo(window ,50,25,75,50,black)

# círculo
retangulo(window ,75,25,100,50,black)

# spline ou bezier
retangulo(window ,100,25,125,50,black)

# polilinha
retangulo(window ,125,25,150,50,black)

#preencher
retangulo(window ,150,25,175,50,black)

#cores: 

#observção: nos números em parênteses, os primeiros dois são a posição do primeiro ponto
#  do retãngulo no canto superior esquerdo e os dois outros
#são a dimensão dele
# Cor 0
pygame.draw.rect(window, black, (0, 0, 25, 25))
# Cor 1
pygame.draw.rect(window, (169, 169, 169), (25,0, 25, 25))
# Cor 2
pygame.draw.rect(window, (0, 0, 255), (50, 0, 25, 25))
 #Cor 3
pygame.draw.rect(window,(255, 255,  0), (75, 0, 25, 25))
# Cor 4
pygame.draw.rect(window, (255, 0, 0), (100, 0, 25, 25))
# Cor 5
pygame.draw.rect(window, (0, 255, 0), (125, 0, 25, 25))
# Cor 6
pygame.draw.rect(window, (255, 105, 180), (150, 0, 25, 25))
# Cor 7
pygame.draw.rect(window, (255, 140, 0), (175, 0, 25, 25))
# Cor 8
pygame.draw.rect(window, (0, 191, 255), (200, 0, 25, 25))
# Cor 9
pygame.draw.rect(window, (255, 191, 0), (225, 0, 25, 25))
# Cor 10
pygame.draw.rect(window, (128, 0, 0), (250, 0, 25, 25))
# Cor 11
pygame.draw.rect(window, (138, 0, 138), (275, 0, 25, 25))
# Cor 12
pygame.draw.rect(window, (80, 200, 120), (300, 0, 25, 25))
# Cor 13
pygame.draw.rect(window, (190, 91, 89), (325, 0, 25, 25))
# Cor 14
pygame.draw.rect(window, (0, 139, 139), (350, 0, 25, 25))
# Cor 15
pygame.draw.rect(window, (166, 70, 62), (375, 0, 25, 25))




colorAtual = black
#
pygame.display.flip()




def desenha_linha(x1,y1):
    fundo_padrao = window.copy()

    print("aqui desenahndo")
    while 1: 
        for event in pygame.event.get():
            x2,y2 = pygame.mouse.get_pos()
            print('antes do if')
            window.blit(fundo_padrao,(0,0))
            bresenham(window, x1, y1, x2, y2, colorAtual)
            window.blit(fundo_padrao, (0, 0), (0, 0, 800, 50))
            if event.type == pygame.MOUSEBUTTONUP:
                print('saindo')
                return



def desenha_quadrado(x1,y1):
    fundo_padrao = window.copy()

    print("aqui desenahndo")
    while 1: 
        for event in pygame.event.get():
            x2,y2 = pygame.mouse.get_pos()
            print('antes do if')
            window.blit(fundo_padrao,(0,0))
            quadrado(window, x1, x2, y1, y2, colorAtual)
            window.blit(fundo_padrao, (0, 0), (0, 0, 800, 50))
            if event.type == pygame.MOUSEBUTTONUP:
                print('saindo')
                return

def dsesenha_circulo(x1,y1):
    fundo_padrao = window.copy()
    while 1: 
        for event in pygame.event.get():
            x2,y2 = pygame.mouse.get_pos()
            print('antes do if')
            window.blit(fundo_padrao,(0,0))
            raio = int(math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2)))

            circulo(window, x1, y1, raio, colorAtual)
            window.blit(fundo_padrao, (0, 0), (0, 0, 800, 50))
            if event.type == pygame.MOUSEBUTTONUP:
                print('saindo')
                return



def desenha_retangulo(x1,y1):
    fundo_padrao = window.copy()

    print("aqui desenahndo")
    while 1: 
        for event in pygame.event.get():
            x2,y2 = pygame.mouse.get_pos()
            print('antes do if')
            window.blit(fundo_padrao,(0,0))
            retangulo(window, x1, y1, x2, y2, colorAtual)
            window.blit(fundo_padrao, (0, 0), (0, 0, 800, 50))
            if event.type == pygame.MOUSEBUTTONUP:
                print('saindo')
                return




def linha_to_poli(x1,y1):
    fundo_padrao = window.copy()

    print("aqui desenahndo")
    while 1: 
        for event in pygame.event.get():
            x2,y2 = pygame.mouse.get_pos()
            print('antes do if')
            window.blit(fundo_padrao,(0,0))
            bresenham(window, x1, y1, x2, y2, colorAtual)
            window.blit(fundo_padrao, (0, 0), (0, 0, 800, 50))
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.display.update()
                fundo_padrao = window.copy()
                (x1,y1) = (x2,y2)
                click_direito = pygame.mouse.get_pressed()
                
                if click_direito[2] ==1:
                    print('saindo')
                    return


def desenha_poli(x1,y1):
    while 1:
        for e in pygame.event.get():
            if (e.type == pygame.MOUSEBUTTONDOWN):
                x1,y1 = pygame.mouse.get_pos()
                linha_to_poli(x1,y1)
                return


def desenha_bezier(x1,y1):
    fundo_padrao = window.copy()

    noPosition = True
    while noPosition:
        for e in pygame.event.get():
            if (e.type == pygame.MOUSEBUTTONDOWN):
                pos1= pygame.mouse.get_pos()
                noPosition = False
                break

    noPosition = True
    while noPosition:
        for e in pygame.event.get():
            if (e.type == pygame.MOUSEBUTTONDOWN):
                pos2= pygame.mouse.get_pos()
                noPosition = False
                break
    
    noPosition = True
    while noPosition:
        for e in pygame.event.get():
            if (e.type == pygame.MOUSEBUTTONDOWN):
                pos3 = pygame.mouse.get_pos()
                window.blit(fundo_padrao,(0,0))
                bezier(window,pos1,pos2,pos3,colorAtual)
                window.blit(fundo_padrao, (0, 0), (0, 0, 800, 50))
                return





def muda_botao(x,y):
    global primitiva
    global colorAtual

    if (x>0 and x <25) and (y>25 and y<50):
        print('mudado pra linha')
        primitiva = 1
    
    if(x>25 and x<50) and (y>25 and y<50):
        print('mudando para quadrado')
        primitiva = 2

    if(x>50 and x<75) and (y>25 and y<50):
        print('mudando para retangulo')
        primitiva = 3

    if(x>75 and x<100) and (y>25 and y<50):
        print('mudando para circulo')
        primitiva = 4

    if(x>100 and x<125) and (y>25 and y<50):
        print('mudando para polilinha')
        primitiva = 5

    if(x>125 and x<150) and (y>25 and y<50):
        print('mudando para bezier')
        primitiva = 6

    #0
    if (x>0 and x <25) and (y>0 and y<25):
        colorAtual = black
    #1
    if (x>25 and x <50) and (y>0 and y<25):
        colorAtual = (169, 169, 169)
    #2  
    if (x>50 and x <75) and (y>0 and y<25):
        colorAtual = (0, 0, 255)
    #3
    if (x>75 and x <100) and (y>0 and y<25):
        colorAtual = (255, 255,  0)
    
    #4
    if (x>100 and x <125) and (y>0 and y<25):
        colorAtual = (255, 0,  0)
    #5
    if (x>125 and x <150) and (y>0 and y<25):
        colorAtual =  (255, 0, 0)
    
    #6
    if (x>150 and x <175) and (y>0 and y<25):
        colorAtual =  (0, 255, 0)
    #7
    if (x>175 and x <200) and (y>0 and y<25):
        colorAtual = (255, 105, 180)
    #8  
    if (x>200 and x <225) and (y>0 and y<25):
        colorAtual =  (255, 140, 0)
    #9
    if (x>225 and x <250) and (y>0 and y<25):
        colorAtual =  (0, 191, 255)
    #10
    if (x>250 and x <275) and (y>0 and y<25):
        colorAtual =  (255, 191, 0)
    #11
    if (x>275 and x <300) and (y>0 and y<25):
        colorAtual =  (255, 191, 0)
    #12
    if (x>300 and x <325) and (y>0 and y<25):
        colorAtual =  (128, 0, 0)
    #13 
    if (x>325 and x <350) and (y>0 and y<25):
        colorAtual =  (128, 0, 0)
    #14 
    if (x>350 and x <375) and (y>0 and y<25):
        colorAtual = (138, 0, 138)
    #15
    if (x>375 and x <400) and (y>0 and y<25):
        colorAtual = (190, 91, 89) 





def click_handle(x,y):
    print('handling')
    print (primitiva)

    if (y <50):
        muda_botao(x,y)


    if (primitiva == 1):
        print('desenha linha')
        desenha_linha(x,y)


    if(primitiva ==2):
        print('desenha quadrado')
        desenha_quadrado(x,y)

    if(primitiva ==3):
        desenha_retangulo(x,y)

    if(primitiva ==4):
        dsesenha_circulo(x,y)

    if(primitiva ==5):
        desenha_poli(x,y)
    
    if(primitiva ==6):
        desenha_bezier(x,y)




while 1:
    x,y = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            click_handle(x,y)
    
    pygame.display.update()
