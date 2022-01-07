import sys
n = int(sys.stdin.readline())
d = [1, 3] + [0] * (n - 1)
for i in range(2, n + 1):
    d[i] = (d[i - 1] * 2 + d[i - 2]) % 9901
print(d[n])
