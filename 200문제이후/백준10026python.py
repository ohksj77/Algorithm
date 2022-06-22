import sys
from collections import deque
n = int(sys.stdin.readline())
colors = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
dr = ((0, 1), (-1, 0), (1, 0), (0, -1))
normalNum = {'R': 0, 'G': 1, 'B': 2}
blindNum = {'R': 0, 'G': 0, 'B': 2}
def bfs(dic):
    visited = [[False for _ in range(n)] for _ in range(n)]
    q = deque()
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                q.append((i, j, colors[i][j]))
                count += 1
                while q:
                    x, y, color = q.popleft()
                    visited[x][y] = True
                    for dx, dy in dr:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n:
                            if dic[colors[nx][ny]] == dic[color] and not visited[nx][ny]:
                                q.append((nx, ny, colors[nx][ny]))
                                visited[nx][ny] = True
    return count
sys.stdout.write(str(bfs(normalNum)) + " " + str(bfs(blindNum)))
