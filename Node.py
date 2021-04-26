from Game import Game
class Nodes:
 
    def __init__(self,parent,children,moves):
        self.parent=None
        self.children=[]
        self.Visits=0
        self.Score=0
        self.moves=moves #array
 
    def is_leaf(self)->bool:
        '''
        méthode verrifiant si le noeud est une feuille
        si le noeud est une feuille elle retourne true
        sinon elle retourne false
        
        '''
    
    def is_terminal(self, Game)->bool:
        ''' Méthode qui verrifie si le noeud est terminal
 
        si noeud terminal return true
        sinon return false
        
        '''
    
    def add_children(self, Game):
 
            '''méthode qui ajoute au noeud de l'instance un fils'''
    
    def find_Random_Child(self, move:Game):
        '''trouver un fils aléatoirement'''