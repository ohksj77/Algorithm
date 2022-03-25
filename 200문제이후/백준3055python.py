import sys
from collections import deque
from copy import deepcopy
r, c = map(int, sys.stdin.readline().split())
board = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
dr = [[1, 0], [0, 1], [-1, 0], [0, -1]]
water = deque()
for i in range(r):
    for j in range(c):
        if board[i][j] == 'S':
            hedgehog = [i, j]
        elif board[i][j] == '*':
            water.append([i, j])
def moveWater():
    while water:
        x, y = water.popleft()
        for m, n in dr:
            nx = x + m
            ny = y + n
            if 0 <= nx < r and 0 <= ny < c:
                if board[nx][ny] == '.':
                    board[nx][ny] = '*'
                    water.append([nx, ny])
def bfs():
    q = deque()
    q.append((hedgehog[0], hedgehog[1], 1))
    visited[hedgehog[0]][hedgehog[1]] = 1
    while q:
        moveWater()
        length = len(q)
        while length:
            x, y, cnt = q.popleft()
            for dx, dy in dr:
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c:
                    if board[nx][ny] == 'D':
                        return cnt
                    if board[nx][ny] == '.' and not visited[nx][ny]:
                        visited[nx][ny] = 1
                        q.append((nx, ny, cnt + 1))
            length -= 1
    return 'KAKTUS'
sys.stdout.write(str(bfs()))
