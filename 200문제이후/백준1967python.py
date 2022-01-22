import sys
sys.setrecursionlimit(100000)
n = int(sys.stdin.readline())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, sys.stdin.readline().split())
    tree[a].append((b, c))
max_n = 0
def dfs(n, d):
    global max_n
    left, right = 0, 0
    for node, w in tree[n]:
        temp = dfs(node, w)
        if left <= right:
            left = max(left, temp)
        else:
            right = max(right, temp)
    max_n = max(max_n, left + right)
    return max(left + d, right + d)
dfs(1, 0)
print(max_n)
