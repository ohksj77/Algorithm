import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    for i in range(n):
        tmp = arr[:i] + arr[i + 1:]
        num = tmp[0]
        for j in range(1, n - 1):
            num ^= tmp[j]
        if num == arr[i]:
            sys.stdout.write(str(num) + '\n')
            break
