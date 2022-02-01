import sys
dx = [0, 1]
dy = [1, 0]
def convert(s):
    return (ord(s[0]) - ord('A'), ord(s[1]) - ord('1'))
def square(x, y):
    return (x // 3) * 3 + (y // 3)
def can(x, y, num):
    return not c[x][num] and not c2[y][num] and not c3[square(x, y)][num]
def check(x, y, num, what):
    c[x][num] = what
    c2[y][num] = what
    c3[square(x, y)][num] = what
def check_range(x, y):
    return 0 <= x < 9 and 0 <= y < 9
def go(z):
    if z == 81:
        for i in range(9):
            sys.stdout.write(''.join(map(str, a[i])))
            print()
        return True
    x = z // 9
    y = z % 9
    if a[x][y] != 0:
        return go(z + 1)
    else:
        for k in range(2):
            nx, ny = x + dx[k], y + dy[k]
            if not check_range(nx, ny):
                continue
            if a[nx][ny] != 0:
                continue
            for i in range(1, 10):
                for j in range(1, 10):
                    if i == j:
                        continue
                    if domino[i][j]:
                        continue
                    if can(x, y, i) and can(nx, ny, j):
                        check(x, y, i, True)
                        check(nx, ny, j, True)
                        domino[i][j] = domino[j][i] = True
                        a[x][y] = i
                        a[nx][ny] = j
                        if go(z+1):
                            return True
                        check(x, y, i, False)
                        check(nx, ny, j, False)
                        domino[i][j] = domino[j][i] = False
                        a[x][y] = 0
                        a[nx][ny] = 0
    return False

count = 1
while True:
    c = [[False] * 10 for _ in range(10)]
    c2 = [[False] * 10 for _ in range(10)]
    c3 = [[False] * 10 for _ in range(10)]
    domino = [[False] * 10 for _ in range(10)]
    a = [[0] * 9 for _ in range(9)]
    m = int(sys.stdin.readline())
    if m == 0:
        break
    for i in range(m):
        n1, s1, n2, s2 = sys.stdin.readline().rstrip().split()
        n1 = int(n1)
        n2 = int(n2)
        x1, y1 = convert(s1)
        x2, y2 = convert(s2)
        a[x1][y1] = n1
        a[x2][y2] = n2
        domino[n1][n2] = domino[n2][n1] = True
        check(x1, y1, n1, True)
        check(x2, y2, n2, True)
    temp = sys.stdin.readline().rstrip().split()
    for i in range(1, 10):
        s = temp[i-1]
        x, y = convert(s)
        a[x][y] = i
        check(x, y, i, True)
    print('Puzzle', count)
    go(0)
    count += 1
