import sys
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
visited = [False] * n
result = []
def dfs(s):
    if m == s:
        print(*result)
        return
    for i in range(n):
        if not visited[i]:
            if s == 0 or result[s - 1] < arr[i]:
                result.append(arr[i])
                visited[i] = True
                dfs(s + 1)
                visited[i] = False
                result.pop()
dfs(0)
