import sys
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
ten = 0
result = []
for i in range(m):
    ten += arr[-1] * (a ** i)
    arr.pop()
while ten:
    result.append(str(ten % b))
    ten //= b
print(' '.join(result[::-1]))
