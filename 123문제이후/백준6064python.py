import sys
def func(m, n, x, y):
    while x <= m * n:
        if(x - y) % n == 0:
            return x
        x += m
    return -1
t = int(sys.stdin.readline())
for _ in range(t):
    m, n, x, y = (map(int, sys.stdin.readline().split()))
    print(func(m, n, x, y))
