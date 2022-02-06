import sys
from collections import deque
def bfs():
    q = deque()
    q.append((a, ""))
    while q:
        num, result = q.popleft()
        mn = (num * 2) % 10000
        if mn == b:
            return result + 'D'
        elif arr[mn] == 0:
            arr[mn] = 1
            q.append((mn, result + 'D'))
        sn = num - 1 if num != 0 else 9999
        if sn == b:
            return result + 'S'
        elif arr[sn] == 0:
            arr[sn] = 1
            q.append((sn, result + 'S'))
        an = int(num % 1000 * 10 + num / 1000)
        if an == b:
            return result + 'L'
        elif arr[an] == 0:
            arr[an] = 1
            q.append((an, result + 'L'))
        bn = int(num % 10 * 1000 + num // 10)
        if bn == b:
            return result + 'R'
        elif arr[bn] == 0:
            arr[bn] = 1
            q.append((bn, result + 'R'))
t = int(sys.stdin.readline())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    arr = [0 for _ in range(10000)]
    print(bfs())
