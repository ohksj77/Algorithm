import sys
n = int(sys.stdin.readline())
d = [[1] * 10]
for i in range(n):
    d.append([0] * 10)
for i in range(1, n + 1):
    for j in range(0, 10):
        for k in range(j + 1):
            d[i][j] += d[i - 1][k]
sys.stdout.write(str(d[n][9] % 10007))
