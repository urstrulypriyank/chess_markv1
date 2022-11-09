import pygame
import os

# LOADING IMAGES
chessBoard = pygame.image.load(os.path.join("images","ChessBoard.jpg"))

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