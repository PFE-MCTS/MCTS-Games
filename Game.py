class Game:
 
    def __init(self):
        self.Turn=1             # turn=1 >>> joueur blanc turn=2 >>>> joueur noir
        self.winner=None    # 0 si null
        self.state=None
    ''' abstract class'''
 
    def possibleMoves(self):
        '''
        contient les mouvements possible a effectuer
                a un instant T du jeu par un joueur
 
        '''

    def play(self):
 
        ''' 
        fonction qui fais le jeu
                invoque la fonction possibleMoves() pour jouer
 
                '''
 
    def HasWon(self)->int:
 
        '''
        fonction donnant le resultat d'une partie 
        retourne le numéro du joueur ayant gagné  (1 ou 2)
        si partie nulle retourne 0
 
        '''
    