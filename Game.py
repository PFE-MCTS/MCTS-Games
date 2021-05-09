from abc import ABC, abstractmethod
class Game(ABC):

    @abstractmethod
    def __init__(self):
        pass



    @abstractmethod
    def possibleMoves(self, board):
        '''
        fonction a utiliser lors du rollout, prends en parametre l'etat actuel du noeud ainsi que le noeud
        :return: une liste de mouvements possibles
        '''

        pass

    @abstractmethod
    def display_state(self):
        pass

    @abstractmethod
    def change_player(self):
        pass



    @abstractmethod
    def play(self, currentstate, coup=None, Rollout=None):

        pass

    @abstractmethod
    def HasWon(self)-> int:

       pass

        



