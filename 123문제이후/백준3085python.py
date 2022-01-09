import sys
t = int(sys.stdin.readline())
arr = []
result = 1
for _ in range(t):
    arr.append(list(sys.stdin.readline()))
def search():
    global result
    for i in range(t):
        count = 1
        for j in range(t - 1):
            if arr[i][j] == arr[i][j + 1]:
                count += 1
                result = max(result, count)
            else:
                count = 1
    for i in range(t):
        count = 1
        for j in range(t - 1):
            if arr[j][i] == arr[j + 1][i]:
                count += 1
                result = max(result, count)
            else:
                count = 1
for i in range(t):
    for j in range(t - 1):
        arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
        search()
        arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
for i in range(t):
    for j in range(t - 1):
        arr[j][i], arr[j + 1][i] = arr[j + 1][i], arr[j][i]
        search()
        arr[j][i], arr[j + 1][i] = arr[j + 1][i], arr[j][i]
print(result)
import sys
t = int(sys.stdin.readline())
arr = []
result = 1
for _ in range(t):
    arr.append(list(sys.stdin.readline()))
def search():
    global result
    for i in range(t):
        count = 1
        for j in range(t - 1):
            if arr[i][j] == arr[i][j + 1]:
                count += 1
                result = max(result, count)
            else:
                count = 1
    for i in range(t):
        count = 1
        for j in range(t - 1):
            if arr[j][i] == arr[j + 1][i]:
                count += 1
                result = max(result, count)
            else:
                count = 1
for i in range(t):
    for j in range(t - 1):
        arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
        search()
        arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
for i in range(t):
    for j in range(t - 1):
        arr[j][i], arr[j + 1][i] = arr[j + 1][i], arr[j][i]
        search()
        arr[j][i], arr[j + 1][i] = arr[j + 1][i], arr[j][i]
print(result)
