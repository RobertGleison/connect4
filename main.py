import connect4
from board import Board
from options_board import OptionsBoard

def main() -> None:
    board = Board()
    options_board = OptionsBoard()
    connect4.start_game(board, options_board)
    
if __name__ == "__main__":
    main()

