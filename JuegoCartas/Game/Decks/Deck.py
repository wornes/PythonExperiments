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
import Game.Cards.Card as Card
class Deck:

    def __init__(self, support=False, tactics = False):
        if support is False:
            self.support=False
        else:
            self.support=support
        if tactics is False:
            self.tactics=False
        else:
            self.tactics=tactics

