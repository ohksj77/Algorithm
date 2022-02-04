import sys
n, k = map(int, sys.stdin.readline().split())
if k < 5 or k == 26:
    print(0 if k < 5 else n)
    exit()
arr = [set(sys.stdin.readline().rstrip()) for _ in range(n)]
array = [0] * 26
for i in ('a', 'c', 'i', 'n', 't'):
    array[ord(i) - ord('a')] = 1
answer = 0
def dfs(i, count):
    global answer
    if count == k - 5:
        temp = 0
        for word in arr:
            for w in word:
                if not array[ord(w) - ord('a')]:
                    break
            else:
                temp += 1
        answer = max(answer, temp) if answer else temp
        return
    for j in range(i, 26):
        if not array[j]:
            array[j] = 1
            dfs(j, count + 1)
            array[j] = 0
dfs(0, 0)
print(answer)
