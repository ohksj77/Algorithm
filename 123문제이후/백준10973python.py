import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
def permutation():
    for i in range(len(arr) - 1, 0, -1):
        prev = arr[i - 1]
        now = arr[i]
        if prev > now:
            for j in range(len(arr) - 1, i - 1, -1):
                if arr[j] < prev:
                    max_index = j
                    break
            arr[i - 1], arr[max_index] = arr[max_index], arr[i - 1]
            arr[i:] = sorted(arr[i:], key=lambda x: -x)
            return
if arr == (sorted(arr)):
    print(-1)
else:
    permutation()
    print(*arr, sep=' ')
