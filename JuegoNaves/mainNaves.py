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
#Necesario para iniciar pygame:
import sys, pygame, pygame.mixer, JuegoNaves.Engine.Engine
from pygame.locals import *

pygame.init()
JuegoNaves.Engine.Engine.Engine()