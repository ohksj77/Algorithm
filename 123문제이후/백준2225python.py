import sys
n, k = map(int, sys.stdin.readline().split())
dp = [1]
dp += [0] * n
for i in range(1, k + 1):
    for j in range(1, n + 1):
        dp[j] += dp[j - 1]
sys.stdout.write(str(dp[n] % 1000000000))
