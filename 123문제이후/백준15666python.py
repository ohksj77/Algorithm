import sys
n, m = map(int, sys.stdin.readline().split())
arr = sorted(list(set(map(int, sys.stdin.readline().split()))))
result = []
def dfs(s):
    if s == m:
        print(*result)
        return
    for i in range(len(arr)):
        if s == 0 or result[-1] <= arr[i]:
            result.append(arr[i])
            dfs(s + 1)
            result.pop()
dfs(0)
