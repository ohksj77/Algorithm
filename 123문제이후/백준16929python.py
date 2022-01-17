import sys
n, m = map(int, sys.stdin.readline().split())
arr = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
flag = False
visited = [[False] * m for _ in range(n)]
def dfs(y, x, y1, x1, dot):
    if visited[y][x]:
        return True
    visited[y][x] = True
    for i in range(4):
        a = y + dy[i]
        b = x + dx[i]
        if a != y1 or b != x1:
            if 0 <= a < n and 0 <= b < m and arr[a][b] == dot:
                if dfs(a, b, y, x, dot):
                    return True
    return False
for i in range(n):
    for j in range(m):
        if visited[i][j]:
            continue
        if dfs(i, j, 0, 0, arr[i][j]):
            flag = True
            break
print("Yes" if flag else "No")
