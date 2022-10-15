with open("dane/szachy.txt") as f:
    file = [line.strip() for line in f]
    plansze = []
    for i in range(int((len(file)+1)/9)):
        plansze.append(file[i*9:i*9 +8])

def columncheck(col, plansza):
    for line in plansza:
        if line[col] != ".":
            return False
    return True

ans = [0, 0]
for plansza in plansze:
    count = 0
    for col in range(8):
        if columncheck(col, plansza):
            count += 1
    if count > 0:
        ans[0] += 1
    if count > ans[1]:
        ans[1] = count
print(ans)

def boardcount(plansza):
    pieces = {"K": 0, "k": 0, "H": 0, "h": 0, "W": 0, "w": 0, "G": 0, "g": 0, "S": 0, "s": 0, "P": 0, "p": 0}
    for line in plansza:
        for piece in line:
            if piece in pieces:
                pieces[piece] += 1
    return pieces
    
def isequal(pieces):
    count = 0
    for piece in pieces:
        count += pieces[piece]
        if pieces[piece] != pieces[piece.upper()]:
            return False, 100
    return True, count

ans = [0, 100]
for plansza in plansze:
    pieces = boardcount(plansza)
    sol = isequal(pieces)
    if sol[0]:
        ans[0] += 1
    if sol[1] < ans[1]:
        ans[1] = sol[1]
print(ans)

def findpiece(piece, board):
    for x, row in enumerate(board):
        for y in range(len(row)):
            if row[y] == piece:
                return x,y
    return 10, 10

def betweencheck(k, w, board):
    if k[0] == w[0]:
        for i in range(k[1] +1, w[1] -1):
            if board[k[0]][i] != '.':
                return False
    if k[1] == w[1]:
        for i in range(k[0] +1, w[0] -1):
            if board[i][k[1]] != '.':
                return False
        
    return True

ans = [0, 0]
for plansza in plansze:
    K = findpiece("K", plansza)
    w = findpiece("w", plansza)
    if K[0] == w[0] or K[1] == w[1]:
        if betweencheck(K, w, plansza):
            ans[0] += 1
    k = findpiece("k", plansza)
    W = findpiece("W", plansza)
    if k[0] == W[0] or k[1] == W[1]:
        if betweencheck(k, W, plansza):
            ans[1] += 1
print(ans)