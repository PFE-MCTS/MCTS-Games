import random

from Game import *
class Nodes:
 
    def __init__(self, moves, parent: object, value=None):
        self.parent = parent
        self.children = []
        self.Visits = 0
        self.Score = 0
        self.value = value
        self.CurrentGameState = None

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

    '''def getBoard(self, simulation: Game, boardTemplate):
        
        méthode donnant l'état du jeu a travers un noeud donné
        :return: un dictionnaire {"board"=[], "NextPlayer" }
        '''



    def getNodeDepth(self):
        count = 0
        while self.parent != None:
            count += 1
            self = self.parent

        return count





    
    def is_terminal(self, game:Game, board) -> bool:               # a revoir
        ''' Méthode qui verrifie si le noeud est terminal
 
        si noeud terminal return true
        sinon return false
        
        '''
        if game.HasWon(board) == None:
            return False
        else:
            return True


    def add_children(self, game: Game):
        for move in game.possibleMoves():
            self.children.append(Nodes(None, self, move))

