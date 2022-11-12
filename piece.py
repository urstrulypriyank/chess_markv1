import pygame
import os

# WHITE GOTI
w_raja = pygame.image.load(os.path.join("images","raja_white.png"))
w_wazir = pygame.image.load(os.path.join("images","wazir_white.png"))
w_bishop = pygame.image.load(os.path.join("images","bw.png"))
w_ghoda = pygame.image.load(os.path.join("images","ghoda_white.png"))
w_hati = pygame.image.load(os.path.join("images","hati_white.png"))
w_payada = pygame.image.load(os.path.join("images","pyada_white.png"))

# BLACK GOTI
b_raja = pygame.image.load(os.path.join("images","raja_black.png"))
b_wazir = pygame.image.load(os.path.join("images","wazir_black.png"))
b_bishop = pygame.image.load(os.path.join("images","bb.png"))
b_ghoda = pygame.image.load(os.path.join("images","ghoda_black.png"))
b_hati = pygame.image.load(os.path.join("images","hati_black.png"))
b_payada = pygame.image.load(os.path.join("images","pyada_black.png"))

# LIST TO TRANSFORM IMAGE AT ONCE
b = [b_raja,b_bishop,b_ghoda,b_wazir,b_hati,b_payada]
w = [w_raja,w_bishop,w_ghoda,w_wazir,w_hati,w_payada]
B = []
W = []
for image in b:
    B.append(pygame.transform.scale(image, (90,90)))
for image in w:
    W.append(pygame.transform.scale(image,(90,90)))




class Piece:
    img = -1
    RECT = (25,25,760,760)
    startX,startY = RECT[0],RECT[1]
    endX,endY = RECT[2],RECT[3]
    
    def __init__(self,row,col,color):
        self.row = row
        self.col = col
        self.color = color
        self.selected = False
        self.move_list = []
    # def validMoves(self,board):
    #     pass
   
    def isSelected(self):
        return self.selected
    def updateValidMoves(self,board):
        self.move_list = self.validMoves(board)

    def draw(self,WINDOW):
        if self.color == "w":
            drawImage = W[self.img_pos]
        else:
            drawImage = B[self.img_pos]
        if self.selected:
            moves = self.move_list
            for move in moves:
                x = 45+round(self.startX + (move[0]*self.RECT[2]/8))
                y = 45+round(self.startY + (move[1]*self.RECT[3]/8))
                pygame.draw.circle(WINDOW, (255,0,0), (x,y), 10)

        x = round(self.startX + (self.col*self.RECT[2]/8))
        y = round(self.startY + (self.row*self.RECT[3]/8))
        if self.selected:
            pygame.draw.rect(WINDOW, (255,0,0), (x,y,90,90),2)
        WINDOW.blit(drawImage,(x,y))
    def changePos(self,pos):
        self.row = pos[0]
        self.col = pos[1]
    def __str__(self):
        return str(self.col) + " " + str(self.row)


class Bishop(Piece):
    img_pos = 1
    def validMoves(self, board):
        i,j = self.row,self.col
        moves = []

        # BLACK DIAGONAL 
        d_jl = j + 1
        d_jr = j -1
        for d_i in range(i+1,8):
            if d_jl < 8 :
                p = board[d_i][d_jl]
                if p == 0:
                    moves.append((d_jl,d_i))
                elif p.color != self.color:
                    moves.append((d_jl,d_i))
                else:
                    break
            else:
                break
            d_jl += 1

        for d_i in range(i+1,8):
            if d_jr > -1:
                p = board[d_i][d_jr]
                if p == 0:
                    moves.append((d_jr,d_i))
                elif p.color != self.color:
                    moves.append((d_jr,d_i))
                else:
                    break
            else:
                break    
            d_jr -= 1
        
        # WHITE DIAGONAL
        d_jl = j-1
        d_jr = j+1
        for d_i in range(i-1,-1,-1):
            if d_jl > -1:
                p = board[d_i][d_jl]
                if p == 0:
                    moves.append((d_jl,d_i))
                elif p.color != self.color:
                    moves.append((d_jl,d_i))
                else:
                    break
            else:
                break
            d_jl -= 1
        
        for d_i in range(i-1,-1,-1):
            if d_jr <= 7:
                p = board[d_i][d_jr]
                if p == 0:
                    moves.append((d_jr,d_i))
                elif p.color != self.color:
                    moves.append((d_jr,d_i))
                else:
                    break
            else:
                break
            d_jr += 1


        
        return moves



class Ghoda(Piece):
    """
        4 POSSIBLE MOVES TO HANDLE 
            1. DOWNL LEFT
            2. DOWN RIGHT
            3. SIDE LEFT
            4. SIDE RIGHT
    """
    img_pos = 2
    def validMoves(self,board):
        i,j = self.row,self.col
        moves = []
        # Down Left
        if i < 6 and j>0:
            p = board[i+2][j-1] 
            if p== 0:
                moves.append((j-1,i+2))
            elif p.color != self.color: 
                moves.append((j-1,i+2))
                
        # Down Right
        if i < 6 and j<7:
            p = board[i+2][j+1] 
            if p== 0 :
                moves.append((j+1,i+2))
            elif p.color != self.color:
                moves.append((j+1,i+2))


       # Side Left
        if i > 1 and j>0:
            p = board[i-2][j-1] 
            if p== 0:
                moves.append((j-1,i-2))
            elif p.color != self.color:
                moves.append((j-1,i-2))
        # Side Riht
        if i > 1  and j<7:
            p = board[i-2][j+1] 
            if p== 0:
                moves.append((j+1,i-2))
            elif p.color != self.color:
                moves.append((j+1,i-2))
        return moves



class Hati(Piece):
    """
        Straight Line in Board 
    """
    img_pos = 4
    def validMoves(self, board):
        i,j = self.row,self.col
        moves = []
        #UP 
        for x in range(i-1,-1,-1):
            p = board[x][j]
            if p == 0:
                moves.append((j,x))
            else:
                break

        # DOWN 
        for x in range(i+1,8,1):
            p = board[x][j]
            if p == 0:
                moves.append((j,x))
            else:
                break
        #LEFT
        for x in range(j-1,-1,-1):
            p = board[i][x]
            if p == 0:
                moves.append((x,i))
            else:
                break
        
        #RIGHT
        for x in range(j+1,8,1):
            p = board[i][x]
            if p == 0:
                moves.append((x,i))
            else:
                break
        return moves



class Payada(Piece):
    img_pos = 5
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.first = True
        self.wazir = False
    def validMoves(self,board):
        i,j = self.row,self.col
        moves = []
        """
        IF THE PAWN IS MOVING FIRST TIME IT CAN MOVE 1 OR 2 STEPS IN A GO 
        """
        if self.color == "B":
            if self.first:
                if i < 6:
                    p = board[i+2][j]
                    if p == 0:
                        moves.append((j,i+2))
                    elif p.color != self.color:
                        moves.append((j,i+2))
            if i < 7:
                p = board[i+1][j] 
                if p== 0:
                    moves.append((j,i+1))
                #DIAGONAL
                if j < 7:
                    p = board[i+1][j+1]
                    if p!=0:
                        if p.color != self.color:
                            moves.append((j+1,i+1))
                if j>0:
                    p = board[i+1][j-   1]
                    if p!=0:
                        if p.color != self.color:
                            moves.append((j-1,i+1))

        # WHITE 
        else:
            if self.first:
                if i > 1:
                    p = board[i-2][j]
                    if p == 0:
                        moves.append((j,i-2))
            if i > 0:
                p = board[i-1][j] 
                if p== 0:
                    moves.append((j,i-1))
             #DIAGONAL
            if j < 7:
                p = board[i+1][j+1]
                if p != 0:
                    if p.color != self.color:
                        moves.append((j+1,i+1))
            if j>0:
                p = board[i-1][j-1]
                if p!=0:
                    if p.color != self.color:
                        moves.append((j-1,i-1))
                
                          
        return moves




class Raja(Piece):
    """
    8 possible position direction one step  
    """
    img_pos = 0
    def validMoves(self, board):
        i,j = self.row,self.col
        moves = []
        # TOP
        if i>0:
        # TOP LEFT
            if j > 0:
                p = board[i-1][j-1]
                if p == 0:
                    moves.append((j-1,i-1))
                elif p.color != self.color:
                    moves.append((j-1,i-1))
        # TOP MIDDLE           
            p = board[i-1][j]
            if p == 0:
                moves.append((j,i-1))
            elif p.color != self.color:
                moves.append((j,i-1))
        # TOP RIFHT
            if j<7:
                p = board[i-1][j+1]
                if p == 0:
                    moves.append((j+1,i-1))
                elif p.color != self.color:
                    moves.append((j+1,i-1))
        #BOTTOM
        if i<7:
            # BL
            if j > 0:
                p = board[i+1][j-1]
                if p == 0:
                    moves.append((j-1,i+1))
                elif p.color != self.color:
                    moves.append((j-1,i+1))
            #BM
            p = board[i+1][j]
            if p == 0:
                moves.append((j,i+1 ))
            elif p.color != self.color:
                moves.append((j,i+1 ))
            #BR
            if j < 7:
                p = board[i+1][j+1]
                if p == 0:
                    moves.append((j+1,i+1))
                elif p.color != self.color:
                    moves.append((j+1,i+1))
        if j>0:
            p = board[i][j-1]
            if p == 0:
                moves.append((j-1,i))
            elif p.color != self.color:
                moves.append((j-1,i))

        if j<7:
            p = board[i][j+1]
            if p == 0: 
                moves.append((j+1,i))
            elif p.color != self.color:
                moves.append((j+1,i))

        return moves


# WAZIR / QUEEN
class Wazir(Piece):
    img_pos = 3

    def validMoves(self, board):
        i,j = self.row,self.col
        moves = []

        # BLACK DIAGONAL 
        d_jl = j + 1
        d_jr = j -1
        for d_i in range(i+1,8):
            if d_jl < 8 :
                p = board[d_i][d_jl]
                if p == 0:
                    moves.append((d_jl,d_i))
                elif p.color != self.color:
                    moves.append((d_jl,d_i))
            d_jl += 1
            if d_jr > -1:
                p = board[d_i][d_jr]
                if p == 0:
                    moves.append((d_jr,d_i))
                elif p.color != self.color:
                    moves.append((d_jr,d_i))
            d_jr -= 1    
        
        # WHITE DIAGONAL
        d_jl = j-1
        d_jr = j+1
        for d_i in range(i-1,-1,-1):
            if d_jl > -1:
                p = board[d_i][d_jl]
                if p == 0:
                    moves.append((d_jl,d_i))
                elif p.color != self.color:
                    moves.append((d_jl,d_i))
            d_jl -= 1
        
            if d_jr <= 7:
                p = board[d_i][d_jr]
                if p == 0:
                    moves.append((d_jr,d_i))
                elif p.color != self.color:
                    moves.append((d_jr,d_i))
            d_jr += 1

# COPY MOVES OF HATHI / ROOK
        #UP 
        for x in range(i-1,-1,-1):
            p = board[x][j]
            if p == 0:
                moves.append((j,x))
            else:
                break

        # DOWN 
        for x in range(i+1,8,1):
            p = board[x][j]
            if p == 0:
                moves.append((j,x))
            else:
                break
        #LEFT
        for x in range(j-1,-1,-1):
            p = board[i][x]
            if p == 0:
                moves.append((x,i))
            else:
                break
        
        #RIGHT
        for x in range(j+1,8,1):
            p = board[i][x]
            if p == 0:
                moves.append((x,i))
            else:
                break

        
        return moves
