import sys
n, m = map(int, sys.stdin.readline().split())
before = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
after = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
def check():
    for i in range(n):
        for j in range(m):
            if before[i][j] != after[i][j]:
                return False
    return True
def reverse(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            before[i][j] = 1 - before[i][j]
cnt = 0
for i in range(n - 2):
    for j in range(m - 2):
        if before[i][j] != after[i][j]:
            reverse(i, j)
            cnt += 1
sys.stdout.write(str(cnt) if check() else "-1")
