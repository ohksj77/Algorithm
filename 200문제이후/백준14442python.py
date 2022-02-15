import sys
from collections import deque
n, m, k = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [[[0] * m for _ in range(n)] for _ in range(k + 1)]
visited[0][0][0] = 1
dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]
def bfs():
    q = deque()
    q.append((0, 0, 0, 1))
    while q:
        x, y, cnt, d = q.popleft()
        if x == n - 1 and y == m - 1:
            return d
        for dx, dy in dr:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 1 and cnt < k and not visited[cnt + 1][nx][ny]:
                    visited[cnt + 1][nx][ny] = 1
                    q.append((nx, ny, cnt + 1, d + 1))
                elif board[nx][ny] == 0 and not visited[cnt][nx][ny]:
                    visited[cnt][nx][ny] = 1
                    q.append((nx, ny, cnt, d + 1))
    return -1
print(bfs())
