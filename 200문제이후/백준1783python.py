import sys
n, m = map(int, sys.stdin.readline().split())
if n == 1:
    sys.stdout.write('1')
elif n == 2:
    sys.stdout.write(str(min(4, (m - 1) // 2 + 1)))
elif m <= 6:
    sys.stdout.write(str(min(4, m)))
else:
    sys.stdout.write(str(m - 2))
