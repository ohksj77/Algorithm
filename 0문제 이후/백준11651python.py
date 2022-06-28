import sys
t = int(sys.stdin.readline())
arr = []
for _ in range(t):
    x, y = map(int, sys.stdin.readline().split())
    arr.append((y, x))
array = sorted(arr)
for i in array:
    print(i[1], i[0])
