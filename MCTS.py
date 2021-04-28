import math

from Node import *
from Game import *
        
class Mcts:
    LeafList = []
    
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
        if root.children == []:
            self.Arr.append(root)
        else:
            for child in root.children:
                self.select_leaf(child)






    def Select_Node(self) -> int:
        '''
            phase de selection des noeuds en applicant UCB 
        '''


        print(self.select_leaf(self.root))
        #print(leafList)




    def expand_Node(self, moves: Game, node: Nodes):
        '''
        phase d'expansion de l'arbre de recherche
        induis a lajout de fils (children au noeud en parametres)
 
        '''
 
    def rollout(self, game: Game, leaf: Nodes) -> int:
        
        '''
        phase de rollout(simulation)
        le parametre Number_Rollout definis le nombre de simulations a faire
        appel de la fonction select_leaf()
        appel a la fonction de haswon() de la classe game
        le resultat du rollout est un score entier
 
        '''
 
 
    def UCT(self, node: Nodes) -> float:
        
        ''' calcul de l'UCT a travers la formule UCB '''

        return node.Score / node.Visits + 2 * math.sqrt(math.log(self.root.Visits)/node.Visits)
 
    def BackPropagation(self, rolloutnode: Nodes):
        
        ''' 
        phase de backpropagation du score et du nombre de visites
 
        '''
