import sys
t = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
d = [0 for _ in range(t)]
for i in range(t):
    for j in range(i):
        if a[i] < a[j] and d[i] < d[j]:
            d[i] = d[j]
    d[i] += 1
print(max(d))
