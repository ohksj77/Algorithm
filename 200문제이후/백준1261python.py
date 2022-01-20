import sys
from collections import deque
m, n = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
distance = [[-1] * m for _ in range(n)]
distance[0][0] = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    q = deque()
    q.append([0, 0])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if distance[nx][ny] == -1:
                    if arr[nx][ny] == 0:
                        distance[nx][ny] = distance[x][y]
                        q.appendleft([nx, ny])
                    else:
                        distance[nx][ny] = distance[x][y] + 1
                        q.append([nx, ny])
    return distance[n - 1][m - 1]
print(bfs())
