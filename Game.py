class Game:

    def __init__(self):
        self.turn=1
        self.winner=None
        self.state=None

    
   



 
    def possibleMoves(self):

        self.state=['1','2','3','4','5','6','7','8','9']
        return self.state        

    
    def display_state(self):
        print(board[0]+" | "+board[1]+" | "+board[2])
        print(board[3]+" | "+board[4]+" | "+board[5])
        print(board[6]+" | "+board[7]+" | "+board[8])




    
    def change_player(self):
        
        if self.turn==1:
            self.turn=2
        elif self.turn==2:
            self.turn=1




    def play(self):
        
        self.possibleMoves()
        self.display_state()

        while self.winner is None:
            position=input(" Choissisez une position entre (1 et 9): ")

            while position not in ['1','2','3','4','5','6','7','8','9']:
                position=input("Position incorrecte, Choissisez une position entre (1 et 9): ")
            

            index=self.state.index(str(position))
            self.state.pop(index)

            position=int(position)-1
            if board[position] != " ":
                raise RuntimeError("Mouvement incorrecte")

            if self.turn==1:
                board[position]="X"
            elif self.turn==2:
                board[position]="O"
            
            self.display_state()
            print("Les possibles moves restants :" + str(self.state))
            self.HasWon()
            
            if self.winner is None:
                self.change_player()
            elif self.winner is not None:
                if self.winner == 0:
                    print("Match nul "+str(self.winner))
                else:
                    print("Joueur "+str(self.winner)+" a gagné")
                        
    
    def HasWon(self):
        
        #rows
        if board[0]==board[1]==board[2]!=" ":
            if board[0]=="X":
                self.winner=1
            elif board[0]=="O":
                self.winner=2
        if board[3]==board[4]==board[5]!=" ":
            if board[3]=="X":
                self.winner=1
            elif board[3]=="O":
                self.winner=2
        if board[6]==board[7]==board[8]!=" ":
            if board[6]=="X":
                self.winner=1
            elif board[6]=="O":
                self.winner=2

        #columns
        if board[0]==board[3]==board[6]!=" ":
            if board[0]=="X":
                self.winner=1
            elif board[0]=="O":
                self.winner=2
        if board[1]==board[4]==board[7]!=" ":
            if board[1]=="X":
                self.winner=1
            elif board[1]=="O":
                self.winner=2
        if board[2]==board[5]==board[8]!=" ":
            if board[2]=="X":
                self.winner=1
            elif board[2]=="O":
                self.winner=2

        #diagonals
        if board[0]==board[4]==board[8]!=" ":
            if board[0]=="X":
                self.winner=1
            elif board[0]=="O":
                self.winner=2
        if board[2]==board[4]==board[6]!=" ":
            if board[2]=="X":
                self.winner=1
            elif board[2]=="O":
                self.winner=2
        
        if " " not in board:
            self.winner=0

        

board=[" "," "," ",
       " "," "," ",
       " "," "," "]


test=Game()
test.play()