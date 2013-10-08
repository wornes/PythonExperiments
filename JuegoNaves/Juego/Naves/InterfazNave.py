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
from Disparo import Disparo

class InterfazNave:
    x=0
    y=0
    posicion = x, y
    velocidad = 1
    disparos = []
    image =pygame.image.load("Engine/Graphics/Images/spaceship.png")
    def __init__(self):
        self.posicion = 100,100
    def move(self):
        self.y=self.y+self.velocidad
        self.posicion = self.x,self.y+self.velocidad
        if self.y >= 600:
            self.velocidad =-1
        elif self.y==0:
            self.velocidad=1
    def setVelocidad(self, velocidad):
        self.velocidad=velocidad
    def setImageSize(self):
        self.image = pygame.transform.scale(self.image,(100,100))
    def disparar(self):
        self.disparos.append(Disparo(self.x+100,self.y+50))
    def checkEvents(self, keys):
        self
