import sys
length = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(length)]
array = [[i] for i in arr]
for i in range(length):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j]:
            array[i] = array[j] + [arr[i]]
            dp[i] = dp[j]
    dp[i] += 1
flag = 0
tmp = 0
for i in range(length):
    if tmp < dp[i]:
        flag = i
        tmp = dp[i]
print(tmp)
print(*array[flag])
