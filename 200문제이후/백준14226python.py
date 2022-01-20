import sys
from collections import deque
s = int(sys.stdin.readline())
arr = [[-1] * (s + 1) for _ in range(s + 1)]
def bfs():
    queue = deque()
    queue.append([1, 0])
    arr[1][0] = 0
    while queue:
        x, y = queue.popleft()
        if arr[x][x] == -1:
            arr[x][x] = arr[x][y] + 1
            queue.append([x, x])
        if x + y <= s and arr[x + y][y] == -1:
            arr[x + y][y] = arr[x][y] + 1
            queue.append([x + y, y])
        if x - 1 >= 0 and arr[x - 1][y] == -1:
            arr[x - 1][y] = arr[x][y] + 1
            queue.append([x - 1, y])
bfs()
result = arr[s][1]
for i in range(1, s):
    if arr[s][i] != -1:
        result = min(result, arr[s][i])
sys.stdout.write(str(result))
