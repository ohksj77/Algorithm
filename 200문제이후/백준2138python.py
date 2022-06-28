import sys
n = int(sys.stdin.readline())
before = list(map(int, sys.stdin.readline().rstrip()))
after = list(map(int, sys.stdin.readline().rstrip()))
def switch(s, cnt):
    if cnt == 1:
        s[0] = 1 - s[0]
        s[1] = 1 - s[1]
    for i in range(1, n):
        if s[i - 1] != after[i - 1]:
            cnt += 1
            s[i - 1] = 1 - s[i - 1]
            s[i] = 1 - s[i]
            if i != n - 1:
                s[i + 1] = 1 - s[i + 1]
    if s == after:
        return cnt
    return -1
result1 = switch(before[:], 0)
result2 = switch(before[:], 1)
if result1 >= 0 and result2 >= 0:
    sys.stdout.write(str(min(result1, result2)))
elif result1 >= 0 and result2 < 0:
    sys.stdout.write(str(result1))
elif result1 < 0 and result2 >= 0:
    sys.stdout.write(str(result2))
else:
    sys.stdout.write("-1")
