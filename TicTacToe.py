from Game import *
class TicTacToe (Game):



    def __init__(self,state=['1','2','3','4','5','6','7','8','9']):
        self.turn = 1
        self.player1 = "X"
        self.player2 = "O"
        self.winner = None
        self.state = state  # état du jeu ( les cases restantes)
        self.Score = 0
        self.board = [" ", " ", " ",
                      " ", " ", " ",
                      " ", " ", " "]



    def possibleMoves(self, board=None):
        '''
        fonction a utiliser lors du rollout, prends en parametre l'etat actuel du noeud ainsi que le noeud
        :return: une liste de mouvements possibles
        '''

        if board == None:
            return self.state
        else:
            possibleMove=[]
            for parcours in board:
                if parcours ==" ":
                    possibleMove.append(board.index(parcours))

            return possibleMove



    def display_state(self):
        print(self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        print(self.board[3] + " | " + self.board[4] + " | " + self.board[5])
        print(self.board[6] + " | " + self.board[7] + " | " + self.board[8])

    def change_player(self):

        if self.turn == 1:
            self.turn = 2
        elif self.turn == 2:
            self.turn = 1


    def play(self,turn,Coup=None):
        if(turn == 1):
            position = input(" Choissisez une position entre (1 et 9): ")
            while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                position = input("Position incorrecte, Choissisez une position entre (1 et 9): ")

            index = self.state.index(str(position))
            self.state.pop(index)
            position = int(position) - 1
            if self.board[position] != " ":
                raise RuntimeError("Mouvement incorrecte")

            self.board[position] = "X"
            self.display_state()
            self.HasWon()
        else:

            index = self.state.index(str(Coup))
            self.state.pop(index)
            position = int(Coup) - 1
            if self.board[position] != " ":
                raise RuntimeError("Mouvement incorrecte")

            self.board[position] = "O"
            self.display_state()
            self.HasWon()

        return position


    def simulation(self, board, nextTurn):
        pass

    '''def play1(self, turn, coup=None):


        self.turn = turn

        if coup is None:
                    #instance de jeu
            position = input(" Choissisez une position entre (1 et 9): ")
            while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                position = input("Position incorrecte, Choissisez une position entre (1 et 9): ")
        else:
           #instance de simulation
            position = coup
                                           
        index = self.state.index(str(position))
        self.state.pop(index)

        position = int(position) - 1

        if self.board[position] != " ":
            raise RuntimeError("Mouvement incorrecte")

        if self.turn == 1:
            self.board[position] = "X"
        elif self.turn == 2:
            self.board[position]="O"

        self.display_state()
        print("Les possibles moves restants :" + str(self.state))
        self.HasWon()

        if self.winner is None:
            self.change_player()
        elif self.winner is not None:
            if self.winner == 0:
                print("Match nul " + str(self.winner))
            else:
                print("Joueur " + str(self.winner) + " a gagné")

        return position
'''
            

    def HasWon(self, board = None) -> int:

        if board == None:
            # rows
            if self.board[0] == self.board[1] == self.board[2] != " ":
                if self.board[0] == "X":
                    self.winner = 1
                elif self.board[0] == "O":
                    self.winner = 2
            if self.board[3] == self.board[4] == self.board[5] != " ":
                if self.board[3] == "X":
                    self.winner = 1
                elif self.board[3] == "O":
                    self.winner = 2
            if self.board[6] == self.board[7] == self.board[8] != " ":
                if self.board[6] == "X":
                    self.winner = 1
                elif self.board[6] == "O":
                    self.winner = 2

            # columns
            if self.board[0] == self.board[3] == self.board[6] != " ":
                if self.board[0] == "X":
                    self.winner = 1
                elif self.board[0] == "O":
                    self.winner = 2
            if self.board[1] == self.board[4] == self.board[7] != " ":
                if self.board[1] == "X":
                    self.winner = 1
                elif self.board[1] == "O":
                    self.winner = 2
            if self.board[2] == self.board[5] == self.board[8] != " ":
                if self.board[2] == "X":
                    self.winner = 1
                elif self.board[2] == "O":
                    self.winner = 2

            # diagonals
            if self.board[0] == self.board[4] == self.board[8] != " ":
                if self.board[0] == "X":
                    self.winner = 1
                elif self.board[0] == "O":
                    self.winner = 2
            if self.board[2] == self.board[4] == self.board[6] != " ":
                if self.board[2] == "X":
                    self.winner = 1
                elif self.board[2] == "O":
                    self.winner = 2

            if " " not in self.board and self.winner is None:
                self.winner = 0

            if (self.winner == 1):
                self.Score = -1  # utilisateur gagne

            elif self.winner == 2:
                self.Score = 1  # computer gagne

            else:
                self.Score = 0

            return self.winner
        else:                                   # cas de simulation on introduis un paramettre board
            # rows
            if board[0] == board[1] == board[2] != " ":
                if board[0] == "X":
                    return -1
                elif self.board[0] == "O":
                    return +1
            if board[3] == board[4] == board[5] != " ":
                if board[3] == "X":
                    return -1
                elif board[3] == "O":
                    return +1
            if board[6] == board[7] == board[8] != " ":
                if board[6] == "X":
                    return -1
                elif board[6] == "O":
                    return +1

            # columns
            if board[0] == board[3] == board[6] != " ":
                if board[0] == "X":
                    return -1
                elif self.board[0] == "O":
                    return 1
            if board[1] == board[4] == board[7] != " ":
                if board[1] == "X":
                    return -1
                elif board[1] == "O":
                    return 1
            if board[2] == board[5] == board[8] != " ":
                if board[2] == "X":
                    return -1
                elif board[2] == "O":
                    return 1

            # diagonals
            if board[0] == board[4] == board[8] != " ":
                if board[0] == "X":
                    return -1
                elif board[0] == "O":
                    return +1
            if board[2] == board[4] == board[6] != " ":
                if board[2] == "X":
                    return -1
                elif board[2] == "O":
                    return +1

            if " " not in board:
                return 0        # match nul
            else:
                return None             # demander a aziz de tester surtout le cas ou il ya pas de vainqueur pour le moment












