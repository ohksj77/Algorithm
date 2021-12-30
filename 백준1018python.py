import sys
x, y = map(int, sys.stdin.readline().split())
chess = []
min_arr = []
for i in range(x):
    chess.append(input())
for i in range(x - 7):
    for j in range(y - 7):
        countA = 0
        countB = 0
        for m in range(i, i + 8):
            for n in range(j, j + 8):
                if (m + n) % 2 == 0:
                    if chess[m][n] != 'W':
                        countA += 1
                    else:
                        countB += 1
                else:
                    if chess[m][n] != 'B':
                        countA += 1
                    else:
                        countB += 1
        min_arr.append(countA)
        min_arr.append(countB)
print(min(min_arr))
