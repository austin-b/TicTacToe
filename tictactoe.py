import os

class TicTacToe():

    def __init__(self, board_x, board_y):
        self.board = [ ["" for j in range(board_x)] for i in range(board_y)]

    def print_board(self):
        print("Board state:")
        for i in range(len(self.board)):
            print("\t", end="")
            for j in range(len(self.board[i])):
                if self.board[i][j] == "":
                    print(f"[ ]", end="")
                else:
                    print(f"[{self.board[i][j]}]", end="")
            print()

    def place_move(self, character, pos_x, pos_y):
        if character == "X" or character == "O":
            if self.board[pos_x][pos_y] == "":
                self.board[pos_x][pos_y] = character
        else:
            raise ValueError("character must be \"X\" or \"O\"")
    
    def check_win(self):
        win = False
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == "X" or self.board[i][j] == "O":
                    current = self.board[i][j]
                    try: # check vertical condition
                        if self.board[i+1][j] == current and self.board[i+2][j] == current:
                            print(f"\twin at {i}, {j}")
                            print(f"\tnext two: {i+1},{j} and {i+2},{j}")
                            win = True
                    except IndexError as e:
                        pass
                    try: # check horizontal condition
                        if self.board[i][j+1] == current and self.board[i][j+2] == current:
                            print(f"\twin at {i}, {j}")
                            print(f"\tnext two: {i},{j+1} and {i},{j+2}")
                            win = True
                    except IndexError as e:
                        pass
                    try: # check negative diagonal condition 
                        if self.board[i+1][j+1] == current and self.board[i+2][j+2] == current:
                            print(f"\twin at {i}, {j}")
                            print(f"\tnext two: {i+1},{j+1} and {i+2},{j+2}")
                            win = True
                    except IndexError as e:
                        pass
                    try: # check positive diagonal condition
                        if i == 2 and j == 0:
                            if self.board[i-1][j+1] == current and self.board[i-2][j+2] == current:
                                print(f"\twin at {i}, {j}")
                                print(f"\tnext two: {i-1},{j-1} and {i-2},{j-2}")
                                win = True
                    except IndexError as e:
                        pass
        return win
    
def process_turn(character):
    print(f"Player {character}:")
    move = input("Where would you like to move? Input: ").split(",")
    x, y = int(move[0].strip()), int(move[1].strip())
    try: 
        board.place_move(character, x, y)
    except:
        print(f"Player {character} move failed.")


if __name__ == "__main__":
    os.system("cls")

    print("What would you like the board size to be? Input: x, y")

    size = input().split(",")

    x, y = int(size[0].strip()), int(size[1].strip())

    board = TicTacToe(x, y)

    while True: # process turns until win
        os.system("cls")

        board.print_board()

        process_turn("X")

        if board.check_win():
            print("Player X won!")
            board.print_board()
            break

        os.system("cls")

        board.print_board()

        process_turn("O")

        if board.check_win():
            print("Player O won!")
            board.print_board()
            break