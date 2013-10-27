#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Wornes
#
# Created:     16/09/2013
# Copyright:   (c) Wornes 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys, pygame, pygame.mixer
from pygame.locals import *
from .Sounds import Sounds
from .Events import Events
from .Graphics import Graphics
from Juego.Juego import Juego

class Engine:
    def __init__(self):
        #TESTING
        juego = Juego()
        #END OF TESTING
        #Crea una variable sound
    ##    sound = pygame.mixer.Sound('Engine/Sounds/SoundFiles/bubble.wav')
        laser = pygame.mixer.Sound('Engine/Sounds/SoundFiles/laser.wav')
        #Crea un reloj. El reloj permite controlar los frames a los que se mueve el
        #programa, ya que si no se mueve a la velocidad que te permita el procesador.
        clock = pygame.time.Clock()

    ##    #Reproduce la variable sound
    ##    sound.play()
        #Crea una variable con dos atributos int
        size = width, height = 800, 700
        #color (rgb) negro usado para limpiar la pantalla
        black = 0,0,0
        #Una variable ventana
        screen = pygame.display.set_mode(size)

        bg = pygame.image.load("Engine/Graphics/Images/bg.jpg").convert()
        bg = pygame.transform.scale(bg,size)
    ##    #carga una imagen
    ##    ship2 = pygame.image.load("Engine/Graphics/Images/spaceship2.png")
    ##    ship = pygame.image.load("Engine/Graphics/Images/spaceship.png")
    ##    #Cambia el tamanio de la imagen
    ##    ship = pygame.transform.scale(ship,(100,100))
    ##    ship2 = pygame.transform.scale(ship2,(100,100))
        x = 0
        y = 0
        #r = 0
        g = 0
        b = 0
        mx,my = pygame.mouse.get_pos()
        while 1:
                #recoge la posicion del raton en mx y my
                #mx,my = pygame.mouse.get_pos()
                #imprime en la consola mx
                #print(mx)
##                print((pygame.key.get_pressed()))

                for event in pygame.event.get():
                        #Cierra la ventana cuando le damos a la equis
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        #Cierra la ventana cuando le damos al escape
                        elif event.type == KEYDOWN and event.key == K_ESCAPE:
                            pygame.quit()
                            sys.exit()
                        #Cierra la ventana cuando le damos a la q
                        elif event.type == KEYDOWN and event.key == K_q:
                            pygame.quit()
                            sys.exit()
##                        #Reproduce la variable laser cuando apretamos el boton del raton
##                        elif event.type == MOUSEBUTTONDOWN:
##                            mx,my = pygame.mouse.get_pos()
##                        #Guarda una screenshot. Puede ser necesario poner la extension
##                        #para que lo guarde correctamente.
##                        elif event.type == KEYDOWN and event.key == K_SPACE:
##    ##                        pygame.image.save(screen,"screenshot.png")
##                            juego.checkEvents(event)
##                            Sounds.playSound(laser)
##                        else:
##                             juego.checkEvents(event)
                #"limpia" la ventana, poniendola a negro para evitar distorsiones
                # al moverse las imagenes
                #screen.fill(black)
                screen.blit(bg,(0,0))
                #blit nos sirve para incluir la imagen en la ventana
                #ponemos -50 para centrar la magen
                #screen.blit(ship2,(mx-50,my-50))
                #Las imagenes cargadas primero se muestran al fondo en la ventana
                #screen.blit(ship,(x,y))
                #TESTING:
                juego.moveObjects()
                keys = pygame.key.get_pressed()
                juego.checkEvents(keys)
##                juego.pressedKeys(keys[pygame.K_UP],keys[pygame.K_DOWN])
                for nave in juego.naves:
                    screen.blit(nave.image,nave.posicion)
                    for disparo in nave.disparos:
                        screen.blit(disparo.image,disparo.posicion)
                #END OF TESTING:
                #Hacemos que funcione cada 60 frames o algo asi, para ralentizarlo
                clock.tick(60)
                #flip refresca la pantalla, si no se pone no se muestran los cambios
                pygame.display.flip()


    ##            if x == 700:
    ##                    x1=-1
    ##            elif x==0:
    ##                    x1=1
    ##            if y == 600:
    ##                    y1=-1
    ##            elif y==0:
    ##                    y1=1
    ##            x=x+x1
    ##            y=y+y1
                #Si r>255 da error, asi que lo controlamos con el if
               # if r == 255:
               #         r1=-1
                       #sound.play()
               # elif r==0:
               #         r1 = 1
                        #sound.play()
               # r = r+r1
