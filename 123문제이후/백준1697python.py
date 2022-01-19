import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
max_n = 100000
distance = [0] * (max_n + 1)
def bfs():
    q = deque()
    q.append(n)
    while q:
        a = q.popleft()
        if a == k:
            print(distance[a])
            exit()
        for i in (a - 1, a + 1, a * 2):
            if 0 <= i <= max_n and not distance[i]:
                distance[i] = distance[a] + 1
                q.append(i)
bfs()
