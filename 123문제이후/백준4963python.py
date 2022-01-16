from collections import deque
import sys
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]
def bfs(a, b):
    s[a][b] = 0
    queue = deque()
    queue.append((a, b))
    while queue:
        x, y = queue[0][0], queue[0][1]
        queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and s[nx][ny] == 1:
                s[nx][ny] = 0
                queue.append([nx, ny])
while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    s = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)
