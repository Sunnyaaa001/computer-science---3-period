"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    for row in board:
        for cell in row:
            if cell == "X":
                x_count += 1
            elif cell == "O":
                o_count += 1
    if x_count == o_count:
        return "X"
    else:
        return "O"



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_list = set()
    for i,row in enumerate(board):
        for j,cell in enumerate(row):
            if cell == EMPTY:
                possible_list.add((i,j))
    return possible_list            


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j = action
    play = player(board=board)
    new_board = copy.deepcopy(board)
    new_board[i][j] = play
    return new_board
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] is not EMPTY and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] is not EMPTY and board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    if board[0][0] is not EMPTY and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] is not EMPTY and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    outcome = winner(board)
    if outcome is None:
        for row in board:
            for cell in row:
                if cell == EMPTY:
                    return False
        return True
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    outcome = winner(board)
    if outcome == X:
        return 1
    elif outcome == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    current_player = player(board)

    if current_player == X:
        best_val = -math.inf
        best_move = None
        for action in actions(board):
            current_value = min_value(result(board,action),-math.inf,math.inf)
            if current_value > best_val:
                best_val = current_value
                best_move = action
        return best_move
    
    if current_player == O:
        best_val = math.inf
        best_move = None
        for action in actions(board):
            current_value = max_value(result(board,action),-math.inf,math.inf)
            if current_value < best_val:
                best_val = current_value
                best_move = action
        return best_move


def max_value(board,alpha,beta):
    if terminal(board):
        return utility(board)
    value = -math.inf
    for action in actions(board):
        value = max(value,min_value(result(board=board,action=action),alpha,beta))
        alpha = max(alpha,value) #-1 -1
        if alpha >= beta:
            break
    return value    


def min_value(board,alpha,beta):
    if terminal(board):
        return utility(board)
    value = math.inf
    for action in actions(board):
        value = min(value,max_value(result(board=board,action=action),alpha,beta))
        beta = min(value,beta) #1
        if beta <= alpha:
            break
    return value    