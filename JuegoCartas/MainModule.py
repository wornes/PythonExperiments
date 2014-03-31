#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Wornes
#
# Created:     15/02/2014
# Copyright:   (c) Wornes 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Necesario para iniciar pygame:
import sys, pygame, pygame.mixer
from pygame.draw import *
from pygame.surface import Surface
from pygame.locals import *
#from Game import Board,Player
from Engine.Buttons.Button import *
pygame.init()

exit = False
startGame = False

#Crea una variable con dos atributos int
size = width, height = 1024, 768
buttonWidth = width/5
buttonHeight = height/10
#color (rgb) negro usado para limpiar la pantalla
black = 0,0,0
purple = 130,0,200
#Crea un reloj. El reloj permite controlar los frames a los que se mueve el
#programa, ya que si no se mueve a la velocidad que te permita el procesador.
clock = pygame.time.Clock()
#Una variable ventana
screen = pygame.display.set_mode(size)
background =pygame.display.set_mode(size)
#Buttons:
startGameButton = Button(width/2-width/10,height/4,buttonWidth,buttonHeight)
exitButton = Button(width/2-width/10,height/2,buttonWidth,buttonHeight)
#Text for the buttons
myfont = pygame.font.SysFont("monospace", 15)
labelStartGame = myfont.render("Start Game", 1, (255,255,0))
labelExit = myfont.render("Exit to desktop", 1, (255,255,0))
#Run
while not exit:
    ''' Leer boton pulsado'''
    'Dos botones: Start Game y Exit.'
    'Dos cuadros de texto: Jugador1 y Jugador2 para incluir el nombre'
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            exit= exitButton.getRect().collidepoint(pygame.mouse.get_pos())
            if startGameButton.getRect().collidepoint(pygame.mouse.get_pos()):
                labelStartGame = myfont.render("GAME STARTED", 1, (255,255,0))

    #"limpia" la ventana, poniendola a negro para evitar distorsiones
    # al moverse las imagenes
    #screen.fill(black)
##    screen.blit(background,(0,0))
    #Draw Buttons
    pygame.draw.rect(background,purple,startGameButton.getRect(),1)
    pygame.draw.rect(background,purple,exitButton.getRect(),1)
    #Draw text
    screen.blit(labelStartGame, startGameButton.getRect().midleft)
    screen.blit(labelExit, exitButton.getRect().midleft)
    #Hacemos que funcione cada 60 frames o algo asi, para ralentizarlo
    clock.tick(60)
    #flip refresca la pantalla, si no se pone no se muestran los cambios
    pygame.display.flip()
pygame.quit()
sys.exit()