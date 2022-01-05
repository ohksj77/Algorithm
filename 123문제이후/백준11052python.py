import sys
t = int(sys.stdin.readline())
arr = [0] + list(map(int, sys.stdin.readline().split()))
num = [0] * (t + 1)
for i in range(1, t + 1):
    for j in range(1, i + 1):
        num[i] = max(num[i], num[i - j] + arr[j])
print(num[t])
