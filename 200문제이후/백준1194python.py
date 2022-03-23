import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
board = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(n)]
dr = [[1, 0], [-1, 0], [0, 1], [0, -1]]
visited = [[[0] * 64 for _ in range(m)] for _ in range(n)]
def bfs():
    q = deque()
    one = [[i, j] for i in range(n) for j in range(m) if board[i][j] == '0']
    q.append((one[0][0], one[0][1], 0, 0))
    while q:
        x, y, d, a = q.popleft()
        for dx, dy in dr:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny][a] == 0:
                if board[nx][ny] == '1':
                    return d + 1
                elif board[nx][ny] == '.' or board[nx][ny] == '0':
                    visited[nx][ny][a] = 1
                    q.append((nx, ny, d + 1, a))
                elif board[nx][ny].islower():
                    na = a | (1 << ord(board[nx][ny]) - 97)
                    if visited[nx][ny][na] == 0:
                        visited[nx][ny][na] = 1
                        q.append((nx, ny, d + 1, na))
                elif board[nx][ny].isupper() and a & 1 << (ord(board[nx][ny]) - 65):
                    visited[nx][ny][a] = 1
                    q.append((nx, ny, d + 1, a))
    return -1
print(bfs())
