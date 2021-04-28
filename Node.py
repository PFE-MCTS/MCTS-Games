import random

from Game import *
class Nodes:
 
    def __init__(self, moves, parent:object, value=None):
        self.parent = parent
        self.children = []
        self.Visits = 0
        self.Score = 0
        self.moves = moves #array
        self.value=value


    def is_leaf(self) -> bool:
        '''
        méthode verrifiant si le noeud est une feuille
        si le noeud est une feuille elle retourne true
        sinon elle retourne false
        '''

        if(self.children == []):
            return True
        else:
            return False






    
    def is_terminal(self, Game) -> bool:
        ''' Méthode qui verrifie si le noeud est terminal
 
        si noeud terminal return true
        sinon return false
        
        '''
    
    def add_children(self, game: Game):
        for move in game.possibleMoves():
            self.children.append(Nodes(None, self, move))


    
    def find_Random_Child(self, move: Game):
        '''trouver un fils aléatoirement'''
        return random.choice(move.possibleMoves())
