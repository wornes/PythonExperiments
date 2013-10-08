#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Wornes
#
# Created:     28/09/2013
# Copyright:   (c) Wornes 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys, pygame, pygame.mixer
from pygame.locals import *
from Naves.InterfazNave import InterfazNave
from Naves.NaveEnemigo import NaveEnemigo
from Naves.NaveJugador import NaveJugador


class Juego:
    naveJugador = NaveJugador()
    naveEnemigo = NaveEnemigo()
    naves=[naveJugador,naveEnemigo]
    def __init__(self):
        self.naveJugador = NaveJugador()
        self.naveEnemigo = NaveEnemigo()
        self.naves=[self.naveJugador,self.naveEnemigo]
    def moveObjects(self):
        self.naveEnemigo.move()
        for nave in self.naves:
            for disparo in nave.disparos:
                disparo.move()
    def checkEvents(self,keys):
        for nave in self.naves:
            nave.checkEvents(keys)

    def pressedKeys(self, up, down):
        if up:
            self.naveJugador.move(-1)
        if down:
            self.naveJugador.move(1)

