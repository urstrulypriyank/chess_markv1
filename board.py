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
        self.turn = "w"
        self.winner = None
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
    
    def select(self,cols,rows,color):
        self.turn = color
        changed = False
        prev = (-1,-1)
       
        
        for i in range(self.rows):
                for j in range(self.cols):
                    if self.board[i][j] != 0:
                        if self.board[i][j].selected:
                                prev = (i,j)
        
        self.reset_selected()
        if self.board[rows][cols] == 0:
            moves = self.board[prev[0]][prev[1]].move_list
            if (cols,rows) in moves:
                changed = self.move(prev,(rows,cols),color)
            self.reset_selected()
        else:
            if self.board[prev[0]][prev[1]].color != self.board[rows][cols].color:
                moves = self.board[prev[0]][prev[1]].move_list
                if (cols,rows) in moves:
                    self.reset_selected()
                    self.board[prev[0]][prev[1]].color = self.board[rows][cols].color
                    # self.update_moves()
                    self.reset_selected()
                    self.board[rows][cols].color = self.board[prev[0]][prev[1]]
                    changed = self.move(prev,(rows,cols),color)
                if self.board[rows][cols].color == color:
                    self.board[rows][cols].selected = True
                    self.update_moves()
                
                    
            else:
                if self.board[rows][cols].color == color:
                    self.board[rows][cols].selected = True
                    self.update_moves()
        # self.reset_selected()            
        return changed  

    def reset_selected(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    self.board[i][j].selected = False
                   

    def move(self,start,end,color):
        checkedBefore = self.isChecked(color)
        changed = True
        oldBoard = self.board[:]
        newBoard = self.board[:]
        if newBoard[start[0]][start[1]].Payada:
            newBoard[start[0]][start[1]].first = False
        newBoard[start[0]][start[1]].changePos((end[0],end[1]))
        newBoard[end[0]][end[1]] = newBoard[start[0]][start[1]]
        newBoard[start[0]][start[1]] = 0
        self.board = newBoard
        # self.reset_selected()

        if color == "w": checkColor = "B"
        else: checkColor = "w"

        # self.update_moves()
        if self.isChecked(color) or (checkedBefore and self.isChecked(color)):
            checkedBefore = self.isChecked(color)
            changed = False
            newBoard = self.board[:]
            if newBoard[end[0]][end[1]].Payada:
                newBoard[end[0]][end[1]].first = True
            newBoard[end[0]][end[1]].changePos((start[0],start[1]))
            newBoard[start[0]][start[1]] = newBoard[end[0]][end[1]]
            newBoard[end[0]][end[1]] = 0
            self.board = newBoard
        return changed  

    
    def update_moves(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    self.board[i][j].updateValidMoves(self.board)



    
    
    


    def isInCheck(self,color):
        under_check_proximity = []
        for i in range(self.rows):
                for j in range(self.cols):
                    if self.board[i][j] != 0:
                        if self.board[i][j].color != color:
                            for move in self.board[i][j].move_list:
                                under_check_proximity.append(move)
        return under_check_proximity



    def isChecked(self,color):
        self.update_moves()
        under_check_proximity = self.isInCheck(color)
        king_pos = (-1,-1)
        for i in range(self.rows):
                for j in range(self.cols):
                    if self.board[i][j] != 0:
                        if self.board[i][j].isKing and self.board[i][j].color == color:
                            king_pos = (j,i)
        if king_pos in under_check_proximity:
            return True
        return False
 
 
   # CHECK AND MATE

"""    def checkMate (self,color):
        under_check_proximity = self.isInCheck(color)
        king_moves = []
        block_moves = []
        for i in range(self.rows):
                for j in range(self.cols):
                    if self.board[i][j] != 0:
                            if self.board[i][j].color == color:
                                if self.board[i][j].isKing: 
                                    for move in self.board[i][j].move_list:
                                        king_moves.append(move)
                                else:
                                    for move in self.board[i][j].move_list:
                                        block_moves.append(move)

        
        if len(king_moves) == 0:
            return False
        for block in block_moves:
            under_check_moves = under_check_proximity[:]
            if block in under_check_proximity:
                under_check_moves.remove(block)
            
        for move in king_moves:
            if move not in under_check_proximity:
                return False
        return True
"""