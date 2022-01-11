import sys
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
result = []
def dfs(s):
    if m == s:
        print(*result)
        return
    for i in range(n):
        result.append(arr[i])
        dfs(s + 1)
        result.pop()
dfs(0)
