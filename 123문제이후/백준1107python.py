import sys
ch = int(sys.stdin.readline())
err = int(sys.stdin.readline())
if err:
    butt = list(sys.stdin.readline().split())
else:
    butt = []
result = abs(100 - ch)
for i in range(1000001):
    for j in str(i):
        if j in butt:
            break
    else:
        result = min(result, len(str(i)) + abs(i - ch))
print(result)
