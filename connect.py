from colored import fg
import sys

class Board:
    def __init__(self):
        self.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
        
        self.player_turn = 'R'
        
    def show_board(self):
        boardGUI = ''
        for x in self.board:
            boardGUI += '\n |'
            for y in x:
                color = ''
                if y == 'Y':
                    boardGUI += '\033[4m'+ fg('yellow') + 'O' + '\033[0m'
                    boardGUI += '|'
                elif y == 'R':
                    boardGUI += '\033[4m'+ fg('red') + 'O' + '\033[0m'
                    boardGUI += '|'
                else:
                    boardGUI += '\033[4m'+ ' ' + '\033[0m' 
                    boardGUI += '|'
        
        print(boardGUI)

    def reset(self):
        for x in range(6):
            for y in range(7):
                self.board[x][y] = ' '

    def ask_col(self):
        while True:
            try:
                col = int(input('Which column: '))
                return col
            except KeyboardInterrupt:
                sys.exit()
            except:
                print('Not a number bitch')



    def add_piece(self, col):
        for i in range(6):
            if self.board[5-i][col-1] == ' ':
                self.board[5-i][col-1] = self.player_turn
                break

    def check_vertical(self, col):
        c = 0
        for i in range(6):
            if self.board[5-i][col-1] == self.player_turn: 
                c += 1
            elif c == 4:
                return True
            else: 
                c = 0
        return False
    
    def check_horizontal(self, row):
        c = 0
        for x in self.board[row-1]:
            if x == self.player_turn:
                c += 1
            elif c == 4:
                return True
            else:
                c = 0
        return False
    
    def check_diagonal(self):
        for i in range(len(self.board) - 3):
            for j in range(len(self.board[0]) - 3):
                if self.board[i][j] != ' ' and self.board[i][j] == self.board[i+1][j+1] == self.board[i+2][j+2] == self.board[i+3][j+3]:
                    return True

        for i in range(len(self.board) - 3):
            for j in range(3, len(self.board[0])):
                if self.board[i][j] != ' ' and self.board[i][j] == self.board[i+1][j-1] == self.board[i+2][j-2] == self.board[i+3][j-3]:
                    return True

        return False

    def check_win(self):
        for x in range(7):
            if self.check_vertical(x): return True

        for x in range(6):
            if self.check_horizontal(x): return True

        if self.check_diagonal(): return True

        return False

    def mainloop(self):
        self.reset()
        self.show_board()
        while not self.check_win():
            self.add_piece(self.ask_col())
            self.show_board()
            if self.check_win(): 
                print(self.player_turn + " has won !")
                break
            if self.player_turn == 'R': self.player_turn = 'Y'
            else: self.player_turn = 'R'

            
        
        

board = Board()
board.mainloop()

