import sys
arr = []
for _ in range(9):
    arr.append(int(sys.stdin.readline()))
s = sum(arr)
flag = False
for i in range(9):
    if flag:
        break
    for j in range(i + 1, 9):
        if s - arr[i] - arr[j] == 100:
            arr.pop(j)
            arr.pop(i)
            print(*sorted(arr))
            flag = True
            break
