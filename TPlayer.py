from TicTacToe import *

class Tplayer:

    def __init__(self):



        '''
        {'board': [" ", " ", " ", " ", " ", " ", " ", " ", " "], 'nextPlayer' : "X"}
        '''

    def Player1Move(self, game: Game, currentGameState):


        result = game.play(currentGameState)
        return  {'board': result['board'], 'nextPlayer': "0", 'value': result['value']}