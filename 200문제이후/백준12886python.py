import sys
from collections import deque
a, b, c = map(int, sys.stdin.readline().split())
visited = [[False] * 1501 for _ in range(1501)]
total = a + b + c
def bfs(i, j, k):
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    while q:
        x, y = q.popleft()
        z = total - x - y
        if x == y == z:
            return 1
        for nx, ny in ((x, y), (x, z), (y, z)):
            if nx < ny:
                ny -= nx
                nx += nx
            elif nx > ny:
                nx -= ny
                ny += ny
            else:
                continue
            nz = total - nx - ny
            maxN = max(nx, ny, nz)
            minN = min(nx, ny, nz)
            if not visited[maxN][minN]:
                q.append((maxN, minN))
                visited[maxN][minN] = True
    return 0
if total % 3 != 0:
    print(0)
else:
    print(bfs(a, b, c))
