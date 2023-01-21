import sys
sys.setrecursionlimit(10**6)

n, m, r = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    arr[u].append(v)
    arr[v].append(u)

visited = [0] * (n + 1)
cnt = 1

def dfs(r):
    global cnt
    visited[r] = cnt
    for a in sorted(arr[r]):
        if not visited[a]:
            cnt += 1
            dfs(a)

dfs(r)
for i in range(1, n + 1):
    sys.stdout.write(str(visited[i]) + '\n')
