from Game import *
import chess
class chessGame (Game):



    def __init__(self,state=None):
        self.turn = 1
        self.player1 = "BLACK"                  # Ordinateur
        self.player2 = "WHITE"                  # joueur
        self.winner = None
        self.state = state  # état du jeu ( les cases restantes)
        self.Score = 0
        self.board = chess.Board()


        '''
        p= pion
        r= tour 
        n= 
        b=fous
        q= reine
        k=rois
        
        
         CurrentGameState de type : {Board:  
        r n b q k b n r
        p p p p p p p p
        . . . . . . . .
        . . . . . . . .
        . . . . . . . .
        . . . . . . . .
        P P P P P P P P
        R N B Q K B N R,
                     nextPlayer: " Black", 'value':''
                }
        
            '''

    def possibleMoves(self, board=None):
        '''
        fonction a utiliser lors du rollout, prends en parametre l'etat actuel du noeud ainsi que le noeud
        :return: une liste de mouvements possibles
        '''

        if board == None:
            moves = list(self.board.legal_moves)
            return moves
        else:
            moves = list(board.legal_moves)
            return moves





    def display_state(self,board):          # y ajouter une interface
        pass

    def change_player(self):
        pass


    def play(self, currentGameState, Coup=None, Rollout=None):
        GameTurn = currentGameState['nextPlayer']
        board = currentGameState['board']
        if Rollout == None:
            if (GameTurn == "Black"):                                                   # tour du joueur

                # ici   interface !!!!

                position = 1
                board[position] = "X"
                currentGameState['board'] = board
                #self.display_state(board)           # interface
                self.HasWon(board)

                return {'board': board, 'nextPlayer': "0", 'value': position + 1}
            else:                                                                       # tour de l'ordinateur

                board.push(Coup)
                next_player = self.Nextplayer(board)

                #self.display_state(board)              # interface

                self.HasWon(board)
                return {'board': board, 'nextPlayer': next_player, 'value': Coup}

        else:                                                                           # rollout
            print("dans le rollout")
            board = currentGameState['board']
            board.push(Coup)
            next_player = self.Nextplayer(board)
            return {'board': board, 'nextPlayer': next_player, 'value': Coup}


    def Nextplayer(self, board):
        '''

        :param board:
        afin davoir le prochain a jouer
        :return:  "black" ou "White"
        '''
        if board.turn == chess.BLACK:
            return "BLACK"
        else:
            return "WHITE"



    def HasWon(self, board=None):                  # a revoir pour indiquer le vrai gagnant
        if board == None:
            resultat = self.board.outcome()
            if resultat == None:
                return None                 # pas encore de vainqueur                   (A REVOIR)
            elif resultat.winner == True:  # white won
                self.winner = 1
                return +1
            elif resultat.winner == False:      #  black won
                self.winner = 2
                return -1  # black won
            else:
                self.winner = 0
                return 0                        # draw

        else:
            resultat = board.outcome()
            if resultat == None:
                return None  # pas encore de vainqueur                   (A REVOIR)
            elif resultat.winner == True:  # white won
                self.winner = 1
                return +1
            elif resultat.winner == False:  # black won
                self.winner = 2
                return -1  # black won
            else:
                self.winner = 0
                return 0  # draw














