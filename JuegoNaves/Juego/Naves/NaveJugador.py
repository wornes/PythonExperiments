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
from threading import Thread
from time import sleep
from pygame.locals import *
from .InterfazNave import InterfazNave
class NaveJugador(InterfazNave):
    image = pygame.image.load("Engine/Graphics/Images/spaceship.png")
    def __init__(self):
        self.x = 0
        self.y = 100
        self.posicion = self.x,self.y
        self.velocidad=0
        self.disparos = []
        self.setImageSize()
        self.move(0)
    def checkEvents(self, keys):
        if keys[pygame.K_SPACE]:
            self.disparar()
        if keys[pygame.K_UP]:
            self.move(-1)
        if keys[pygame.K_DOWN]:
            self.move(1)
    def move(self, velocidad):
        if (velocidad >0) and self.y<600:
            self.y=self.y+velocidad
            print(self.y)
        elif velocidad <0 and self.y>0:
            self.y=self.y+velocidad
            print(self.y)
        self.posicion = self.x, self.y


##        self.y=self.y+self.velocidad
##        self.posicion = self.x,self.y+self.velocidad
##        if self.y >= 600:
##            self.velocidad =-1
##        elif self.y==0:
##            self.velocidad=1
