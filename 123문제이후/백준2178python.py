import sys
n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
queue = [[0, 0]]
while queue:
    a, b = queue[0][0], queue[0][1]
    del queue[0]
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < n and 0 <= y < m and arr[x][y] == 1:
            queue.append([x, y])
            arr[x][y] = arr[a][b] + 1
print(arr[n - 1][m - 1])
