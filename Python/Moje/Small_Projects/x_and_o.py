import random
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def win_check():
    for num in range(0, 3):
        if board[num][0] == board[num][1] and board[num][1] == board[num][2] and board[num][0] != 0 or \
                board[0][num] == board[1][num] and board[1][num] == board[2][num] and board[0][num] != 0:
            return True
    if board[1][1] != 0:
        if board[0][0] == board[1][1] and board[1][1] == board[2][2] or \
                board[2][0] == board[1][1] and board[1][1] == board[0][2]:
            return True

def legal_move(x, y):
    return True if board[x][y] == 0 else False

def stalemate():
    for a in range(3):
        for b in range(3):
            if board[a][b] == 0:
                return False
    return True

def player_move():
    turn = True
    while turn:
        move = list(map(int, input('Your move, input coordinates (x y)').split()))
        if legal_move(move[0] -1, move[1] -1):
            return move
        print('Invalid move')

def computer_move(level):
    record = 0
    cmove = []
    for a in range(3):
        for b in range(3):
            if legal_move(a, b):
                board[a][b] = 2
                if win_check():
                    board[a][b] = 0
                    return [a, b]
                board[a][b] = 1
                if win_check():
                    board[a][b] = 0
                    return[a, b]
                board[a][b] = 2
                num = best_move(0, level -1)
                if num > record:
                    record = num
                    cmove = [a, b]
                board[a][b] = 0
    if record > 0:
        return cmove
    else:
        move = True
        while move:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            if legal_move(x, y):
                return [x, y]

def best_move(count, level):
    for a in range(3):
        for b in range(3):
            if legal_move(a, b):
                if level % 2 == 0:
                    board[a][b] = 2
                    if win_check():
                        board[a][b] = 0
                        return count + 1
                else:
                    board[a][b] = 1
                    if win_check():
                        board[a][b] = 0
                        return count - 1
                if stalemate():
                    board[a][b] = 0
                    return 0
                if level > 0:
                    count = best_move(count, level -1)
                board[a][b] = 0
    return count

def main():
    game = True
    level = 9
    while game:
        level -= 1
        move = computer_move(level)
        board[move[0]][move[1]] = 2
        print(*board, sep='\n')
        if win_check():
            return 2
        if stalemate():
            return 0
        move = player_move()
        board[move[0] -1][move[1] -1] = 1
        if win_check():
            return 1
    
win = main()

if win == 2:
    print('You lose !')
elif win == 1:
    print('You win !')
else:
    print("It's a draw !")