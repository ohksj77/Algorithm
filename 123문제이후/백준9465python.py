import sys
t = int(sys.stdin.readline())
for _ in range(t):
    d = []
    n = int(sys.stdin.readline())
    d.append(list(map(int, sys.stdin.readline().split())))
    d.append(list(map(int, sys.stdin.readline().split())))
    for i in range(1, n):
        if i == 1:
            d[0][i] += d[1][i - 1]
            d[1][i] += d[0][i - 1]
        else:
            d[0][i] += max(d[1][i - 1], d[1][i - 2])
            d[1][i] += max(d[0][i - 1], d[0][i - 2])
    print(max(d[0][n - 1], d[1][n - 1]))
