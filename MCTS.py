import math

from Node import *
from Game import *
        
class Mcts:
    LeafList = []       #global var
    
    def __init__(self, game, root: Nodes, number_rollout):
        self.game = game
        self.NbrParties = 0
        self.Score = 0
        self.root = root
        self.runtime = 0
        self.rolloutDone = 0
        self.Number_Rollout = number_rollout


    def select_leaf(self, root: Nodes):            # probleme retourne None
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






    def Select_Node(self, root: Nodes) -> int:          #pas encore testé
        '''
            phase de selection des noeuds en applicant UCB 
        '''
        # condition si le noeud a un fils is leaf
        valeurUCT = 0
        MaxNode = None
        while root.children is not []:

            for node in root.children:
                if valeurUCT <= self.UCT(node):
                    valeurUCT = self.UCT(node)
                    MaxNode = node
                else:
                    pass
            root = MaxNode

        return MaxNode



    def expand_Node(self, moves: Game, node: Nodes):
        '''
        phase d'expansion de l'arbre de recherche
        induis a lajout de fils (children au noeud en parametres)
 
        '''
        if node.is_leaf():
            node.add_children(moves)


    def get_ActualState(self, node: Nodes):
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




    def rollout(self, game: Game, leaf: Nodes) -> int:
        
        '''
        phase de rollout(simulation)
        le parametre Number_Rollout definis le nombre de simulations a faire
        appel de la fonction select_leaf()
        appel a la fonction de haswon() de la classe game
        le resultat du rollout est un score entier
 
        '''

        game.possibleMoves()






 
 
    def UCT(self, node: Nodes) -> float:
        
        ''' calcul de l'UCT a travers la formule UCB '''
        if node.Visits ==0:
            return float('inf')
        else:
            return node.Score / node.Visits + 2 * math.sqrt(math.log(self.root.Visits)/node.Visits)



    def BackPropagation(self, rolloutnode: Nodes, score: Game):
        
        ''' 
        phase de backpropagation du score et du nombre de visites
 
        '''
        while rolloutnode.parent is not None:
            rolloutnode.Visits += 1
            rolloutnode.Score += score.Score
            rolloutnode = rolloutnode.parent

        self.root.Visits += 1
        self.Score += score.Score
        self.root.Score += score.Score







