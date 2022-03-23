import sys
from bisect import bisect_left
length = int(sys.stdin.readline())
arr = [0] + list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(length + 1)]
compare = [-1000000001]
maxNum = 0
for i in range(1, length + 1):
    if compare[-1] < arr[i]:
        compare.append(arr[i])
        dp[i] = len(compare) - 1
        maxNum = dp[i]
    else:
        dp[i] = bisect_left(compare, arr[i])
        compare[dp[i]] = arr[i]
print(maxNum)
result = []
for i in range(length, 0, -1):
    if dp[i] == maxNum:
        result.append(arr[i])
        maxNum -= 1
print(*(reversed(result)))
