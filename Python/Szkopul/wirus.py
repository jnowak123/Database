from collections import deque

class Wirus:

    def __init__(self):
        self.n, self.m, self.t = list(map(int, input().split()))
        self.room = []
        for dummy_a in range(self.n):
            self.room.append(input().split())
        print(self.infection())
        
    def infect(self, x, y, n):
        if x > -1 and x < self.n and y > -1 and y < self.m and self.room[x][y] == 'o':
            self.room[x][y] = 'x'
            self.q.append([x, y, n+1])

    def infection(self):
        self.q = deque([])
        for row in range(self.n):
            for col in range(self.m):
                if self.room[row][col] == 'x':
                    self.q.append([row, col, 0])
        while len(self.q) != 0 and self.q[0][2] < self.t:
            p = self.q.popleft()
            self.infect(p[0]+1, p[1], p[2])
            self.infect(p[0]-1, p[1], p[2])
            self.infect(p[0], p[1]+1, p[2])
            self.infect(p[0], p[1]-1, p[2])
        return sum(n.count('x') for n in self.room)

Wirus()
  