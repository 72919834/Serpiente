import pygame
from pygame.locals import*
import sys
import grafitero
import time

pygame.init()
ventana=pygame.display.set_mode((800,600))
pygame.display.set_caption("SERPIENTE: By Baxon")
g=grafitero.grafica()

fase=0
seleccionmenu=0
orientacion=0
Pcomida=(200,200)
puntuacion=0

while True:
    if fase==0:
       g.fondo()
       g.titulo(seleccionmenu)
    elif fase ==1:
        g.fondo()
        Pcomida, puntuacion=g.DibujarSnake(orientacion, Pcomida, puntuacion)
        g.comida(Pcomida)
        puntuacion=g.score(puntuacion)
        pass
    elif fase ==2:
        g.fondo()
        g.creditos()
        pass
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
            pass
        elif evento.type == KEYDOWN:
            if fase==0:
                if evento.key ==pygame.k_DOWN:
                    if seleccionmenu <1:
                        seleccionmenu+=1
                    else:
                        seleccionmenu=0
                elif evento.key==pygame.K_UP:
                    if seleccionmenu>0:
                        seleccionmenu -=1
                else:
                    seleccionmenu=1
            elif evento.key==pygame.K_z:
                if seleccionmenu==0:
                    fase=1
                elif seleccionmenu==1:
                    fase=2
            elif fase==1:
                if evento.key==pygame.K_DOWN and orientacion !=90:
                   orientacion=270
                if evento.key==pygame.K_UP and orientacion !=270:
                    orientacion=90
                if evento.key==pygame.K_LEFT and orientacion!=0:
                    orientacion=270
                if evento.key==pygame.K_RIGHT and orientacion!=180:
                    orientacion=0
            elif fase==2:
                if evento.key==pygame.K_x:
                    fase=0
            elif evento.type==KEYUP:
                pass



