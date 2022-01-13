import sys
from itertools import combinations
while True:
    arr = list(map(int, sys.stdin.readline().split()))
    if arr[0] == 0:
        break
    del arr[0]
    result = list(combinations(arr, 6))
    for i in result:
        for j in i:
            print(j, end=' ')
        print()
    print()
