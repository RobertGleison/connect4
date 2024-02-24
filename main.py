import connect4
from board import Board

def main():
    board = Board()
    connect4.start_game(board)
    
if __name__ == "__main__":
    main()

