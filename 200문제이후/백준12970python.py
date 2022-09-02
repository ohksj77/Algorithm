import sys
n, k = map(int, sys.stdin.readline().split())
a, b = 0, n
while a * b < k and 0 < b:
    a += 1
    b -= 1
if k == 0:
    sys.stdout.write('B' * n)
    exit()
elif b == 0:
    sys.stdout.write('-1')
    exit()
res = k - (a - 1) * b
sys.stdout.write('A' * (a - 1) + 'B' * (b - res) + 'A' + 'B' * res)
