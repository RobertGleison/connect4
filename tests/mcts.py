# #Coloquei aqui só para base, logo modificamos

# # from connectFour import getActionsBot, getActionsPlayer, playerPlays
# from board import Board
# import random
# import math
# import time

# class TreeNode:
#     def __init__(self, state: Board, next_player:str, parent=None ):
#         self.state = state
#         self.parent = parent
#         self.children = []
#         self.visits = 0
#         self.value = 0.0
#         self.next_player = next_player

#     def expand(self):
#         if(self.next_player == "BOT"):
#             for child in getActionsBot(self.state):
#                 new_node = TreeNode(child, "PLAYER", self)
#                 self.children.append(new_node)
#         else:
#             for child in getActionsPlayer(self.state):
#                 new_node = TreeNode(child, "BOT", self)
#                 self.children.append(new_node)

#         return len(self.children)

#     def is_fully_expanded(self):
#         return len(self.children) == len(self.state.getColumnsDone())

# class Monte_carlo_tree_search:
#     def __init__(self, root_state):
#         self.root = TreeNode(root_state, "BOT")
#         self.num_nodes_gen = 0

#     def getNumNodesGen(self):
#         return self.num_nodes_gen

#     def run(self, iterations):
#         for i in range(iterations):
#             node = self.select_node()
#             if not node.is_fully_expanded():
#                 self.num_nodes_gen += node.expand()
#                 if(len(node.children) != 0):
#                     self.simulate(node.children[-1])
#             else:
#                 self.simulate(node)
        
#         return self.get_best_move()
    
#     def select_node(self):
#         node = self.root
#         while node.children:
#             best_child = None
#             best_value = float("-inf")
#             for child in node.children:
#                 if child.visits == 0:
#                     UCT_value = float("inf")
#                 else:
#                     UCT_value = child.value / child.visits + 2*math.sqrt((math.log(node.visits) / child.visits))
#                 if UCT_value > best_value:
#                     best_child = child
#                     best_value = UCT_value
#             node = best_child
#         return node

#     def simulate(self, node):
#         state = node.state
#         player = node.next_player
#         while not state.gameFinished():
#             if(player =="BOT"):
#                 state = random.choice(getActionsBot(state))
#                 player = "PLAYER"
#             else:
#                 state = random.choice(getActionsPlayer(state))
#                 player = "BOT"
#         reward = state.getPoints()
#         if(reward == 512):
#             self.backpropagate(node, 1)
#             return
#         elif(reward == -512):
#             self.backpropagate(node, -1)
#             return
#         self.backpropagate(node,0)

#     def backpropagate(self, node, reward):
#         while node is not None:
#             node.visits += 1
#             node.value += reward
#             node = node.parent

#     def get_best_move(self):
#         best_value = float("-inf")
#         best_moves = []
#         for child in self.root.children:
#             value = child.value / child.visits
#             if value > best_value:
#                 best_value = value
#                 best_moves = [child.state]
#             elif value == best_value:
#                 best_moves.append(child.state)
#         return random.choice(best_moves)

# def play_mcts(node: Board):
#     new_table = node
#     while new_table.gameTied() is not True:
#         start_time = time.time()
#         new_table = playerPlays(new_table)
#         end = new_table.gameOver() 
#         if end is not None:
#             print(new_table)
#             print(end + " WINS")
#             return
#         print(new_table)
#         mcts = Monte_carlo_tree_search(new_table)    
#         new_table = mcts.run(5000)
#         end = new_table.gameOver() 
#         if end is not None:
#             end_time_win = time.time()
#             print("----------- BOT -----------")
#             print("\nTEMPO DE RESPOSTA: ", end_time_win - start_time)
#             print("NUMERO DE NÓS CRIADOS: ",mcts.getNumNodesGen())
#             print(new_table)
#             print(end + " WINS")
#             return
#         end_time = time.time()
#         print("----------- BOT -----------")
#         print("\nTEMPO DE RESPOSTA: ", end_time - start_time)
#         print("NUMERO DE NÓS CRIADOS: ",mcts.getNumNodesGen())
#         print(new_table)

#     print("------------ EMPATE ------------")