# from game import constants as c
# from game import game_logic as game
# import numpy as np
# import random

# def mcts(board, simulations=100) -> int:
#     root = Node(board)
#     for _ in range(simulations):
#         node = select_node(root)
#         board_copy = node.board.copy()
#         selected_move = simulate_playout(board_copy)
#         backpropagate(node, selected_move)
#     return get_best_move(root)


# class Node:
#     def __init__(self, board):
#         self.board = board
#         self.parent = None
#         self.children = []
#         self.visits = 0
#         self.wins = 0

#     def is_leaf(self):
#         return not self.children

#     def can_expand(self):
#         return any(game.is_valid(self.board, col) for col in range(c.COLUMNS))


# def select_node(node):
#     while not node.is_leaf():
#         best_score = float('-inf')
#         best_child = None
#         for child in node.children:
#             exploitation = child.wins / child.visits
#             exploration = np.sqrt(np.log(node.visits) / child.visits)
#             score = exploitation + c.EXPLORATION_PARAM * exploration
#             if score > best_score:
#                 best_score = score
#                 best_child = child
#         node = best_child
#     return node


# def simulate_playout(board):
#     while True:
#         player = random.choice([c.AI_PIECE, c.HUMAN_PIECE])
#         valid_moves = [col for col in range(c.COLUMNS) if game.is_valid(board, col)]
#         if not valid_moves:
#             break  # Tie game
#         selected_move = random.choice(valid_moves)
#         game.make_move(board, None, board, player, selected_move)
#         if game.winning_move(board, player):
#             return player
#     return c.EMPTY  # Tie game


# def backpropagate(node, winner):
#   """
#   Propagates the game outcome (win or tie) back up the tree, updating node statistics.
#   """
#   while node:
#     node.visits += 1
#     node.wins += winner == c.AI_PIECE
#     winner = node.parent.board[c.ROWS-1][node.parent.children.index(node)]  # Update winner for parent based on child's outcome
#     node = node.parent


# def get_best_move(node):
#     most_visited_child = None
#     for child in node.children:
#         if not most_visited_child or child.visits > most_visited_child.visits:
#            most_visited_child = child
#     return most_visited_child.board[c.ROWS-1].index(c.EMPTY)  # Identify the column from child node's board

# # Usage example (assuming game.py and heuristics.py are available)
# board = np.zeros((c.ROWS, c.COLUMNS))
# best_move = mcts(board)
# print(f"MCTS recommends playing column {best_move}")
