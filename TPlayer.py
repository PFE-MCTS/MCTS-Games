from TicTacToe import *

class Tplayer:

    def __init__(self):



        '''
        {'board': [" ", " ", " ", " ", " ", " ", " ", " ", " "], 'nextPlayer' : "X",'value': '1:9'}
        '''

    def Player1Move(self, game: Game, currentGameState):


        result = game.play(currentGameState)
        return result

    def Playerinterface(self, game: Game, currentGameState, coup):
        result = game.play(currentGameState, coup)

        return result