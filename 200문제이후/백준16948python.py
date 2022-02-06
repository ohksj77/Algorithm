import sys
from collections import deque
n = int(sys.stdin.readline())
r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]
visited = [[-1] * n for _ in range(n)]
def bfs():
    q = deque()
    q.append((r1, c1))
    visited[r1][c1] = 0
    while q:
        r, c = q.popleft()
        for i in range(6):
            nr = r + dx[i]
            nc = c + dy[i]
            if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == -1:
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
                if nr == r2 and nc == c2:
                    return visited[r2][c2]
    return -1
print(bfs())
