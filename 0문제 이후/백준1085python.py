import sys
x, y, w, h = map(int, sys.stdin.readline().split())
arr = []
arr.append(w - x)
arr.append(x - 0)
arr.append(h - y)
arr.append(y - 0)
temp = arr[0]
n = 0
for i in range(4):
    if temp >= arr[i]:
        temp = arr[i]
        n = i
print(arr[n])