from interface import Interface
from board import Board


def main() -> None:
    board = Board()
    interface = Interface()
    interface.start_game(board)
    
if __name__ == "__main__":
    main()