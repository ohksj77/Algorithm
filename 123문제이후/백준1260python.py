from collections import deque
import sys
n, m, v = map(int, sys.stdin.readline().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited1 = [0] * (n + 1)
visited2 = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1
def dfs(s):
    visited2[s] = 1
    print(s, end=' ')
    for i in range(1, n + 1):
        if not visited2[i] and graph[s][i]:
            dfs(i)
def bfs(s):
    q = deque()
    q.append(s)
    visited1[s] = 1
    while q:
        s = q.popleft()
        print(s, end=' ')
        for i in range(1, n + 1):
            if not visited1[i] and graph[s][i]:
                q.append(i)
                visited1[i] = 1
dfs(v)
print()
bfs(v)
