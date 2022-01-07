import sys
t = int(sys.stdin.readline())
arr = []
for i in range(t):
    arr.append(list(map(int, sys.stdin.readline().split())))
k = 2
for i in range(1, t):
    for j in range(k):
        if j == 0:
            arr[i][j] = arr[i][j] + arr[i - 1][j]
        elif i == j:
            arr[i][j] = arr[i][j] + arr[i - 1][j - 1]
        else:
            arr[i][j] = max(arr[i - 1][j - 1], arr[i - 1][j]) + arr[i][j]
    k += 1
print(max(arr[t - 1]))
