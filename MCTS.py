import math

from Node import *
from TicTacToe import *
        
class Mcts:

    LeafList = []       #global var
    
    def __init__(self, game, number_rollout):
        self.game = game
        self.NbrParties = 0
        self.Score = 0
        self.root = None         # pour l'instant a revoir
        self.runtime = 0
        self.rolloutDone = 0
        self.Number_Rollout = number_rollout
        self.PreviousGameNode = None
        self.CurrentGameNode = None

        '''
        GameState : {Board: ["X", "O", "X",
                      " ", "O", "O",
                      " ", " ", " "],
             Player: "O"
        }
        '''


    def initialize(self, game:Game, currentGameState):
        # creer la racine
        board = currentGameState['board'][:]
        root = TNode(None, board, None)
        self.root = root
        #Ajoute les premiers fils
        self.root.add_children(game, currentGameState)
        return self.root

    def select_leaf(self, root: TNode):             # a supprimer apres
        '''
        retourne tous les fils existants
        :return:
        '''
        if root is None:
            return []
        if root.is_leaf():
            self.LeafList.append(root)
        else:
            for child in root.children:
                self.select_leaf(child)



    def selectMove(self,actualNode: TNode):
        valeurUCT = 0
        MaxNode = None
        if actualNode.children != []:
            for node in actualNode.children:
                if valeurUCT <= self.UCT(node):
                    valeurUCT = self.UCT(node)
                    MaxNode = node

            return MaxNode
        else:
            print(" exception dans selectMove()")





    def Select_Node(self, root: TNode):
        '''
            phase de selection des noeuds en applicant UCB 
        '''
                            # condition si le noeud a un fils is leaf
        if root.children == []:
            return root
        else:
            UTC = 0
            MaxNode = None
            for node in root.children:
                if (self.UCT(node) > UTC):
                    UTC = self.UCT(node)
                    MaxNode = node
            return self.Select_Node(MaxNode)







    def find_Node(self, node:TNode, valeur):

        if(node.children != []):
            for node in node.children:
                if node.currentGameState['value'] == valeur:
                    return node


        else:
            return False




    def expand_Node(self, moves: Game, node: TNode):  # expension a revoir
        '''
        phase d'expansion de l'arbre de recherche
        induis a lajout de fils (children au noeud en parametres)
 
        '''
        board = node.getBoard()
        if(node.is_terminal(moves, board) == False):
            if node.is_leaf():
                node.add_children(moves)




    def get_ActualState(self, node: TNode):             # a revoir ou supprimer
        '''
        fonction servant a donner l'état du jeu  a partir d'un noeud afin de faire un rollout
        prends en paramettre le noeud,
        :return: une liste de valeurs des noeuds
        '''
        ActualState=[]

        while node.parent is not None:
            ActualState.append(node.value)
            node = node.parent

        return ActualState




    def rollout(self, game: Game, leaf: TNode) -> int:              # a revoir
        
        '''
        phase de rollout(simulation)
        le parametre Number_Rollout definis le nombre de simulations a faire
        appel de la fonction select_leaf()
        appel a la fonction de haswon() de la classe game
        le resultat du rollout est un score entier
 
        '''
        while game.winner == None:
            if game.turn == 1:
                game.play(2, random.choice(game.possibleMoves()))
                game.turn = 2
            else:
                game.play(1, random.choice(game.possibleMoves()))
                game.turn = 1
        return game.Score


    def UCT(self, node: TNode) -> float:
        
        ''' calcul de l'UCT a travers la formule UCB '''
        if node.Visits == 0:
            return float('inf')
        else:
            return (node.Score / node.Visits) + 2 * (math.sqrt(math.log(self.root.Visits)/node.Visits) )



    def BackPropagation(self, rolloutnode: TNode, score):
        
        ''' 
        phase de backpropagation du score et du nombre de visites
 
        '''
        while rolloutnode.parent is not None:
            rolloutnode.Visits += 1
            rolloutnode.Score += score
            rolloutnode = rolloutnode.parent

        self.root.Visits += 1
        self.Score += score
        self.root.Score += score


    def ApplyMCTS(self,game: Game, currentNode: TNode):

        iteration = 0
        while iteration < 50:

            if currentNode.children == []:
                currentNode.add_children(game)

            SelectedNode = self.Select_Node(currentNode)


            if SelectedNode.Visits == 0:
                Score = self.rollout(game, SelectedNode)

                self.BackPropagation(SelectedNode, Score)

            else:
                self.expand_Node(game, SelectedNode)


            iteration += 1

    '''
        def ApplyMCTS(self, game: Game, currentNode: TNode):

        iteration = 0
        while iteration < 50:

            if currentNode.children == []:
                currentNode.add_children(game, currentNode.currentGameState)

            SelectedNode = self.Select_Node(currentNode)

            if SelectedNode.Visits == 0:
                Score = self.rollout(game, SelectedNode)

                self.BackPropagation(SelectedNode, Score)

            else:
                self.expand_Node(game, SelectedNode)

            iteration += 1

    '''

    def ComputerPlay(self, game: Game,lastState,currentMctsState ,currentNode: TNode):

        self.CurrentGameNode = self.find_Node(currentNode, currentMctsState['value'])
        self.applyMCTS(game, self.CurrentGameNode)

        ComputerMove = self.selectMove(self.CurrentGameNode)
        currentMctsState = game.play(currentMctsState, ComputerMove.currentGameState['value'])


        self.CurrentGameNode = self.find_Node(currentNode, currentMctsState['value'])

        return currentMctsState


        '''         #Precondition: CurrentGameNode.currentGameState == lastMCTSState
    def ComputerPlay(self,game:Game ,lastMCTSState, currentGameNode:TNode):

        # on ajoute le noeud joué par le joueur

        #on fais mcts
        self.applyMCTS(game,currentGameNode)

        ComputerMove = self.selectMove(currentNode)
        game.play(2, ComputerMove.value)

        # on ajoute le noued joué par l'ordinateur
        return {'board': board, 'nextPlayer': "0", 'value': result['value']}
        '''
