import sys
n = int(sys.stdin.readline())
time = sorted(list(map(int, sys.stdin.readline().split())), key=lambda x: x)
for i in range(1, n):
    time[i] += time[i - 1]
sys.stdout.write(str(sum(time)))
