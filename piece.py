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
    def move(self):
        pass
    def isSelected(self):
        return self.selected
    def draw(self,WINDOW):
        if self.color == "w":
            drawImage = W[self.img_pos]
        else:
            drawImage = B[self.img_pos]
        x = round(self.startX + (self.col*self.RECT[2]/8))
        y = round(self.startY + (self.row*self.RECT[2]/8))
        WINDOW.blit(drawImage,(x,y))
class Bishop(Piece):
    img_pos = 1
class Ghoda(Piece):
    img_pos = 2
class Hati(Piece):
    img_pos = 4
class Payada(Piece):
    img_pos = 5
class Raja(Piece):
    img_pos = 0
class Wazir(Piece):
    img_pos = 3
