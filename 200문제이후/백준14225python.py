import sys
n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
arr = [0] * 10000000
def dfs(i, a):
    if i == n:
        return
    a += s[i]
    arr[a] = 1
    dfs(i + 1, a)
    dfs(i + 1, a - s[i])
dfs(0, 0)
for i in arr:
    if i == 0:
        print(arr[1:].index(i) + 1)
        break
