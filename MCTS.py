from copy import deepcopy
import math
import random

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
        root.currentGameState = deepcopy(currentGameState)
        self.root = root
        #Ajoute les premiers fils
        self.root.add_children(game, currentGameState)
        self.CurrentGameNode = deepcopy(root)
        return self.CurrentGameNode

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
        NbrVisites = 0
        MaxNode = None
        if actualNode.children != []:
            for node in actualNode.children:
                if NbrVisites <= node.Visits:
                    NbrVisites = deepcopy(node.Visits)
                    MaxNode = node

            return MaxNode
        else:
            print(" exception dans selectMove()")





    def Select_Node(self, root: TNode):
        '''
            phase de selection des noeuds en applicant UCB
            fonction recursive
        '''
                            # condition si le noeud a un fils is leaf
        if root != None:
            if root.children == []:
                return root
            else:
                UTC = float('-inf')
                MaxNode = None
                for node in root.children:
                    if (self.UCT(node) >= UTC):
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




    def expand_Node(self, game: Game, node: TNode):
        '''
        phase d'expansion de l'arbre de recherche
        induis a lajout de fils (children au noeud en parametres)
 
        '''
        state = deepcopy(node.currentGameState)
        board = deepcopy(node.currentGameState['board'])
        if(node.is_terminal(game, board) == False):
            if node.is_leaf():
                node.add_children(game, state)
        else:
            return None




    def rollout(self, game: Game, leaf: TNode, NumberRollout=1):
        '''
        phase de rollout(simulation)
        le parametre Number_Rollout definis le nombre de simulations a faire
        appel a la fonction de haswon() de la classe game
        le resultat du rollout est un score entier
        '''
        Scorefinal =0
        for i in range(NumberRollout):
            state = deepcopy(leaf.currentGameState)
            board = deepcopy(leaf.currentGameState['board'])
            while game.HasWon(board) == None:

                move = random.choice(game.possibleMoves(board))
                state = game.play(state, move, 1)
                board = state['board'][:]
            Scorefinal += game.HasWon(board)
        return Scorefinal


    def UCT(self, node: TNode) -> float:
        
        ''' calcul de l'UCT a travers la formule UCB '''
        if node.Visits == 0:
            return float('inf')
        else:

            return (node.Score / node.Visits) + 2 * (math.sqrt(math.log(self.NbrParties)/node.Visits) )



    def BackPropagation(self, rolloutnode: TNode, score):
        
        ''' 
        phase de backpropagation du score et du nombre de visites
 
        '''
        if rolloutnode.parent == None:
            rolloutnode.Visits += 1
            rolloutnode.Score += score
            self.Score += score
            self.NbrParties += 1
        else:
            rolloutnode.Visits += 1
            rolloutnode.Score += score
            self.BackPropagation(rolloutnode.parent, score)



    def ApplyMCTS(self,game: Game, currentNode: TNode):

        iteration = 0
        while iteration < 500:

            #print(currentNode)
            if currentNode.children == []:
                currentNode.add_children(game, currentNode.currentGameState)

            SelectedNode = self.Select_Node(currentNode)        # phase de selection
            if SelectedNode.Visits == 0:
                Score = self.rollout(game, SelectedNode)        # phase de rollout
                self.BackPropagation(SelectedNode, Score)       #phase de backpropagation

            else:
                self.expand_Node(game, SelectedNode)        #phase d'expension

            iteration += 1


    def ComputerPlay(self, game: Game,currentMctsState ,currentNode: TNode):

        #print(currentNode.currentGameState['board'])
        print("children",currentNode.children)
        print("dict",currentNode.currentGameState)
        #print(game.possibleMoves())
        self.CurrentGameNode = self.find_Node(currentNode, currentMctsState['value'])

        self.ApplyMCTS(game, self.CurrentGameNode)

        ComputerMove = self.selectMove(self.CurrentGameNode)
        currentMctsState = game.play(currentMctsState, ComputerMove.currentGameState['value'])


        self.CurrentGameNode = self.find_Node(self.CurrentGameNode, currentMctsState['value'])

        return currentMctsState
