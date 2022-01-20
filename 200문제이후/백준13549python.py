import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
max_n = 100001
distance = [-1 for _ in range(max_n)]
distance[n] = 0
def bfs():
    q = deque()
    q.append(n)
    while q:
        a = q.popleft()
        if a == k:
            print(distance[a])
            exit()
        if 0 < a * 2 < max_n and distance[a * 2] == -1:
            distance[a * 2] = distance[a]
            q.appendleft(a * 2)
        if 0 <= a + 1 < max_n and distance[a + 1] == -1:
            distance[a + 1] = distance[a] + 1
            q.append(a + 1)
        if 0 <= a - 1 < max_n and distance[a - 1] == -1:
            distance[a - 1] = distance[a] + 1
            q.append(a - 1)
bfs()
