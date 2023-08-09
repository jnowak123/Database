def is_solved(board):
    for row in range(3):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
            return board[row][0]
    for col in range(3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
            return board[0][col]
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) or (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        return board[1][1]
    for row in board:
        if "0" in row:
            return -1
    return 0
