import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
board = []
temp = []
for i in range(n):
    board.append(list(sys.stdin.readline().rstrip()))
    for j in range(m):
        if board[i][j] == "o":
            temp.append((i, j))
q = deque()
q.append((temp[0][0], temp[0][1], temp[1][0], temp[1][1], 0))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    while q:
        x1, y1, x2, y2, count = q.popleft()
        if count >= 10:
            return -1
        for i in range(4):
            mx1 = x1 + dx[i]
            my1 = y1 + dy[i]
            mx2 = x2 + dx[i]
            my2 = y2 + dy[i]
            if 0 <= mx1 < n and 0 <= my1 < m and 0 <= mx2 < n and 0 <= my2 < m:
                if board[mx1][my1] == "#":
                    mx1, my1 = x1, y1
                if board[mx2][my2] == "#":
                    mx2, my2 = x2, y2
                q.append((mx1, my1, mx2, my2, count + 1))
            elif 0 <= mx1 < n and 0 <= my1 < m:
                return count + 1
            elif 0 <= mx2 < n and 0 <= my2 < m:
                return count + 1
    return -1
print(bfs())
