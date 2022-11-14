import pygame
import os
from piece import Bishop
from board import Board
import math

pygame.init()

#WINDOW VARIABLES 
WINDOW_WIDTH = 810
WINDOW_HEIGHT = 810
WINDOW_TITLE = "CHESS GAME"
RED = (255,0,0)

# LOADING IMAGES
chessBoard = pygame.image.load(os.path.join("images","ChessBoard.png"))
chessBoard = pygame.transform.scale(chessBoard, [WINDOW_WIDTH,WINDOW_HEIGHT])
RECT = (28,28,753,758)
turn = "w"





def update_gameWindow():
    global WINDOW,b
    WINDOW.blit(chessBoard, (0,0))
    b.draw(WINDOW)
    pygame.draw.rect(WINDOW, (255,0,0),(28,28,753,758) ,2)
    pygame.display.update()


def click(position):
    x = position[0]
    y = position[1]
    if RECT[0] < x <  RECT[0]+RECT[2]:
        if RECT[1] < y < RECT[1]+RECT[3]:
            divX = x -  RECT[0] 
            divY = y - RECT[0]
            i = int((divX /(RECT[2]/8)))
            j = int((divY/(RECT[3]/8)))
            # print(i,j)
    return i,j

def endScreen(WINDOW,msg):
    pygame.font.init()
    font = pygame.font.SysFont("comicsans", 80)
    txt = font.render(msg, 1,RED)
    WINDOW.blit(txt,(WINDOW_WIDTH/2 - txt.get_width()/2,250))
    pygame.display.update()


    pygame.time.set_timer(pygame.USEREVENT+1,5000)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                run = False
            elif event.type == pygame.KEYDOWN:
                run = False
            elif event.type == pygame.USEREVENT+1:
                run = False

    

def main():
    global b
    run = True
    turn = "w"
    b = Board(8, 8)
    clock = pygame.time.Clock()
    while run:
        clock.tick(10)
        update_gameWindow()    
        # Event control during game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                b.update_moves()
                i,j = click(position)
                change = b.select(i,j,turn) 
                b.update_moves()
                # update_gameWindow()   
                if change:
                    if turn == "w": turn = "B"
                    else: turn = "w"
    if b.checkMate("w"):
        endScreen(WINDOW, "white Won!")
    if b.checkMate("B"):
        endScreen(WINDOW, "Black Won!")        
                
# WINDWO VARIABLES 
WINDOW = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)
main()