import sys
t = int(sys.stdin.readline())
arr = []
for _ in range(t):
    arr.append(sys.stdin.readline().strip())
set_arr = set(arr)
arr = list(set_arr)
arr.sort()
arr.sort(key=len)
for w in arr:
    print(w)
