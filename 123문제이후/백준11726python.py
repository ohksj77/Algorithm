import sys
n = int(sys.stdin.readline())
arr = [1, 1] + [0] * n
for i in range(2, n + 1):
    arr[i] = arr[i - 2] + arr[i - 1]
print(arr[n] % 10007)
