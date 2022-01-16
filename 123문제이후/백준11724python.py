import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph = [[]for i in range(n + 1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0] * (n + 1)
def bfs(v):
    q = deque()
    q.append(v)
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1
result = 0
for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)
        result += 1
sys.stdout.write(str(result))
