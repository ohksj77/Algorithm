import sys
t = int(sys.stdin.readline())
arr = [0] + list(map(int, sys.stdin.readline().split()))
num = [False] * (t + 1)
for i in range(1, t + 1):
    for j in range(1, i + 1):
        if not num[i]:
            num[i] = num[i - j] + arr[j]
        else:
            num[i] = min(num[i], num[i - j] + arr[j])
print(num[t])
