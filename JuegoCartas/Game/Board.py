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
import JuegoCartas.Game.Player, JuegoCartas.Game.Decks,JuegoCartas.Game.Cards
class Board:

    def __init__(self, players):
        self.players=players
        'Llamar a los DeckAdapters/Factories en vez de a Deck directamente'
        self.supportDeck = Decks.Deck(support)
        self.tacticsDeck = Decks.Deck(tactics)
        self.setPlayersHands()
        self.runGame()

    def setPlayersHands():
        for player in self.players:
            player.setStartingHand()
    def runGame():
        while 1:
            ''' Ejecuta el juego por turnos
            1 - Fase de colocaciÃ³n: cada jugador pone uno a uno sus regimientos?
            2 - "Tirada inicial" para elegir evento (carga, atacante/defensor etc)
            3 - Robo de cartas iniciales (tÃ¡cticas)
            4 - Comienzo del turno:
                4.1 Se da la vuelta a las cartas de apoyo del turno anterior y se aplica su efecto?
                4.2 Se colocan las cartas (tÃ¡cticas y de apoyo)
                4.3 Se dan la vuelta a las cartas de tÃ¡cticas y se aplica su efecto.
                4.4 Se calculan los resultados del combate
                4.5 Se retiran las cartas utilizadas y se envÃ­an a sus pilas de descartes.
                4.6 Se retiran tambiÃ©n las cartas que hayan quedado sin usar en la mano.
                4.7 Se roban nuevas cartas
            '''


