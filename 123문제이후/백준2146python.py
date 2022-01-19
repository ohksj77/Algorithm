from collections import deque
import sys
n = int(sys.stdin.readline())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
check = [[False] * n for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
ans = 1000
def bfs1(x, y):
    q1 = deque()
    q1.append((x, y))
    check[x][y] = True
    d[x][y] = 0
    while q1:
        x, y = q1.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] == 1 and not check[nx][ny]:
                    check[nx][ny] = True
                    q1.append((nx, ny))
                    q2.append((nx, ny))
                    d[nx][ny] = 0
def bfs2(q):
    q = deque(q)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] == 0 and d[nx][ny] == -1:
                    d[nx][ny] = d[x][y] + 1
                    q.append((nx, ny))
                elif a[nx][ny] == 1 and d[nx][ny] == -1:
                    return d[x][y]
    return 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and not check[i][j]:
            d = [[-1] * n for _ in range(n)]
            q2 = [(i, j)]
            bfs1(i, j)
            temp = bfs2(q2)
            if ans > temp:
                ans = temp
print(ans)
