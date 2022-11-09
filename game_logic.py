import pygame
import os
from piece import Bishop
from board import Board

pygame.init()

#WINDOW VARIABLES 
WINDOW_WIDTH = 810
WINDOW_HEIGHT = 810
WINDOW_TITLE = "CHESS GAME"

# LOADING IMAGES
chessBoard = pygame.image.load(os.path.join("images","ChessBoard.png"))
chessBoard = pygame.transform.scale(chessBoard, [WINDOW_WIDTH,WINDOW_HEIGHT])
RECT = (25,25,760,760)






def update_gameWindow():
    global WINDOW
    WINDOW.blit(chessBoard, (0,0))
    b = Bishop(1,1, "w")
    b.draw(WINDOW)
    # pygame.draw.rect(WINDOW, (255,0,0),(25,25,760,760) ,5)
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(10)
        update_gameWindow()    
        # Event control during game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass


# WINDWO VARIABLES 
WINDOW = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)
main()