import sys
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
result = []
visited = [False] * n
def dfs(s):
    if s == m:
        print(*result)
        return
    for i in range(n):
        if not visited[i]:
            result.append(arr[i])
            visited[i] = True
            dfs(s + 1)
            visited[i] = False
            result.pop()
dfs(0)
