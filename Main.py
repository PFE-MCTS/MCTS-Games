from Node import *
from TicTacToe import *
from MCTS import *



class main:



    '''

    cette version est une version sans Base de donnés

    quand cette version marchera elle sera modifiée afin de stocker l'arbre dans une BDD

    '''

    def play(self):

        ticTac = TicTacToe()        # instance du jeu
        Simulation = TicTacToe()            # instance de jeu utilisant MCTS ( afin de generer l'arbre)
        root = Nodes(None, None, None)  # creation de l'arbre
        mcts= Mcts(Simulation, root, 1)



        while(ticTac.winner == None):

            ValeurJouer = ticTac.play(1)                #   ici  demander au joueur de jouer
            Simulation.board = ticTac.board              # mettre la simualtion est dans le meme etat que le jeu
            Simulation.state = ticTac.state




            if mcts.find_Node(root, ValeurJouer) == False:              # voir si le noeud existe deja si non le créer

                Node = Nodes(None, root, ValeurJouer)
                root.children.append(Node)

            else:
                Node = mcts.find_Node(root, ValeurJouer)            # se diriger vers le noeud deja existant




            if Node.children == []:
                Node.add_children(Simulation)                   # pour ajouter les fils du noeud


            Iteration = 0

            while Iteration is not 500:


                Selected_Node = mcts.Select_Node(Node)

                if Selected_Node.Visits == 0:
                    '''
                    si le noeud n'est pas exploré
                    faire un rollout
                    '''

                    Number_Rollout = mcts.Number_Rollout

                    for i in range(Number_Rollout):

                        Score = mcts.rollout(Simulation, Selected_Node)

                        '''
                        ensuite on fais une back propagation

                        '''
                        mcts.BackPropagation(Selected_Node, Score)



                else:
                    '''
                    si le noeud est deja exploré
                    faire une expension

                    '''

                    mcts.expand_Node(Simulation, Selected_Node)

                Iteration += 1

                '''
                 apres les 500 iterations au tour de l'ordinateur de jouer
                '''
            MaxUCBNode = mcts.selectMove(Node)

            ticTac.play(2, MaxUCBNode.value)                          # l'ordinateur joue le noeud ayant la plus grande valeur
            Simulation.board = ticTac.board
            Simulation.state = ticTac.state

            if mcts.find_Node(Node, MaxUCBNode.value) == False:  # voir si le noeud existe deja si non le créer

                Node = Nodes(None, Node, ValeurJouer)
                Node.children.append(Node)

            else:
                Node = mcts.find_Node(root, ValeurJouer)  # se diriger vers le noeud deja existant
                root = Node










