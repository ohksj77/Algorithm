import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    cnt = 0
    if k == 1:
        for i in range(1, n - 1, 2):
            cnt += 1
        sys.stdout.write(str(cnt) + "\n")
        continue
    else:
        for i in range(1, n - 1):
            if arr[i] > arr[i - 1] + arr[i + 1]:
                cnt += 1
        sys.stdout.write(str(cnt) + "\n")
