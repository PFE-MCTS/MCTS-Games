from Node import *
from TicTacToe import *
from TPlayer import *
from MCTS import *



class main:




    def testerTicTacToe(self,game:Game):
        game.play1(2,4)
        print(game.state)



    def play(self, game: Game):

                    #declarations

        ticTac = TicTacToe(['1','2','3','4','5','6','7','8','9'])        # instance du jeu
        player1 = Tplayer()         #demander au joueur 1 de joueur
        mcts = Mcts(ticTac, Nodes(None, None, None), 1)


        # initialisation mcts
        mcts.root.add_children(ticTac)          # Ajouter des fils a la racine
        ActualState = mcts.root

        while game.winner == None:


            # jeux joueur 1
         DeplacementJoueur = player1.Player1Move(game)
         ActualState = mcts.find_Node(ActualState, DeplacementJoueur)

            # jeux ordinateur
         deplacementordinateur = mcts.ComputerPlay(game, ActualState)
         ActualState = mcts.find_Node(ActualState, deplacementordinateur)







main= main()
TicTacToe = TicTacToe()
main.testerTicTacToe(TicTacToe)


