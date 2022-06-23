import sys
from collections import deque
s, t = map(int, sys.stdin.readline().split())
if s == t:
    sys.stdout.write("0")
    exit()
def bfs():
    q = deque()
    q.append((s, ""))
    check = [s]
    operation = ["*", "+", "-", "/"]
    while q:
        num, op = q.popleft()
        if num == t:
            return op
        for i, nextNum in enumerate([num * num, num + num, 0, 1]):
            if nextNum > t:
                continue
            if nextNum not in check:
                q.append((nextNum, op + operation[i]))
                check.append(nextNum)
    return "-1"
sys.stdout.write(bfs())
