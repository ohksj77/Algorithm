import sys
n = int(sys.stdin.readline())
arr = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(n)], key=lambda x: (x[1], x[0]))
cnt, end = 0, 0
for i, j in arr:
    if i >= end:
        cnt += 1
        end = j
sys.stdout.write(str(cnt))
