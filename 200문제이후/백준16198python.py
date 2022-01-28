import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
result = 0
def search(ar, tot):
    global result
    if len(ar) == 3:
        tot += ar[0] * ar[-1]
        result = max(tot, result)
        return
    for i in range(1, len(ar) - 1):
        search(ar[:i] + ar[i + 1:], tot + ar[i - 1] * ar[i + 1])
search(arr, 0)
print(result)
