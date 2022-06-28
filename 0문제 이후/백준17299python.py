import sys
from collections import Counter
t = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
count = Counter(arr)
stack = [0]
result = [-1] * t
for i in range(t):
    while stack and count[arr[stack[-1]]] < count[arr[i]]:
        result[stack.pop()] = arr[i]
    stack.append(i)
print(*result)
