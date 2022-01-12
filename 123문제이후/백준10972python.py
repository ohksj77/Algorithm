import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
def nextPermutation():
    for i in range(len(arr) - 1, 0, -1):
        prev = arr[i - 1]
        now = arr[i]
        if prev < now:
            for j in range(len(arr) - 1, i - 1, -1):
                if arr[j] > prev:
                    arr[j], arr[i - 1] = arr[i - 1], arr[j]
                    return i
if arr == sorted(arr, key=lambda x:-x):
    print(-1)
else:
    i = nextPermutation()
    num = sorted(arr[i:])
    print(*arr[:i], *num, sep=' ')
