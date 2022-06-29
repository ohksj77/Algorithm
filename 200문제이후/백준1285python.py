import sys
n = int(sys.stdin.readline())
board = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
def change(x):
    return 'T' if x == 'H' else 'H'
ans = n * n
for bit in range(1 << n):
    sum = 0
    for i in range(n):
        tail = 0
        for j in range(n):
            cur = board[j][i]
            if (bit & (1 << j)) != 0:
                cur = change(cur)
            if cur == 'T':
                tail += 1
        sum += min(tail, n - tail)
    if sum < ans:
        ans = sum
sys.stdout.write(str(ans))
