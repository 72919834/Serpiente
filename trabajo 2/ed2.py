import pygame
from pygame.locals import*
import random
pygame.init()

Ventana=pygame.display.set_mode((800,600))
VerdeFondo=(80,120,80)
VerdeObjeto=(30,40,30)
VerdeObjetoClaro=(50,60,50)

Fuente_Titulo=pygame.font.Font("Font/PressStart2P,ttf", 50)
Fuente_Menu=pygame.font.Font("Font/PressStart2p.ttf", 25)
Fuente_Texto=pygame.font.Font("Font/PressStart2p.ttf", 15)

Titulo= Fuente_Titulo.render("Classic Snake", True, VerdeObjeto)
UnJugador= Fuente_Menu.render("Un Jugador", True,VerdeObjeto)
creditos=Fuente_Menu.render("creditos", True, VerdeObjeto)
InstruccionMenu = Fuente_Texto.render("prexione x para entrar a la opcion", True, VerdeObjeto)
InstruccionMenu2 = Fuente_Texto.render("precione z para volver al menu", True, VerdeObjeto)
Creditos1=Fuente_Texto.render("Este juego fue desarrollado por", True, VerdeObjeto)
Creditos2=Fuente_Texto.render("Eduardo Jose, para no bickear CS1100", True, VerdeObjeto)
Creditos3=Fuente_Texto.render("comer para ganar...", True, VerdeObjeto)
score = Fuente_Texto.render("Score: ", True, VerdeObjeto)

secciones =[(80,80),(80,100),(80,120),(80,140),(80,160),(100,160)]

class grafica(object):
    def _init_(self):
            print("Nuevas aplicaciones")
            pass
    def Fondo(slef):
        Ventana.fill(VerdeFondo)
    def Titulo(self, seleccion):
            if seleccion==0:
                pygame.draw.rect(Ventana,VerdeObjetoClaro,(110,200,300,30))
            elif seleccion ==1:
                pygame.draw.rect(Ventana, VerdeObjetoClaro,(110,230,300,30))
            Ventana.blit(Titulo,(80,50))
            Ventana.blit(UnJugador,(120,200))
            Ventana.blit(creditos, (120,230))
            Ventana.blit(InstruccionMenu, (10,550))
            pass
    def creditos(self):
     Ventana.blit(creditos, (120,230))
     Ventana.blit(Creditos1,(120,260))
     Ventana.blit(Creditos2, (120,200))
     Ventana.blit(Creditos3,(120,300))
     Ventana.blit(InstruccionMenu2, (10, 550))

    def DibujarSnake(self, orientacion,Pcomida, puntuacion):
                        for i in secciones:
                            pygame.draw.rect(Ventana.VerdeObejeto, (i[0]+1,i[1]+1, 18, 18))
                            if secciones.index(i)==len(secciones)-1:
                                if orientacion == 0:
                                    secciones.append((i[0]+20,i[1]))
                                elif orientacion == 90:
                                    secciones.append((i[0],i[1]-20))
                                elif orientacion == 180:
                                    secciones.append((i[0]-20,i[1]))
                                elif orientacion == 270:
                                    secciones.append((i[0],i[1]+20))
                                if i != Pcomida:
                                    del secciones[0]
                                    return (Pcomida, puntuacion)
                                else:
                                    puntuacion=puntuacion+1
                            return ((random.randit(0,39)*20,random.randit(0,29)*20), puntuacion)
                            break
                 def Pcomida(self,Pcomida):
                     pygame.draw.rect(Ventana,VerdeObjetoClaro,(Pcomida[0],Pcomida[1],18,18))

                     def score(self, puntuacion):
                         Ventana.blit(score,(10,10))
                         puntos=Fuente_Texto.render(str(puntuacion), True, VerdeObjetoClaro)
                         Ventana.blit(puntos, (150,10))
