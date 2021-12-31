import sys
t = int(sys.stdin.readline())
arr = []
for _ in range(t):
    x, y = map(int, sys.stdin.readline().split())
    arr.append((x,y))
array = sorted(arr)
for i in array:
    print(i[0], i[1])
