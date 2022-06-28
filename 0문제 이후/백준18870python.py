import sys
t = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
array = sorted(list(set(arr)))
dic = {array[i]: i for i in range(len(array))}
for i in arr:
    print(dic[i], end=' ')
