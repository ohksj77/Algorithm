import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
def bfs():
    q = deque()
    q.append([0, 0, 1])
    visited[0][0][1] = 1
    while q:
        x, y, b = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][b]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 1 and b == 1:
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    q.append([nx, ny, 0])
                elif board[nx][ny] == 0 and visited[nx][ny][b] == 0:
                    visited[nx][ny][b] = visited[x][y][b] + 1
                    q.append([nx, ny, b])
    return -1
print(bfs())
