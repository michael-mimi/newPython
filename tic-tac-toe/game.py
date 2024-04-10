from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
                    print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in number_board:
              print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i,spot in enumerate(self.board) if spot==' ']
        # moves = []
        # for (i,spot) in enumerate(self.board):
        #     if spot == ' ':
        #             moves.append(i)
        # return moves
    
    def has_empty_squares(self):
         return ' ' in self.board
        
    def num_empty_squares(self):
         return self.board.count(' ')
    
    def make_move(self,square,letter):
         if self.board[square] == ' ':
              self.board[square] = letter
              if self.check_winner(square, letter):
                   self.current_winner = letter
              return True
         return False
    
    def check_winner(self,square,letter):
         #check row
         row_ind = square // 3
         row = self.board[row_ind*3 : (row_ind+1)*3]
         if all([spot == letter for spot in row]):
              return True
         #check column
         col_ind = square % 3
         column = [self.board[col_ind+i*3] for i in range(3)]
         if all([spot == letter for spot in column]):
              return True
         
         #check对角线,只有在选择(0,2,4,6,8)格子时才需要check
         if square % 2 == 0:
              diagnal1 = [self.board[i] for i in [0,4,8]]#左斜线
              diagnal2 = [self.board[i] for i in [2,4,6]]#右斜线
              if all([spot == letter for spot in diagnal1]):
                   return True
              if all([spot == letter for spot in diagnal2]):
                   return True
         #after all the checks
         return False


def play(game, x_player, o_player, print_game=True):
    # return the winner of the game or None for a tie
    if print_game:
        game.print_board_nums()
    
    letter = 'X'
    while game.has_empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
             if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('') #just empty line
            
             if game.current_winner:
                  if print_game:
                       print(letter + ' wins!')
                  return letter

        #after we made our move, we need to alternate letters
        letter = 'O' if letter == 'X' else 'X'
        # if letter == 'X':
        #      letter = 'O'
        # else:
        #      letter = 'X'
    
    if print_game:
         print('It\'s a tie!')



if __name__ == '__main__':
     x_player = HumanPlayer('X')
     o_player = RandomComputerPlayer('O')
     game = TicTacToe()
     play(game,x_player,o_player)