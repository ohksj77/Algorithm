import sys
n = int(sys.stdin.readline())
dp = [0 for _ in range(n + 1)]
arr = [i**2 for i in range(1, 317)]
for i in range(1, n + 1):
    index = []
    for j in arr:
        if j > i:
            break
        index.append(dp[i - j])
    dp[i] = min(index) + 1
print(dp[n])
