import sys
sys.setrecursionlimit(10**9)
n = int(sys.stdin.readline())
parent = [-1] * (n + 1)
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)
def dfs(s):
    for i in tree[s]:
        if parent[i] == -1:
            parent[i] = s
            dfs(i)
dfs(1)
for i in range(2, n + 1):
    print(parent[i])
