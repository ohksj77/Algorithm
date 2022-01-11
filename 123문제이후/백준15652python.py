import sys
n, m = map(int, sys.stdin.readline().split())
arr = []
def dfs(s):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(s, n + 1):
        arr.append(i)
        dfs(i)
        arr.pop()
dfs(1)
