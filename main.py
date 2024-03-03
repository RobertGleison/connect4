from interface import Interface
from board import Board


def main() -> None:
    board = Board()
    interface = Interface()
    interface.start_game(board)
    
if __name__ == "__main__":
    main()

# 2024-03-03 12:58:25,229 - INFO - Calculate Score
# 2024-03-03 12:58:25,229 - INFO - 1 ocorrencia ai: 1
# 2024-03-03 12:58:25,229 - INFO - 2 ocorrencia ai: 60
# 2024-03-03 12:58:25,229 - INFO - 3 ocorrencia ai: 150
# 2024-03-03 12:58:25,229 - INFO - 3 ocorrencia ai: 150
# 2024-03-03 12:58:25,229 - INFO - 1 ocorrencia oponente: 6
# 2024-03-03 12:58:25,230 - INFO - 2 ocorrencia oponente: 30
# 2024-03-03 12:58:25,230 - INFO - 3 ocorrencia oponente: 50
# 2024-03-03 12:58:25,230 - INFO - 3 ocorrencia oponente: 50
# 2024-03-03 12:58:25,230 - INFO - Total: 125

# [[0. 0. 0. 1. 0. 0. 0.]
#  [0. 0. 0. 2. 0. 0. 0.]
#  [0. 0. 0. 2. 0. 0. 0.]
#  [0. 0. 0. 1. 0. 0. 0.]
#  [0. 0. 0. 2. 0. 0. 0.]
#  [0. 0. 0. 1. 1. 0. 0.]] 