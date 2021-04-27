import math

from Node import *
from Game import *
        
class Mcts:
    
    def __init__(self, game, root: Nodes, number_rollout):
        self.game = game
        self.NbrParties = 0
        self.Score = 0
        self.root = root
        self.runtime = 0
        self.rolloutDone = 0
        self.Number_Rollout = number_rollout
    
 
    def Select_Node(self) -> int:
        '''
            phase de selection des noeuds en applicant UCB 
        '''
        leafList=[]
        if(self.root.is_leaf()):
            return 1
        else:
            self.root.children



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
        #NbrVisitesRacines=self.root.Visits
        return node.Score / node.Visits + 2 * math.sqrt(math.log(self.root.Visits)/node.Visits)
 
    def BackPropagation(self, rolloutnode: Nodes):
        
        ''' 
        phase de backpropagation du score et du nombre de visites
 
        '''
