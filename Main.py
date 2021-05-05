from Node import *
from TicTacToe import *
from MCTS import *



class main:



    def play(self):

        ticTac = TicTacToe(['1','2','3','4','5','6','7','8','9'])        # instance du jeu
        Simulation = TicTacToe(['1','2','3','4','5','6','7','8','9'])            # instance de jeu utilisant MCTS ( afin de generer l'arbre)
        root = Nodes(None, None, None)  # creation de l'arbre
        mcts= Mcts(Simulation, root, 1)


        #print(" hors du while winner is none")

        while(ticTac.winner == None):

            print("dans le while  winner is none")

            ValeurJouer = ticTac.play(1)                #   ici  demander au joueur de jouer


            #Simulation.board = ticTac.board              # mettre la simualtion est dans le meme etat que le jeu
            Simulation.state.pop(Simulation.state.index(str(ValeurJouer)))

            print("verrifier si le noeud existe")

            if mcts.find_Node(root, ValeurJouer) == False:              # voir si le noeud existe deja si non le créer
                print("creation du noeud  ")
                Node = Nodes(None, root, ValeurJouer)
                root.children.append(Node)

            else:
                print(" le noeud existe on pointe vers lui")

                Node = mcts.find_Node(root, ValeurJouer)            # se diriger vers le noeud deja existant


            print("si le noued n'as pas de fils")

            if Node.children == []:

                print("   le noued n'as pas de fils")
                Node.add_children(Simulation)                   # pour ajouter les fils du noeud
                print("les enfants ajoutés sont :",Node.children)


            Iteration = 0

            while Iteration < 10:
                print("while iterations   ")

                Selected_Node = mcts.Select_Node(Node)

                if Selected_Node.Visits == 0:
                    '''
                    si le noeud n'est pas exploré
                    faire un rollout
                    '''

                    Number_Rollout = mcts.Number_Rollout

                    for i in range(Number_Rollout):
                        print( "rollout N°: ",i)

                        Score = mcts.rollout(Simulation, Selected_Node)

                        print(" rollout done N:",i )

                        '''
                        ensuite on fais une back propagation

                        '''
                        mcts.BackPropagation(Selected_Node, Score)
                        print(" apres backpropagation ")


                else:
                    '''
                    si le noeud est deja exploré
                    faire une expension

                    '''
                    print(" avant expension")
                    mcts.expand_Node(Simulation, Selected_Node)
                    print(" apres expension")
                Iteration += 1

                '''
                 apres les 500 iterations au tour de l'ordinateur de jouer
                '''
            print("this is state: ", ticTac.state)
            MaxUCBNode = mcts.selectMove(Node)
            print("this is max ucb selected:  ",MaxUCBNode.value)
            print("this is the board ",ticTac.board)
            print("Simulation  board ", Simulation.board)



            ticTac.play(2, MaxUCBNode.value)                          # l'ordinateur joue le noeud ayant la plus grande valeur
            Simulation.board = ticTac.board
            Simulation.state = ticTac.state

            if mcts.find_Node(Node, MaxUCBNode.value) == False:  # voir si le noeud existe deja si non le créer

                Node = Nodes(None, Node, ValeurJouer)
                Node.children.append(Node)

            else:
                Node = mcts.find_Node(root, ValeurJouer)  # se diriger vers le noeud deja existant
                root = Node








main= main()
main.play()


