import sys
r, c = map(int, sys.stdin.readline().split())
arr = [list(map(lambda x : ord(x) - 65, sys.stdin.readline().rstrip())) for _ in range(r)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
answer = 1
array = [0] * 26
array[arr[0][0]] = 1
def search(i, j, count):
    global answer
    answer = max(count, answer)
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < r and 0 <= ny < c and array[arr[nx][ny]] == 0:
            array[arr[nx][ny]] = 1
            search(nx, ny, count + 1)
            array[arr[nx][ny]] = 0
search(0, 0, 1)
print(answer)
