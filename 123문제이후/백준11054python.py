import sys
t = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
d1 = [0 for _ in range(t)]
d2 = [0 for _ in range(t)]
result = [0 for _ in range(t)]
for i in range(t):
    for j in range(i):
        if a[i] > a[j] and d1[i] < d1[j]:
            d1[i] = d1[j]
    d1[i] += 1
for i in range(t - 1, -1, -1):
    for j in range(t - 1, i, -1):
        if a[i] > a[j] and d2[i] < d2[j]:
            d2[i] = d2[j]
    d2[i] += 1
for i in range(t):
    result[i] = d1[i] + d2[i] - 1
print(max(result))
