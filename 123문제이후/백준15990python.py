import sys
max_n = 100001
mod = 1000000009
arr = [[0, 0, 0, 0] for _ in range(max_n)]
arr[1] = [1, 0, 0]
arr[2] = [0, 1, 0]
arr[3] = [1, 1, 1]
for i in range(4, 100001):
    arr[i][0] = (arr[i - 1][1] + arr[i - 1][2]) % mod
    arr[i][1] = (arr[i - 2][0] + arr[i - 2][2]) % mod
    arr[i][2] = (arr[i - 3][0] + arr[i - 3][1]) % mod
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    print(sum(arr[n]) % mod)
