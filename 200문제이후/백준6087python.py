import sys
from collections import deque
w, h = map(int, sys.stdin.readline().split())
board = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(h)]
visited = [[1e9] * w for _ in range(h)]
dr = [[-1, 0], [1, 0], [0, 1], [0, -1]]
cArray = []
for i in range(h):
    for j in range(w):
        if board[i][j] == 'C':
            cArray.append((i, j))
(fx, fy), (sx, sy) = cArray
def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for dx, dy in dr:
            nx, ny = x + dx, y + dy
            while True:
                if not (0 <= nx < h and 0 <= ny < w):
                    break
                if board[nx][ny] == "*":
                    break
                if visited[nx][ny] < visited[x][y] + 1:
                    break
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                nx, ny = nx + dx, ny + dy
bfs(fx, fy)
sys.stdout.write(str(visited[sx][sy] - 1))
