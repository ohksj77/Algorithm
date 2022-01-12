import sys
n, m = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))
result = []
def dfs():
    if len(result) == m:
        print(*result)
        return
    last = 0
    for i in range(n):
        if last != arr[i]:
            result.append(arr[i])
            last = arr[i]
            dfs()
            result.pop()
dfs()
