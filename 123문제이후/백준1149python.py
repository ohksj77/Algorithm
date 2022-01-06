import sys
t = int(sys.stdin.readline())
arr = []
for _ in range(t):
    arr.append(list(map(int, sys.stdin.readline().split())))
for i in range(1, t):
    arr[i][0] = min(arr[i - 1][1], arr[i - 1][2]) + arr[i][0]
    arr[i][1] = min(arr[i - 1][0], arr[i - 1][2]) + arr[i][1]
    arr[i][2] = min(arr[i - 1][0], arr[i - 1][1]) + arr[i][2]
sys.stdout.write(str(min(arr[t - 1][0], arr[t - 1][1], arr[t - 1][2])))
