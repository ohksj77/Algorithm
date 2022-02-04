import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
q = deque()
def initialize():
    ri, rj, bi, bj = 0, 0, 0, 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                ri, rj = i, j
            elif board[i][j] == 'B':
                bi, bj = i, j
    q.append((ri, rj, bi, bj, 1))
    visited[ri][rj][bi][bj] = True
def move(i, j, x, y):
    c = 0
    while board[i + x][j + y] != '#' and board[i][j] != 'O':
        i += x
        j += y
        c += 1
    return i, j, c
def bfs():
    initialize()
    while q:
        ri, rj, bi, bj, d = q.popleft()
        if d > 10:
            break
        for i in range(4):
            nrx, nry, rcnt = move(ri, rj, dx[i], dy[i])
            nbx, nby, bcnt = move(bi, bj, dx[i], dy[i])
            if board[nbx][nby] != 'O':
                if board[nrx][nry] == 'O':
                    print(d)
                    exit()
                if nrx == nbx and nry == nby:
                    if rcnt > bcnt:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    q.append((nrx, nry, nbx, nby, d + 1))
    print(-1)
bfs()
