import database
from Node import *
from TicTacToe import *
from chessGame import *
from TPlayer import *
from MCTS import *
from database import *


class main:



    '''def play(self, game, database):

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





    def chess_play(self, game, database):
        # declarations

        chess = chessGame()
        currentGameState = {'board': deepcopy(chess.board), 'nextPlayer': "WHITE", 'value': None}
        player1 = Tplayer()
        mcts = Mcts(chess, 1)
        mcts.CurrentGameNode = mcts.initialize(chess, currentGameState, database)  # créer la racine et les fils de la racine
        lastMCTSState = currentGameState

        while chess.winner == None:
            # jeux joueur 1
            currentGameState = player1.Player1Move(game, currentGameState)

            chess.HasWon(currentGameState['board'])

            print("chess.winner",chess.winner)
            if (chess.winner == None):
                print("in chess.winner\n")
                # jeux ordinateur
                currentGameState = mcts.ComputerPlay(game, currentGameState, mcts.CurrentGameNode)

                print("after mcts.computer play\n")
                lastMCTSState = deepcopy(currentGameState)
                chess.HasWon(currentGameState['board'])

        print("the winner is the player", chess.winner)
        data = connection("chess")
        deleteTree(data)
        updateTreesearch(data, mcts.root)
'''



    def tictacTraining(self, Nbrpartie:int):
        tictac = TicTacToe()
        currentGameState = {'board': [" ", " ", " ", " ", " ", " ", " ", " ", " "], 'nextPlayer': "X", 'value': None}
        mcts = Mcts(tictac, 1)
        mcts.CurrentGameNode = mcts.initialize(tictac, currentGameState,
                                               "tictactoe")  # créer la racine et les fils de la racine

        for i in range(Nbrpartie):
            while tictac.HasWon(currentGameState['board']) == None:
                # jeux joueur 1

               # premier joueur MCTS

                currentGameState= mcts.ComputerVsComputer(tictac, currentGameState)

                if (tictac.HasWon(currentGameState['board']) == None):

                    currentGameState = mcts.ComputerVsComputer(tictac, currentGameState)
                    lastMCTSState = deepcopy(currentGameState)
                    tictac.HasWon(currentGameState['board'])

            print("the winner is the player", tictac.HasWon(currentGameState['board']))
            print("\n the final board", currentGameState['board'])
            currentGameState = {'board': [" ", " ", " ", " ", " ", " ", " ", " ", " "], 'nextPlayer': "X",
                                'value': None}
            mcts.CurrentGameNode = mcts.root
            print("root.visits", mcts.root.Visits)
            for node in mcts.root.children:
                '''print("children value", node.value)
                print("children visits", node.Visits)
                print("children Score", node.Score)'''

            data = connection("tictactoe")
            deleteTree(data)
            updateTreesearch(data, mcts.root)








    def chessTraining(self, Nbrpartie):
        jeu = chessGame()
        currentGameState = {'board': deepcopy(jeu.board), 'nextPlayer': "WHITE", 'value': None}
        mcts = Mcts(jeu, 1)
        mcts.CurrentGameNode = mcts.initialize(jeu, currentGameState,
                                               "chess")  # créer la racine et les fils de la racine

        for i in range(Nbrpartie):
            while jeu.HasWon(currentGameState['board']) == None:
                # jeux joueur 1

                # premier joueur MCTS

                currentGameState = mcts.ComputerVsComputer(jeu, currentGameState)

                if (jeu.HasWon(currentGameState['board']) == None):
                    currentGameState = mcts.ComputerVsComputer(jeu, currentGameState)
                    lastMCTSState = deepcopy(currentGameState)
                    tictac.HasWon(currentGameState['board'])

            print("the winner is the player", jeu.HasWon(currentGameState['board']))
            print("\n the final board", currentGameState['board'])
            currentGameState = {'board': [" ", " ", " ", " ", " ", " ", " ", " ", " "], 'nextPlayer': "X",
                                'value': None}
            mcts.CurrentGameNode = mcts.root

            # for testing
            print("root.visits", mcts.root.Visits)
            for node in mcts.root.children:
                '''print("children value", node.value)
                print("children visits", node.Visits)
                print("children Score", node.Score)'''

            data = connection("chess")
            deleteTree(data)
            updateTreesearch(data, mcts.root)


main= main()


tictac = TicTacToe()
main.tictacTraining(50)

#main.chessTraining(10)






'''# jeu tic tac toe
tictac = TicTacToe()
main.play(tictac, "tictactoe")



# jeu chess

jeu = chessGame()
main.chess_play(jeu, "chess")
'''




