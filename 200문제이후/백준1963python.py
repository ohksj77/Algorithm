import sys
from collections import deque
t = int(sys.stdin.readline())
prime = [list(map(int, sys.stdin.readline().split())) for _ in range(t)]
arr = [True] * 10001
for i in range(2, 101):
    if arr[i]:
        j = i * 2
        while j < 10001:
            arr[j] = False
            j += i
def bfs(a, b):
    q = deque()
    q.append((a, 0))
    visited = [0 for _ in range(10000)]
    visited[a] = 1
    while q:
        num, cnt = q.popleft()
        if num == b:
            return cnt
        if num < 1000:
            continue
        for i in [1, 10, 100, 1000]:
            n = num - num % (i * 10) // i * i
            for j in range(10):
                if visited[n] == 0 and arr[n]:
                    visited[n] = 1
                    q.append((n, cnt + 1))
                n += i
    return "impossible"
for i, j in prime:
    print(bfs(i, j))
