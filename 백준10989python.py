import sys
t = int(sys.stdin.readline())
arr = [0] * 10001
for _ in range(t):
    n = int(sys.stdin.readline())
    arr[n] = arr[n] + 1
for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)
