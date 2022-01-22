import sys
n = int(sys.stdin.readline())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
alpha = [0 for _ in range(26)]
for i in range(n):
    a = 0
    for word in arr[i][::-1]:
        alpha[ord(word) - ord('A')] += (10 ** a)
        a += 1
alpha.sort(reverse=True)
result = 0
num = 9
for i in alpha:
    if i == 0:
        break
    result += (num * i)
    num -= 1
print(result)
