import sys
arr = [0, 1, 2, 4] + [0] * 1000
for i in range(4, 1001):
    arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    print(arr[n])
