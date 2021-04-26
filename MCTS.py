from Node import *
from Game import *
        
class Mcts:
    
    def __init__(self,game,root:Nodes,Number_Rollout):
        self.game=game
        self.NbrParties=0
        self.Score=0
        self.root=root
        self.runtime=0
        self.numberOfrolloutdone=0
        self.Number_Rollout=Number_Rollout
    
 
    def Select_Node(self)->int:
        '''
            phase de selection des noeuds en applicant UCB 
        '''
    
    '''def select_leaf(self):
       
        selection de feuille aléatoirement
         pour faire un rollout
         
         '''
    def expand_Node(self,Moves:Game,node:Nodes):
        '''
        phase d'expansion de l'arbre de recherche
        induis a lajout de fils (children au noeud en parametres)
 
        '''
 
    def rollout(self,game:Game,leaf:Nodes)->int:
        
        '''
        phase de rollout(simulation)
        le parametre Number_Rollout definis le nombre de simulations a faire
        appel de la fonction select_leaf()
        appel a la fonction de haswon() de la classe game
        le resultat du rollout est un score entier
 
        '''
 
 
    def UCT(self,node:Nodes)->float:
        
        ''' calcul de l'UCT a travers la formule UCB '''
 
    def BackPropagation(self,rolloutNode:Nodes):
        
        ''' 
        phase de backpropagation du score et du nombre de visites
 
        '''
