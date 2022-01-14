from itertools import combinations
import sys
n = int(sys.stdin.readline())
arr = [x for x in range(n)]
cases = list(combinations(arr, int(n/2)))
for i in range(n):
    arr[i] = list(map(int, sys.stdin.readline().split()))
mini = 100 * n * n
for i in cases:
    a, b = 0, 0
    for j in i:
        for k in i:
            a += arr[j][k]
    m = [x for x in range(n) if x not in i]
    for j in m:
        for k in m:
            b += arr[j][k]
    mini = min(mini, abs(a - b))
print(mini)
