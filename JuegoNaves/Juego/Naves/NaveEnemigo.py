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
from InterfazNave import InterfazNave
class NaveEnemigo(InterfazNave):
    image = pygame.image.load("Engine/Graphics/Images/spaceship2.png")
    def __init__(self):
        self.x = 700
        self.y = 100
        self.posicion = self.x,self.y
        self.velocidad=1
        self.disparos = []
        self.setImageSize()
