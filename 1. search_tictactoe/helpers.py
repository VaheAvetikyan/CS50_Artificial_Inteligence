def valid_board(board):
    if len(board) != 3:
        return False
    for i in board:
        if len(i) != 3:
            return False
        for j in i:
            if not j in ('X', 'O', None):
                return False
    return True
