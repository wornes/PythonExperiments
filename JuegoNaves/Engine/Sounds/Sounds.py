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
from Engine.Events import Events
from Engine.Graphics import Graphics
from Juego import *

def playSound(sound):
    sound.play()
