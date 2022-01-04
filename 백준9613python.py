import sys
import math
t = int(sys.stdin.readline())
for _ in range(t):
    arr = list(map(int, sys.stdin.readline().split()))
    count = 0
    for i in range(1, len(arr)):
        for j in range(i + 1, len(arr)):
            count += math.gcd(arr[i], arr[j])
    print(count)
