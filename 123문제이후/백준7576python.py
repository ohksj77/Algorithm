from collections import deque
import sys
m, n = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            queue.append([i, j])
while queue:
    a, b = queue.popleft()
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < n and 0 <= y < m and arr[x][y] == 0:
            queue.append([x, y])
            arr[x][y] = arr[a][b] + 1
result = 0
for i in arr:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    result = max(result, max(i))
print(result - 1)
