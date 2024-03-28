from game_rules.board import Board
from play_game.interface import Interface

def main() -> None:
    board = Board()
    interface = Interface()
    interface.start_game(board)
    
if __name__ == "__main__":
    main()