from Game import *
class TicTacToe (Game):



    def possibleMoves(self):
        '''
        fonction a utiliser lors du rollout, prends en parametre l'etat actuel du noeud ainsi que le noeud
        :return: une liste de mouvements possibles
        '''
        return self.state

    def display_state(self):
        print(self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        print(self.board[3] + " | " + self.board[4] + " | " + self.board[5])
        print(self.board[6] + " | " + self.board[7] + " | " + self.board[8])

    def change_player(self):

        if self.turn == 1:
            self.turn = 2
        elif self.turn == 2:
            self.turn = 1

    def play(self, turn, coup=None):


        self.turn = turn

        if coup is None:
            #instance de play
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

            

    def HasWon(self) -> int:

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
            self.Score = 1 #utilisateur gagne

        elif self.winner == 2:
            self.Score = -1 #computer gagne

        else:
            self.Score = 0

        return self.winner



#test=TicTacToe()
#test.play(1)




