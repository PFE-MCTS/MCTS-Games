from Node import *
from Game import *
from TicTacToe import *

from MCTS import *
import numpy as np


root=Nodes(None,None,0)

child1=Nodes(None,root,1)
child2=Nodes(None,root,2)
child4=Nodes(None,child1,3)
child3=Nodes(None,child2,4)

root.children.append(child1)
root.children.append(child2)
child2.children.append(child3)
child2.children.append(child4)

mcts=Mcts(Game, root, 0)

print(mcts.get_ActualState(child4))

'''partie= Game()
partie.play()
'''


'''mcts.BackPropagation(child4, partie)

print("Game.Score=", partie.Score)
print("Child 1 score= ",child1.Score)
print("child1 Visits=",child1.Visits)

print(" root Score ", root.Score)

print("root visites ", root.Visits)

mcts.select_leaf(root)
print(mcts.LeafList[0].value)
game = Game()'''

'''
mcts.expand_Node(game, child4)

print(child4.__dict__)
'''


'''print(root.children)
print(child2.children)
'''


class main:



    '''

    cette version est une version sans Base de donnés

    quand cette version marchera elle sera modifiée afin de stocker l'arbre dans une BDD

    '''

    def play(self):
        ticTac = TicTacToe()        # instance du jeu
        root = Nodes(ticTac.possibleMoves(),None,None)  # creation de l'arbre
        root.add_children(ticTac)
        mcts= Mcts(ticTac, root, 1)



        while(ticTac.winner is None):

            #   ici  demander au joueur de jouer

            ValeurJouer = "1"  # en fonction de la valeur jouée par le joueur
            Node=Nodes(None, root, ValeurJouer)  # ajouter condition pour voir si le noeud exite deja pas besoin de le créer

            # ajouter le fils et le pére

            Iteration = 0
            while Iteration is not 500:

                if Node.children == []:
                    ticTac.possibleMoves()  # mechi blassetha
                    # on dois creer les noueds des mouvements possibles ici si ils ne sont pas deja creé


                Selected_Node = mcts.Select_Node(Node)

                if Selected_Node is float('inf'):
                    '''
                    si le noeud n'est pas exploré
                    faire un rollout
                    '''
                    mcts.rollout(ticTac, Selected_Node)

                    '''
                    ensuite on fais une back propagation

                    '''

                    mcts.BackPropagation(Selected_Node, Game)

                else:
                    '''
                    si le noeud est deja exploré
                    faire une expension

                    '''

                    mcts.expand_Node(Game, Selected_Node)

                Iteration += 1

                '''
                 apres les 500 iterations au tour de l'ordinateur de jouer
                '''
            MaxUCB = mcts.Select_Node(Selected_Node)

            # jouer le noeud ayant le max UCB










