import sys
t = int(sys.stdin.readline())
mod = 1000000009
num = []
for _ in range(t):
    num.append(int(sys.stdin.readline()))
arr = [0, 1, 2, 4] + [0] * (max(num) + 1)
for i in range(4, max(num) + 1):
    arr[i] = (arr[i - 1] + arr[i - 2] + arr[i - 3]) % mod
for i in num:
    sys.stdout.write(str(arr[i]))
    print()
