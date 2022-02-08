import sys
from collections import deque
from copy import deepcopy
n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
virus = [(i, j) for i in range(n) for j in range(m) if board[i][j] == 2]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def safe(graph):
    global answer
    cnt = 0
    for i in range(n):
        cnt += graph[i].count(0)
    answer = max(answer, cnt)
def bfs():
    q = deque(virus)
    temp = deepcopy(board)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] == 0:
                temp[nx][ny] = 2
                q.append((nx, ny))
    safe(temp)
def wall(count):
    if count == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1
                wall(count + 1)
                board[i][j] = 0
answer = 0
wall(0)
print(answer)
