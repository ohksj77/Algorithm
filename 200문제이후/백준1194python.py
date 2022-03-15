import sys
from collections import deque
from copy import deepcopy
n, m = map(int, sys.stdin.readline().split())
board = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(n)]
dr = [[1, 0], [-1, 0], [0, 1], [0, -1]]
def bfs():
    q = deque()
    one = [[i, j] for i in range(n) for j in range(m) if board[i][j] == '0']
    alpha = [0] * 6
    q.append((one[0][0], one[0][1], 0, alpha))
    while q:
        x, y, d, a = q.popleft()
        for dx, dy in dr:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m:
                array = deepcopy(a)
                tmp = board[nx][ny]
                if tmp == '1':
                    return d + 1
                elif tmp == '.' or tmp == '0':
                    q.append((nx, ny, d + 1, array))
                elif tmp.islower():
                    if not array[ord(tmp) - ord('a')]:
                        array[ord(tmp) - ord('a')] = 1
                        q.append((nx, ny, d + 1, array))
                    else:
                        q.append((nx, ny, d + 1, array))
                elif tmp.isupper() and array[ord(tmp) - ord('A')]:
                    q.append((nx, ny, d + 1, array))
    return -1
print(bfs())
