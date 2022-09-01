import sys
n = sys.stdin.readline().rstrip()
if '0' not in n or int(n) % 3 != 0:
    sys.stdout.write('-1')
    exit()
arr = [int(i) for i in n]
arr.sort(reverse=True)
for i in arr:
    sys.stdout.write(str(i))
