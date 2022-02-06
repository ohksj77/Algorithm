import sys
from copy import deepcopy
n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = 0
def move(dir):
    if dir == 0:
        for i in range(n):
            idx = 0
            for j in range(1, n):
                if board[j][i]:
                    tmp = board[j][i]
                    board[j][i] = 0
                    if board[idx][i] == 0:
                        board[idx][i] = tmp
                    elif board[idx][i] == tmp:
                        board[idx][i] = tmp * 2
                        idx += 1
                    else:
                        idx += 1
                        board[idx][i] = tmp
    elif dir == 1:
        for i in range(n):
            idx = n - 1
            for j in range(n - 2, -1, -1):
                if board[j][i]:
                    tmp = board[j][i]
                    board[j][i] = 0
                    if board[idx][i] == 0:
                        board[idx][i] = tmp
                    elif board[idx][i] == tmp:
                        board[idx][i] = tmp * 2
                        idx -= 1
                    else:
                        idx -= 1
                        board[idx][i] = tmp
    elif dir == 2:
        for j in range(n):
            idx = 0
            for i in range(1, n):
                if board[j][i]:
                    tmp = board[j][i]
                    board[j][i] = 0
                    if board[j][idx] == 0:
                        board[j][idx] = tmp
                    elif board[j][idx] == tmp:
                        board[j][idx] = tmp * 2
                        idx += 1
                    else:
                        idx += 1
                        board[j][idx] = tmp
    else:
        for j in range(n):
            idx = n - 1
            for i in range(n - 2, -1, -1):
                if board[j][i]:
                    tmp = board[j][i]
                    board[j][i] = 0
                    if board[j][idx] == 0:
                        board[j][idx] = tmp
                    elif board[j][idx] == tmp:
                        board[j][idx] = tmp * 2
                        idx -= 1
                    else:
                        idx -= 1
                        board[j][idx] = tmp
def dfs(count):
    global board, answer
    if count == 5:
        for i in range(n):
            boardMax = max(board[i])
            answer = max(answer, boardMax)
        return
    temp = deepcopy(board)
    for i in range(4):
        move(i)
        dfs(count + 1)
        board = deepcopy(temp)
dfs(0)
print(answer)
