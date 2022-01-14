import sys
n = int(sys.stdin.readline())
arr = sys.stdin.readline().rstrip().split()
d = [False] * 10
max_n = ''
min_n = ''
def is_ok(i, j, k):
    if k == '<':
        return i < j
    if k == '>':
        return i > j
    return True
def dfs(count, s):
    global max_n, min_n
    if count == n + 1:
        if not len(min_n):
            min_n = s
        else:
            max_n = s
        return
    for i in range(10):
        if not d[i]:
            if count == 0 or is_ok(s[-1], str(i), arr[count - 1]):
                d[i] = True
                dfs(count + 1, s + str(i))
                d[i] = False
dfs(0, "")
print(max_n)
print(min_n)
