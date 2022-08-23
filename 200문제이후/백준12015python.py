import sys
from bisect import bisect_left
a = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [0]
for i in arr:
    if dp[-1] < i:
        dp.append(i)
    else:
        dp[bisect_left(dp, i)] = i
sys.stdout.write(str(len(dp) - 1))
