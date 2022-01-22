import sys
from collections import deque
v = int(sys.stdin.readline())
tree = [[] for _ in range(v + 1)]
for _ in range(v):
    arr = list(map(int, sys.stdin.readline().split()))
    for i in range(1, len(arr) - 1, 2):
        tree[arr[0]].append([arr[i], arr[i + 1]])
def bfs(i):
    q = deque()
    visited = [-1] * (v + 1)
    q.append(i)
    visited[i] = 0
    max_n = [0, 0]
    while q:
        n = q.popleft()
        for a in tree[n]:
            if visited[a[0]] == -1:
                visited[a[0]] = visited[n] + a[1]
                q.append(a[0])
                if max_n[0] < visited[a[0]]:
                    max_n[0] = visited[a[0]]
                    max_n[1] = a[0]
    return max_n
array = bfs(1)
print(bfs(array[1])[0])
