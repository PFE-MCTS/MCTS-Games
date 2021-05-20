import database
from Node import *
from TicTacToe import *
from TPlayer import *
from MCTS import *
from database import *


class main:




    '''def testerTicTacToe(self,game:Game):
        game.play1(2,4)
        print(game.state)
    '''

    #ticTac: Objet jeux, contient les méthodes "nextMoves"  # possible moves

    def play(self, game, database):

                #declarations

        tictac = TicTacToe()
        currentGameState = {'board': [" ", " ", " ", " ", " ", " ", " ", " ", " "], 'nextPlayer' : "X", 'value': None}
        player1 = Tplayer()
        mcts = Mcts(tictac, 1)
        mcts.CurrentGameNode = mcts.initialize(tictac, currentGameState, database)       # créer la racine et les fils de la racine


        lastMCTSState = currentGameState

        while tictac.winner== None:
            # jeux joueur 1

          currentGameState = player1.Player1Move(game, currentGameState)

          tictac.HasWon(currentGameState['board'])

          if(tictac.winner==None):
              # jeux ordinateur
              currentGameState = mcts.ComputerPlay(game, currentGameState, mcts.CurrentGameNode)
              lastMCTSState = deepcopy(currentGameState)
              tictac.HasWon(currentGameState['board'])

        print("the winner is the player", tictac.winner)
        data = connection("tictactoe")
        deleteTree(data)
        updateTreesearch(data, mcts.root)

    def chess_play(self,game):
        pass






main= main()
tictac = TicTacToe()
main.play(tictac, "tictactoe")




