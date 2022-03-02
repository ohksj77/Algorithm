import sys
from collections import deque
board = [list(sys.stdin.readline().rstrip()) for _ in range(8)]
walls = [(i, j) for i in range(8) for j in range(8) if board[i][j] == '#']
dr = [[0, 0], [1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
def bfs():
    q = deque()
    q.append((7, 0, 0))
    while q:
        x, y, time = q.popleft()
        for dx, dy in dr:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < 8 and 0 <= ny < 8 and board[nx - time][ny] != '#' and board[nx - time - 1][ny] != '#':
                if nx - time < 0:
                    return 1
                q.append((nx, ny, time + 1))
    return 0
print(bfs())
