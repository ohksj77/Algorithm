import sys
t = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
sumArr = [arr[0]]
for i in range(t - 1):
    sumArr.append(max(sumArr[i] + arr[i + 1], arr[i + 1]))
print(max(sumArr))
