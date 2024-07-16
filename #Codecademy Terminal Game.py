#Codecademy Terminal Game

class Player():
    def Player():
        pass

#board array
class Board():
    def __init__(self, rows = 6, cols = 7):
        self.rows = rows
        self.cols = cols
        self.board = [[" " for i in range(6)] for j in range(7)] #" " makes this a string list?    
    def __repr__(self):
        return self
    def printBoard(self):
        count = 0
        for r in range(6): #iterate thru rows to give us a basic connect 4 board
            print('this is row ' + str(count) + str(self.board[r]))
            count += 1


#Add falling pieces
def add_piece(col, row = 0, piece = "x"):
    if (board[0][col] != " "):
        return "This row is full."
    if (col < 0 or col > 6):
        return "out of bounds"
    if (piece != 'x' or piece != 'o'):
        return "invalid piece"
    else:
        while board[row][col] == ' ':
            if board[5][col] == ' ':
                board[row][col].insert(piece)
                break
            if board[row][col] != ' ':
                board[row-1][col].insert(piece)
                break
            row += 1
    printBoard()
    return "successful piece drop"

playboard1 = Board()

playboard1.printBoard()
