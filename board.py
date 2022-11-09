class Board:
    def __init__(self,row,col):
        self.row = row
        self.col = col

        self.board = [[[] for _ in range(cols)] for _ in range(rows)]