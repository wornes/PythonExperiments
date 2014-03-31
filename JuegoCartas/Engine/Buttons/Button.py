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
from pygame.rect import *

class Button:

    def __init__(self, x=0, y=0, width=0, height=0):
        self.buttonRectangle= Rect(x,y,width,height)
    def isMouseOver(self,x=0,y=0):
        return self.buttonRectangle.collidePoint(x,y)
    def setText(self, text):
        self.text=text
    def getRect(self):
        return self.buttonRectangle
    def getText(self):
        return self.text



