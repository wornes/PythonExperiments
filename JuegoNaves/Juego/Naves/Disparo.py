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

class Disparo:
    x=0
    y=0
    posicion = x, y
    velocidad = 3
    image =pygame.image.load("Engine/Graphics/Images/laser.png")
    def __init__(self,x,y):
##        self.image =pygame.image.load("Engine/Graphics/Images/laser.png")
        self.x=x
        self.y=y
        self.velocidad=8
        self.posicion = x,y
    def move(self):
        self.x=self.x+self.velocidad
        self.posicion = self.x,self.y
        if self.x >= 700:
            del self
    def setVelocidad(self, velocidad):
        self.velocidad=velocidad
