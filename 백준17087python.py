import sys
import math
n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
dist = []
for i in arr:
    if s - i > 0:
        dist.append(s - i)
    else:
        dist.append(i - s)
result = dist[0]
for i in dist:
    result = math.gcd(result, i)
print(result)
