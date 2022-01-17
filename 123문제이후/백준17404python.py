import sys
InF = 2147000000
n = int(sys.stdin.readline())
arr = []
result = InF
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
for i in range(3):
    d = [[InF, InF, InF] for _ in range(n)]
    d[0][i] = arr[0][i]
    for j in range(1, n):
        d[j][0] = arr[j][0] + min(d[j - 1][1], d[j - 1][2])
        d[j][1] = arr[j][1] + min(d[j - 1][0], d[j - 1][2])
        d[j][2] = arr[j][2] + min(d[j - 1][0], d[j - 1][1])
    for j in range(3):
        if i != j:
            result = min(result, d[-1][j])
print(result)
