from Node import *
from TicTacToe import *
from TPlayer import *
from MCTS import *



class main:




    '''def testerTicTacToe(self,game:Game):
        game.play1(2,4)
        print(game.state)
    '''

    #ticTac: Objet jeux, contient les méthodes "nextMoves"  # possible moves

    def play(self, game: Game):

                #declarations

        tictac = TicTacToe()
        currentGameState = {'board': [" ", " ", " ", " ", " ", " ", " ", " ", " "], 'nextPlayer' : "X", 'value':None}
        player1 = Tplayer()         #demander au joueur 1 de joueur
        mcts = Mcts(tictac, 1)
        mcts.CurrentGameNode = mcts.initialize(currentGameState)       # créer la racine et les fils de la racine


        lastMCTSState = currentGameState

        while tictac.winner == None:
            # jeux joueur 1

          currentGameState = player1.Player1Move(game, currentGameState)

            # jeux ordinateur
          currentGameState = mcts.ComputerPlay(game, lastMCTSState, currentGameState)
          lastMCTSState = currentGameState









main= main()
TicTacToe = TicTacToe()
main.testerTicTacToe(TicTacToe)


