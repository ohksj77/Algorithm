import sys
t = int(sys.stdin.readline())
arr = [0]
for _ in range(t):
    arr.append(int(sys.stdin.readline()))
d = [0, arr[1]]
if t > 1:
    d.append(arr[1] + arr[2])
flag = True
for i in range(3, t + 1):
    d.append(max(d[i - 1], d[i - 3] + arr[i - 1] + arr[i], d[i - 2] + arr[i]))
print(d[t])
