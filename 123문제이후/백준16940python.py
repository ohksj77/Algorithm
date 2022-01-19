import sys
from collections import deque
n = int(sys.stdin.readline())
arr = [set() for _ in range(n + 1)]
arr[0].add(1)
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].add(b)
    arr[b].add(a)
def bfs():
    queue = deque()
    queue.append(0)
    idx = 0
    ans = list(map(int, sys.stdin.readline().split()))
    for i in ans:
        while i not in arr[queue[idx]]:
            idx += 1
            if idx == len(queue):
                return 0
        queue.append(i)
    return 1
print(bfs())
