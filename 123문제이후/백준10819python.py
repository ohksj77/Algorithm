import itertools
import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
arr2 = list(itertools.permutations(arr, n))
result = 0
for i in range(len(arr2)):
    current = 0
    for j in range(0, n - 1):
        current += abs(arr2[i][j] - arr2[i][j + 1])
    if current > result:
        result = current
print(result)
