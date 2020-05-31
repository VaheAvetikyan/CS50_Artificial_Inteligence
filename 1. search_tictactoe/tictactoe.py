"""
Tic Tac Toe Player
"""

import math
import copy 

from helpers import valid_board

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
    if not valid_board(board):
        raise ValueError

    x = o = 0

    for i in board:
        for j in i:
            if j == X:
                x += 1
            elif j == O:
                o += 1

    player = X if x <= o else O

    return player


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    rows = len(board)
    columns = len(board[0])

    for i in range(rows):
        for j in range(columns):
            if board[i][j] == EMPTY:
                actions.add((i,j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if not action in actions(board):
        raise ValueError

    board_ = copy.deepcopy(board)
    board_[action[0]][action[1]] = player(board)

    return board_


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    h = len(board)
    for i in range(h):
        if board[i][0] != EMPTY and board[i][0] == board[i][1] and board[i][0] == board[i][2]:
            return board[i][0]
        elif board[0][i] != EMPTY and board[0][i] == board[1][i] and board[0][i] == board[2][i]:
            return board[0][i]
    if board[1][1] != EMPTY and (board[1][1] == board[0][0] and board[1][1] == board[2][2]) or (board[1][1] == board[0][2] and board[1][1] == board[2][0]):
        return board[1][1]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return len(actions(board)) == 0 or winner(board) != None


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if not terminal(board):
        return

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    plr = player(board)
    move = None

    if plr == X:
        res = -math.inf
        for action in actions(board):
            val = min_value(result(board, action))

            if val > res:
                res = val
                move = action

        return move

    elif plr == O:
        res = math.inf
        for action in actions(board):
            val = max_value(result(board, action))

            if val < res:
                res = val
                move = action

        return move


def max_value(board):
    if terminal(board):
        return utility(board)

    val = -math.inf

    for action in actions(board):
        val = max(val, min_value(result(board, action)))
        if val == 1:
            return val

    return val


def min_value(board):
    if terminal(board):
        return utility(board)

    val = math.inf
    
    for action in actions(board):
        val = min(val, max_value(result(board, action)))
        if val == -1:
            return val

    return val
