from piece import Raja
from piece import Ghoda
from piece import Hati
from piece import Bishop
from piece import Wazir
from piece import Payada

class Board:
    def __init__(self,rows,cols):
        self.rows = rows
        self.cols= cols

        self.board = [[ 0 for x in range(8)]  for _ in range(rows)]

    

        self.board[0][0] = Hati(0, 0, "B")
        self.board[0][1] = Ghoda(0, 1, "B")
        self.board[0][2] = Bishop(0, 2, "B")
        self.board[0][3] = Wazir(0, 3, "B")
        self.board[0][4] = Raja(0, 4, "B")
        self.board[0][5] = Bishop(0, 5, "B")
        self.board[0][6] = Ghoda(0, 6, "B")
        self.board[0][7] = Hati(0, 7, "B")
        
        # FOR WHITE6
        self.board[7][0] = Hati(7, 0, "w")
        self.board[7][1] = Ghoda(7, 1, "w")
        self.board[7][2] = Bishop(7, 2, "w")
        self.board[7][3] = Wazir(7, 3, "w")
        self.board[7][4] = Raja(7, 4, "w")
        self.board[7][5] = Bishop(7, 5, "w")
        self.board[7][6] = Ghoda(7, 6, "w")
        self.board[7][7] = Hati(7, 7, "w")

        # PAWN PLOT FOR BLACK
        for i in range(8):
            self.board[1][i] = Payada(1, i, "B")

        # PAWN PLOT FOR WHITE
        for i in range(8):
            self.board[6][i] = Payada(6, i, "w") 
   
    def draw(self,WINDOW):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    self.board[i][j].draw(WINDOW)
    
    def select(self,cols,rows):
        prev = (-1,-1)
        for i in range(self.rows):
                for j in range(self.cols):
                    if self.board[i][j] != 0:
                        if self.board[i][j].selected:
                            prev = (i,j)
        # if peice 
        if self.board[rows][cols] == 0:
            moves = self.board[prev[0]][prev[1]].move_list
            if (cols,rows) in moves:
                self.move(prev,(rows,cols))
            self.reset_selected()
        else:
            self.reset_selected()
            self.board[rows][cols].selected = True

    def reset_selected(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    self.board[i][j].selected = False
                   

    def move(self,start,end):
        newBoard = self.board[:]
        newBoard[start[0]][start[1]].changePos((end[0],end[1]))
        newBoard[end[0]][end[1]] = newBoard[start[0]][start[1]]
        newBoard[start[0]][start[1]] = 0
        self.board = newBoard
    
    def update_moves(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    self.board[i][j].updateValidMoves(self.board)