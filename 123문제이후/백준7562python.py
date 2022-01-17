import sys
from collections import deque
t = int(sys.stdin.readline())
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]
def bfs(x1, y1, x2, y2):
    queue = deque()
    queue.append([x1, y1])
    arr[x1][y1] = 1
    while queue:
        a, b = queue.popleft()
        if a == x2 and b == y2:
            print(arr[x2][y2] - 1)
            return
        for i in range(8):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < n and arr[x][y] == 0:
                queue.append([x, y])
                arr[x][y] = arr[a][b] + 1
for _ in range(t):
    n = int(sys.stdin.readline())
    x1, y1 = map(int, sys.stdin.readline().split())
    x2, y2 = map(int, sys.stdin.readline().split())
    arr = [[0] * n for _ in range(n)]
    bfs(x1, y1, x2, y2)
