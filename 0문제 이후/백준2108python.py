import sys
from collections import Counter
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort()
count = Counter(arr).most_common()
print(round(sum(arr)/n))
print(arr[len(arr)//2])
if len(count) > 1:
    if count[0][1] == count[1][1]:
        print(count[1][0])
    else:
        print(count[0][0])
else:
    print(count[0][0])
print(arr[-1] - arr[0])
