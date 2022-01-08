import sys
t = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
d = [[0] * t for _ in range(2)]
d[0][0] = arr[0]
result = arr[0]
if t == 1:
    print(arr[0])
else:
    for i in range(1, t):
        d[0][i] = max(d[0][i - 1] + arr[i], arr[i])
        d[1][i] = max(d[1][i - 1] + arr[i], d[0][i - 1])
        result = max(result, d[0][i], d[1][i])
    print(result)
