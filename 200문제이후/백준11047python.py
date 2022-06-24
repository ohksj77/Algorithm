import sys
n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]
for i in range(n):
    if coins[i] > k:
        coins = coins[:i]
        break
for i in range(len(coins)):
    if k % coins[i] != 0:
        coins = coins[i - 1:]
        break
cnt = 0
for i in reversed(range(len(coins))):
    cnt += k // coins[i]
    k %= coins[i]
sys.stdout.write(str(cnt))
