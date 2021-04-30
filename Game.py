from abc import ABC, abstractmethod
class Game(ABC):

    def __init__(self, state=['1','2','3','4','5','6','7','8','9']):
        self.turn=1
        self.winner=None
        self.state=state            #état du jeu ( les cases restantes)
        self.Score=0
        self.board = [" ", " ", " ",
                 " ", " ", " ",
                 " ", " ", " "]






    @abstractmethod
    def possibleMoves(self):
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
    def play(self):

        pass

    @abstractmethod
    def HasWon(self)-> int:

       pass

        



'''test=Game()
test.play()
'''