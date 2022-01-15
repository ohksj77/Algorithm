import sys
n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
def bitmask():
    global max_num
    for i in range(1 << n * m):
        total = 0
        for row in range(n):
            rowsum = 0
            for col in range(m):
                idx = row * m + col
                if i & (1 << idx) != 0:
                    rowsum = rowsum * 10 + arr[row][col]
                else:
                    total += rowsum
                    rowsum = 0
            total += rowsum
        for col in range(m):
            colsum = 0
            for row in range(n):
                idx = row * m + col
                if i & (1 << idx) == 0:
                    colsum = colsum * 10 + arr[row][col]
                else:
                    total += colsum
                    colsum = 0
            total += colsum
        max_num = max(max_num, total)
max_num = 0
bitmask()
print(max_num)
