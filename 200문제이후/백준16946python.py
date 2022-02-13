from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
zeros = [[0] * m for _ in range(n)]
group = 1
info = {}
info[0] = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(start):
    q = deque()
    q.append(start)
    cnt = 1
    while q:
        i, j = q.popleft()
        zeros[i][j] = group
        for idx in range(4):
            ni, nj = i + dy[idx], j + dx[idx]
            if ni < 0 or ni >= n or nj < 0 or nj >= m or visited[ni][nj] or board[ni][nj] == 1:
                continue
            visited[ni][nj] = True
            q.append((ni, nj))
            cnt += 1
    return cnt
for i in range(n):
    for j in range(m):
        if board[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            w = bfs((i, j))
            info[group] = w
            group += 1
for i in range(n):
    for j in range(m):
        addList = set()
        if board[i][j]:
            for idx in range(4):
                ni, nj = i + dy[idx], j + dx[idx]
                if ni < 0 or ni >= n or nj < 0 or nj >= m:
                    continue
                addList.add(zeros[ni][nj])
            for add in addList:
                board[i][j] += info[add]
                board[i][j] %= 10
for i in board:
    sys.stdout.write("".join(map(str, i)))
    sys.stdout.write('\n')
